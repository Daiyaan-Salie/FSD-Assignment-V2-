'''
    Author: Kenneth Ssekimpi
'''
from app.main import frames_dict
import pandas as pd

# Retrieving all the necessary dataframes from the dictionary to work with downstream
df_BA_Beta_Output = pd.DataFrame(frames_dict['tbl_BA_Beta_Output'])
df_Beta_Output = pd.DataFrame(frames_dict['tbl_Beta_Output'])
df_EOD_Equity_Data = pd.DataFrame(frames_dict['tbl_EOD_Equity_Data'])
df_EOD_Interest_Rate_Data = pd.DataFrame(frames_dict['tbl_EOD_Interest_Rate_Data'])
df_FTSEJSE_Index_Series = pd.DataFrame(frames_dict['tbl_FTSEJSE_Index_Series'])
df_Index_Constituents = pd.DataFrame(frames_dict['tbl_Index_Constituents'])
df_Industry_Classification_Benchmark = pd.DataFrame(frames_dict['tbl_Industry_Classification_Benchmark'])


'''
df_Industry_Classification_Benchmark = frames_dict["tbl_Industry_Classification_Benchmark"]
df_Index_Constituents = frames_dict["tbl_Index_Constituents"]
df_BA_Beta_Output = frames_dict["tbl_BA_Beta_Output"]
df_FTSEJSE_Index_Series = frames_dict["tbl_FTSEJSE_Index_Series"]
df_EOD_Equity_Data = frames_dict["tbl_EOD_Equity_Data"]
df_EOD_Interest_Rate_Data = frames_dict["tbl_EOD_Interest_Rate_Data"]
df_Beta_Output = frames_dict["tbl_Beta_Output"]
'''

