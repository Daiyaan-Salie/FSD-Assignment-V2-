import pandas as pd
import numpy as np
from sqlalchemy.engine import URL, create_engine, Inspector
from app import main
from app.dataframes import df_Index_Constituents, df_Industry_Classification_Benchmark, df_BA_Beta_Output
from app.weights_and_ics import getICsAndWeights
from app.calc_stats import CalcStats
from app.betas_mkt_spec_vols import getBetasMktAndSpecVols
from flask import jsonify, request
from flask_cors import CORS
import json


app = main.app

CORS(app, resources={r"/*":{'origins':"*"}})

Date_1_year = '2018'
Date_1_quarter = 1

Date_2_year = '2018'
Date_2_quarter = 4

IndexCode_temp = "TOPI"

@app.route("/api/synthetictable", methods=["GET"])

def Synthetic_Table():#(Date_1_year,Date_1_quarter,Date_2_year,Date_2_quarter,IndexCode_temp):
    #Hardcoded 
    Date_1_year = '2018'
    Date_1_quarter = 1

    Date_2_year = '2018'
    Date_2_quarter = 4

    IndexCode_temp = "TOPI"
    #---------------------

    Quarter_month = {1:3, 2:6, 3:9, 4:12}
    Date_1_month = str(Quarter_month[Date_1_quarter])
    Date_2_month = str(Quarter_month[Date_2_quarter])

    Date_1 = Date_1_year +"-"+ Date_1_month+"-01"
    Date_2 = Date_2_year +"-"+ Date_2_month+"-28"

    Date_1 = pd.to_datetime(Date_1, format = "%Y-%m-%d")
    Date_2 = pd.to_datetime(Date_2, format = "%Y-%m-%d")

    Dates = (df_Index_Constituents.loc[(df_Index_Constituents["Date"] >= Date_1) & (df_Index_Constituents["Date"] <= Date_2)]).loc[:,"Date"].unique() #get list of quarters between two dates
    Industry_codes = df_Industry_Classification_Benchmark.loc[:,"Industry Code"].unique() #find all the industry codes
    Industry_names = df_Industry_Classification_Benchmark.loc[:,"Industry"].unique()

    #IndexCode is provided by user: "ALSI", "FLED", "LRGC", "MIDC", "SMLC", "TOPI", "RESI", "FINI", "INDI", "PCAP", "SAPY" or "ALTI"

    df_Storage = pd.DataFrame(columns=['Date', 'Industry', 'Weight', 'Beta', 'SysVol', 'SpecVar'])
    #put in If Else statement for conditions where the weights is 0 which will give error
    it = 0
    for i in Dates:
        for t in range(len(Industry_codes)):
            it = it + 1
            print("iteration:",it)
            print("Date:",i)
            
            Subsector = (df_Industry_Classification_Benchmark.loc[df_Industry_Classification_Benchmark["Industry Code"] == Industry_codes[t]]).loc[:,"Sub-Sector Code"].unique()
            #Select index code - Provided by the user

            #run through first function
            Results_1 = getICsAndWeights(i,IndexCode_temp,df_Index_Constituents)
            Results_1_filtered = Results_1.loc[Results_1["ICB Sub-Sector"].isin(Subsector)] 

            #Place if-Else statement here:
            if len(Results_1_filtered)>0:

                Filtered_GMC = np.array(Results_1_filtered.loc[:,"Gross Market Capitalisation"])
                Total_GMC = np.array(Results_1.loc[:,"Gross Market Capitalisation"])

                Industry_Weights = pd.DataFrame((Filtered_GMC/np.sum(Total_GMC)))
                Industry_Weight_tot = "{:.2%}".format(float(np.sum(Industry_Weights)))

                ICs_temp = Results_1_filtered["Alpha"]
                mktIndexCode_temp = "J203"
                Results_2 = getBetasMktAndSpecVols(i,ICs_temp,df_BA_Beta_Output,mktIndexCode_temp)

                mktVol_temp = Results_2["mktVol"][0]
                betas_temp = np.transpose(np.matrix(Results_2["Betas"]))
                specVols_temp = np.transpose(np.matrix(Results_2["specVols"]))

                Results_3 = CalcStats(Industry_Weights,betas_temp,specVols_temp,mktVol_temp)

                beta_output = Results_3["pfBeta"][0]
                SysVol_output = "{:.3%}".format(float(Results_3["pfSysVol"][0]))
                SpecVar_output = round(float(Results_3["pfSpecVol"][0]),6)
                
                date_output = pd.to_datetime(i)
                date_output = str(date_output.year)+"-Q"+str(date_output.quarter)


                df_Storage = df_Storage.append({'Date': date_output, 'Industry': Industry_names[t], 'Weight': Industry_Weight_tot, 'Beta' : Results_3["pfBeta"], 'SysVol' : SysVol_output, 'SpecVar' : SpecVar_output}, ignore_index=True)
                print("Industry:", Industry_names[t])
            else:
                weight_output = "{:.2%}".format(0.000)
                date_output = pd.to_datetime(i)
                date_output = str(date_output.year)+"-Q"+str(date_output.quarter)
                df_Storage = df_Storage.append({'Date': date_output, 'Industry': Industry_names[t], 'Weight': weight_output, 'Beta' : "     -", 'SysVol' : "     -", 'SpecVar' : "     -"}, ignore_index=True)
                print("Industry:", Industry_names[t])

    return df_Storage.to_json()



