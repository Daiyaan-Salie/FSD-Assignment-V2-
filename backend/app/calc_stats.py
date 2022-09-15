'''
    Author: Daiyaan Salie
    
'''
import numpy as np
import pandas as pd
from app.weights_and_ics import getICsAndWeights
from app.betas_mkt_spec_vols import getBetasMktAndSpecVols
from app.dataframes import df_BA_Beta_Output

def CalcStats(weights,betas,specVols,mktVol):
    
    pfBeta = round(np.matmul(np.transpose(weights),betas),3)

    sysCov = np.matmul(betas,np.transpose(betas))*(mktVol**2)

    pfSysVol = np.transpose(weights)@betas@np.transpose(betas)@weights*(mktVol**2)

    specCov = np.diagflat(specVols)@np.diagflat(specVols)

    pfSpecVol = np.transpose(weights)@(specCov)@weights

    totCov = sysCov + specCov

    pfVol = pfSysVol + pfSpecVol

    d = np.diagflat(np.matrix(np.diag(totCov)))
    
    corrMat = (np.linalg.inv(d)@(sysCov+specCov))@np.linalg.inv(d)

    Output = {"pfBeta" : pfBeta, "sysCov" : sysCov, "pfSysVol" : pfSysVol, "specCov" : specCov, "pfSpecVol" : pfSpecVol, "totCov" : totCov, "pfVol" : pfVol, "corrMat": corrMat}
    
    return (Output)