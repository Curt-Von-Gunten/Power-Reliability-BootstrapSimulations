# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 13:58:06 2018

@author: cv85
"""
import os
import pandas as pd
import numpy as np
from decimal import Decimal, ROUND_HALF_UP

path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Stroop/Revision"
os.chdir(path)
############################################################################
Stroop = pd.read_csv('Stroop_Ready_Revision.txt', sep="\t")
SubMax = Stroop[['Subject','Trial','Condition']].groupby(['Subject','Condition'], as_index=False).count()
Trial_Number_Counts = SubMax[['Subject','Condition','Trial']].groupby(['Condition','Trial'], as_index=False).count()
Max = SubMax[['Trial','Condition']].groupby('Condition').max()
Min = SubMax[['Trial','Condition']].groupby('Condition').min()
############################################################################ 
############################################################################
############################################################################ 
TrialBins1 = [1, 25,49,73]
TrialBins2 = [24,48,72,96]
TrialBins3 = [1, 25,49,73]
TrialBins4 = [24,48,72,96]
Means = []
Stds = []
IQR = []
#Perc_75 = []
#Perc_25 = []
Max = []
Min = []
Inter = []
Cond = []
for inter1, inter2, inter3, inter4 in zip(TrialBins1, TrialBins2, TrialBins3, TrialBins4):
    currBinCong = str(inter1) + '-' + str(inter2)
    currBinIncong = str(inter3) + '-' + str(inter4)
    StroopCongBin = Stroop[(Stroop['Trial'] >= inter1) & (Stroop['Trial'] <= inter2)]
    cong = StroopCongBin[StroopCongBin['Condition'] == 'Cong']
    cong_trialsPerBin = cong[['Subject','Trial']].groupby('Subject', as_index=False).count()
    cong_trialsPerBin = cong_trialsPerBin['Subject'][cong_trialsPerBin['Trial'] > 12].tolist()
    cong = cong[cong['Subject'].isin(cong_trialsPerBin)]
    congSubMeans = cong[['Subject','RT',]].groupby(cong['Subject'], as_index=False).mean().sort_values(by='RT', ascending=False)
    congSubMeans.rename({'RT': 'RT_cong'}, axis='columns', inplace=True)
    StroopIncongBin = Stroop[(Stroop['Trial'] >= inter3) & (Stroop['Trial'] <= inter4)]
    incong = StroopIncongBin[StroopIncongBin['Condition'] == 'Incong']    
    incong_trialsPerBin = incong[['Subject','Trial']].groupby('Subject', as_index=False).count()
    incong_trialsPerBin = incong_trialsPerBin['Subject'][incong_trialsPerBin['Trial'] > 12].tolist()
    incong = incong[incong['Subject'].isin(incong_trialsPerBin)]
    incongSubMeans = incong[['Subject','RT',]].groupby(incong['Subject'], as_index=False).mean().sort_values(by='RT', ascending=False)
    incongSubMeans.rename({'RT': 'RT_incong'}, axis='columns', inplace=True)
    bothSubMeans = congSubMeans.merge(incongSubMeans, how='outer') 
    bothSubMeans['RT_diff'] = bothSubMeans['RT_incong'] - bothSubMeans['RT_cong']
    Means.append(bothSubMeans['RT_diff'].mean())
    Stds.append(bothSubMeans['RT_diff'].std())
    #Perc_75.append(np.nanpercentile(bothSubMeans['RT_diff'],75))
    #Perc_25.append(np.nanpercentile(bothSubMeans['RT_diff'],25))
    IQR.append(np.subtract(*np.nanpercentile(bothSubMeans['RT_diff'], [75, 25])))
    Max.append(bothSubMeans['RT_diff'].max())
    Min.append(bothSubMeans['RT_diff'].min())
    Inter.append(str(currBinCong + "; " + currBinIncong))

roundList = [Means, Stds, IQR, Min, Max]   
for descList in roundList: 
    for i, elem in enumerate(descList):
        descList[i] = Decimal(str(elem)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        
StroopMetrics_dff_bin_1212 = pd.DataFrame({'Trial_Bin': Inter, 'Mean': Means, 'Std': Stds, 'IQR': IQR, 'Min': Min, 'Max': Max})  


#Means = [Decimal(str(elem)).quantize(Decimal('1'), rounding=ROUND_HALF_UP) for elem in Means]        
#Stds = [Decimal(str(elem)).quantize(Decimal('1'), rounding=ROUND_HALF_UP) for elem in Stds]      
#IQR = [Decimal(str(elem)).quantize(Decimal('1'), rounding=ROUND_HALF_UP) for elem in IQR]      
#Min = [Decimal(str(elem)).quantize(Decimal('1'), rounding=ROUND_HALF_UP) for elem in Min]      
#Max = [Decimal(str(elem)).quantize(Decimal('1'), rounding=ROUND_HALF_UP) for elem in Max]      
    
    