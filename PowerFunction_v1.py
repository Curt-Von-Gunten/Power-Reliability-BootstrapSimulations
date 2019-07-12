# -*- coding: utf-8 -*-
"""
Created on Sun May 19 18:38:35 2019

@author: cv85
"""
import os
import pandas as pd
import numpy as np
from scipy import stats
def PowerSimulation(path,dataset,subjectNumber,trialNumber,effectMag,simulationNumber=50,designType='between',differenceScore=False,stopSignal=False):
    os.chdir(path)
    data = pd.read_csv(str(dataset + '.txt'), sep="\t")
    datasubs = list(data.Subject.unique())
    powerResults = pd.DataFrame(columns=['Numb_of_Subs', 'Numb_of_Trials', 'Effect_Magnitude', 'Effect_Size', 'Power'])
    if stopSignal == True and designType == 'between':
        for e in subjectNumber:
            for f in trialNumber:
                for g in effectMag:
                    powercounter = 0
                    d = []
                    for h in range(1,simulationNumber):
                        SubLevDF1 = pd.DataFrame(columns=['SSRT'])
                        SubLevDF2 = pd.DataFrame(columns=['SSRT'])
                        SubList1 = list(np.random.choice(datasubs, int(e/2)))
                        for subject in SubList1:
                            temp = data[data.Subject == subject]
                            tempnotstop = temp[temp['TrialType'] == 'NotStop']
                            tempstop = temp[temp['TrialType'] == 'Stop']
                            TrialListNotStop = list(np.random.choice(list(tempnotstop.Trial), int(f) * 3))
                            TrialListStop = list(np.random.choice(list(tempstop.Trial), int(f)))
                            tempnotstop.set_index("Trial", inplace=True)
                            tempstop.set_index("Trial", inplace=True)
                            tempnotstop = tempnotstop.loc[TrialListNotStop]
                            tempstop = tempstop.loc[TrialListStop]
                            tempnotstop.reset_index(inplace=True)
                            tempstop.reset_index(inplace=True)
                            RTNotStop = float(tempnotstop[["RT"]].mean())
                            SSDStop = float(tempstop[["SSD"]].mean())
                            SSRTList = [[RTNotStop - SSDStop]]
                            tempDF = pd.DataFrame(SSRTList,columns=['SSRT'])
                            SubLevDF1 = SubLevDF1.append(tempDF)
                        SubList2 = list(np.random.choice(datasubs, int(e/2)))
                        for subject in SubList2:
                            temp = data[data.Subject == subject]
                            tempnotstop = temp[temp['TrialType'] == 'NotStop']
                            tempstop = temp[temp['TrialType'] == 'Stop']
                            TrialListNotStop = list(np.random.choice(list(tempnotstop.Trial), int(f) * 3))
                            TrialListStop = list(np.random.choice(list(tempstop.Trial), int(f)))
                            tempnotstop.set_index("Trial", inplace=True)
                            tempstop.set_index("Trial", inplace=True)
                            tempnotstop = tempnotstop.loc[TrialListNotStop]
                            tempstop = tempstop.loc[TrialListStop]
                            tempnotstop.reset_index(inplace=True)
                            tempstop.reset_index(inplace=True)
                            RTNotStop = float(tempnotstop[["RT"]].mean())
                            SSDStop = float(tempstop[["SSD"]].mean())
                            SSRTList = [[RTNotStop - SSDStop]]
                            tempDF = pd.DataFrame(SSRTList,columns=['SSRT'])
                        SubLevDF2 = SubLevDF2.append(tempDF)
                        SubLevDF2['SSRT'] = SubLevDF2['SSRT'].apply(lambda x: x + g)                 
                        SSRT1 = SubLevDF1[["SSRT"]]
                        SSRT2 = SubLevDF2[["SSRT"]]      
                        SSE1 = ((e/2)-1)*(np.var(SSRT1, ddof=1))
                        SSE2 = ((e/2)-1)*(np.var(SSRT2, ddof=1))
                        pooledvar = (SSE1 + SSE2) / ((e/2) + (e/2) -2)
                        pooledSD = np.sqrt(pooledvar)
                        d.append(float(np.mean(SSRT1 - SSRT2)/pooledSD))
                        ttest = stats.ttest_ind(SSRT1, SSRT2, nan_policy='propagate')
                        print(str(h) + "th power test:" + str(e) + "," + str(f) + "," + str(g))
                        if ttest.pvalue < .050:
                            powercounter = powercounter + 1
                    CohenD = abs(np.mean(d))
                    finalpower = powercounter/h        
                    print("I Have The POWER: " + str(e) + "," + str(f) + "," + str(g) + ": " + str(finalpower) + "%")   
                    Experiment = [[e,f,g,CohenD,finalpower]]
                    ExpPower = pd.DataFrame(Experiment,columns=['Numb_of_Subs', 'Numb_of_Trials', 'Effect_Magnitude', 'Effect_Size', 'Power'])
                    powerResults = powerResults.append(ExpPower)
    elif stopSignal == True and designType == 'within':
        for e in subjectNumber:
            for f in trialNumber:
                for g in effectMag:
                    powercounter = 0
                    d = []
                    for h in range(1,simulationNumber):
                        SubLevDF = pd.DataFrame(columns=['SSRT1','SSRT2'])
                        SubList = list(np.random.choice(datasubs, e))
                        for subject in SubList:
                            temp = data[data.Subject == subject]
                            tempnotstop = temp[temp['TrialType'] == 'NotStop']
                            tempstop = temp[temp['TrialType'] == 'Stop']
                            TrialListNotStop1 = list(np.random.choice(list(tempnotstop.Trial), int(f/2) * 3))
                            TrialListNotStop2 = list(np.random.choice(list(tempnotstop.Trial), int(f/2) * 3))
                            TrialListStop1 = list(np.random.choice(list(tempstop.Trial), int(f/2)))
                            TrialListStop2 = list(np.random.choice(list(tempstop.Trial), int(f/2)))
                            tempnotstop.set_index("Trial", inplace=True)
                            tempstop.set_index("Trial", inplace=True)
                            tempnotstop1 = tempnotstop.loc[TrialListNotStop1]
                            tempnotstop2 = tempnotstop.loc[TrialListNotStop2]
                            tempstop1 = tempstop.loc[TrialListStop1]
                            tempstop2 = tempstop.loc[TrialListStop2]
                            tempnotstop1.reset_index(inplace=True)
                            tempnotstop2.reset_index(inplace=True)
                            tempstop1.reset_index(inplace=True)
                            tempstop2.reset_index(inplace=True)
                            RTNotStop1 = float(tempnotstop1[["RT"]].mean())
                            RTNotStop2 = float(tempnotstop2[["RT"]].mean())
                            SSDStop1 = float(tempstop1[["SSD"]].mean())
                            SSDStop2 = float(tempstop2[["SSD"]].mean())
                            SSRTvalue1 = RTNotStop1 - SSDStop1
                            SSRTvalue2 = RTNotStop2 - SSDStop2
                            SSRTvalue2 = SSRTvalue2 + g
                            SSRTPairList = [[SSRTvalue1,SSRTvalue2]]
                            tempDF = pd.DataFrame(SSRTPairList,columns=['SSRT1','SSRT2'])
                        SubLevDF = SubLevDF.append(tempDF)
                        SSRT1 = SubLevDF[["SSRT1"]]
                        SSRT2 = SubLevDF[["SSRT2"]]
                        Diffcond = SSRT1['SSRT1'] - SSRT2['SSRT2']
                        d.append(float(np.mean(Diffcond)/np.std(Diffcond, ddof=1)))
                        ttest = stats.ttest_rel(SSRT1, SSRT2, nan_policy='propagate')
                        print(str(h) + "th power test:" + str(e) + "," + str(f) + "," + str(g))
                        if ttest.pvalue < .050:
                            powercounter = powercounter + 1
                    CohenD = abs(np.mean(d))
                    finalpower = powercounter/h        
                    print("I Have The POWER: " + str(e) + "," + str(f) + "," + str(g) + ": " + str(finalpower) + "%")  
                    Experiment = [[e,f,g,CohenD,finalpower]]
                    ExpPower = pd.DataFrame(Experiment,columns=['Numb_of_Subs', 'Numb_of_Trials', 'Effect_Magnitude', 'Effect_Size', 'Power'])
                    powerResults = powerResults.append(ExpPower)
    elif differenceScore == False and designType == 'between':
        for e in subjectNumber:
            for f in trialNumber:
                for g in effectMag:
                    powercounter = 0
                    d = []
                    for h in range(1,simulationNumber):
                        SubLevDF1 = pd.DataFrame(columns=['Acc'])
                        SubLevDF2 = pd.DataFrame(columns=['Acc'])
                        SubList1 = list(np.random.choice(datasubs, int(e/2)))
                        for subject in SubList1:
                            temp = data[data.Subject == subject]
                            TrialListCong = list(np.random.choice(list(temp.Trial), f))
                            temp.set_index("Trial", inplace=True)
                            temp = temp.loc[TrialListCong]
                            temp.reset_index(inplace=True)
                            Accvalue = [[float(temp[["Acc"]].mean())]]
                            tempDF = pd.DataFrame(Accvalue,columns=['Acc'])
                            SubLevDF1 = SubLevDF1.append(tempDF)  
                        SubList2 = list(np.random.choice(datasubs, int(e/2)))
                        for subject in SubList2:
                            temp = data[data.Subject == subject]
                            TrialListCong = list(np.random.choice(list(temp.Trial), f))
                            temp.set_index("Trial", inplace=True)
                            temp = temp.loc[TrialListCong]
                            temp.reset_index(inplace=True)
                            Accvalue = [[float(temp[["Acc"]].mean())]]
                            tempDF = pd.DataFrame(Accvalue,columns=['Acc'])
                            SubLevDF2 = SubLevDF2.append(tempDF)  
                        SubLevDF2['Acc'] = SubLevDF2['Acc'].apply(lambda x: x + g)                 
                        Acc1 = SubLevDF1[["Acc"]]
                        Acc2 = SubLevDF2[["Acc"]]
                        SSE1 = ((e/2)-1)*(np.var(Acc1, ddof=1))
                        SSE2 = ((e/2)-1)*(np.var(Acc2, ddof=1))
                        pooledvar = (SSE1 + SSE2) / ((e/2) + (e/2) -2)
                        pooledSD = np.sqrt(pooledvar)
                        d.append(float(np.mean(Acc1 - Acc2)/pooledSD))
                        ttest = stats.ttest_ind(Acc1, Acc2, nan_policy='propagate')
                        print(str(h) + "th simulation:" + str(e) + "," + str(f) + "," + str(g) + "," + str(powercounter))
                        if ttest.pvalue < .050:
                            powercounter = powercounter + 1        
                    CohenD = abs(np.mean(d))
                    finalpower = powercounter/h        
                    print("I HAVE THE POWER: " + str(e) + "," + str(f) + "," + str(g) + ": " + str(finalpower) + "%")   
                    Experiment = [[e,f,g,CohenD,finalpower]]
                    ExpPower = pd.DataFrame(Experiment,columns=['Numb_of_Subs', 'Numb_of_Trials', 'Effect_Magnitude', 'Effect_Size', 'Power'])
                    powerResults = powerResults.append(ExpPower)
    elif differenceScore == False and designType == 'within':
        for e in subjectNumber:
            for f in trialNumber:
                for g in effectMag:
                    powercounter = 0
                    d = []
                    for h in range(1,simulationNumber):
                        SubLevDF = pd.DataFrame(columns=['Acc1','Acc2'])
                        SubList = list(np.random.choice(datasubs, e))
                        for subject in SubList:
                            temp = data[data.Subject == subject]
                            TrialList1 = list(np.random.choice(list(temp.Trial), int(f/2)))
                            TrialList2 = list(np.random.choice(list(temp.Trial), int(f/2)))
                            temp.set_index("Trial", inplace=True)
                            temp1 = temp.loc[TrialList1]
                            temp2 = temp.loc[TrialList2]
                            temp.reset_index(inplace=True)
                            Accvalue1 = float(temp1[["Acc"]].mean())
                            Accvalue2 = float(temp2[["Acc"]].mean())
                            Accvalue2 = Accvalue2 + g
                            AccPairList = [[Accvalue1,Accvalue2]]
                            tempDF = pd.DataFrame(AccPairList,columns=['Acc1','Acc2'])
                            SubLevDF = SubLevDF.append(tempDF)
                        Diff1 = SubLevDF[["Acc1"]]
                        Diff2 = SubLevDF[["Acc2"]]
                        Diffcond = Diff1['Acc1'] - Diff2['Acc2']
                        d.append(float(np.mean(Diffcond)/np.std(Diffcond, ddof=1)))
                        ttest = stats.ttest_rel(Diff1, Diff2, nan_policy='propagate')
                        print(str(h) + "th power test:" + str(e) + "," + str(f) + "," + str(g))
                        if ttest.pvalue < .050:
                            powercounter = powercounter + 1
                    CohenD = abs(np.mean(d))
                    finalpower = powercounter/h        
                    print("I Have The POWER: " + str(e) + "," + str(f) + "," + str(g) + ": " + str(finalpower) + "%")  
                    Experiment = [[e,f,g,CohenD,finalpower]]
                    ExpPower = pd.DataFrame(Experiment,columns=['Numb_of_Subs', 'Numb_of_Trials', 'Effect_Magnitude', 'Effect_Size', 'Power'])
            powerResults = powerResults.append(ExpPower)        
    elif differenceScore == True and designType == 'between':
        for e in subjectNumber:
            for f in trialNumber:
                for g in effectMag:
                    powercounter = 0
                    d = []
                    for h in range(1,simulationNumber):
                        SubLevDF1 = pd.DataFrame(columns=['RT'])
                        SubLevDF2 = pd.DataFrame(columns=['RT'])
                        SubList1 = list(np.random.choice(datasubs, int(e/2)))
                        for subject in SubList1:
                            temp = data[data.Subject == subject]
                            tempcong = temp[temp.Condition == 'cong']
                            tempincong = temp[temp.Condition == 'incong']
                            TrialListCong = list(np.random.choice(list(tempcong.Trial), int(f/2)))
                            TrialListIncong = list(np.random.choice(list(tempincong.Trial), int(f/2)))
                            tempcong.set_index("Trial", inplace=True)
                            tempincong.set_index("Trial", inplace=True)
                            tempcong = tempcong.loc[TrialListCong]
                            tempincong = tempincong.loc[TrialListIncong]
                            tempcong.reset_index(inplace=True)
                            tempincong.reset_index(inplace=True)
                            RTvalueCong = float(tempcong[["RT"]].mean())
                            RTvalueIncong = float(tempincong[["RT"]].mean())
                            RTPairList = [[RTvalueCong - RTvalueIncong]]
                            tempDF = pd.DataFrame(RTPairList,columns=['RT'])
                            SubLevDF1 = SubLevDF1.append(tempDF)
                        SubList2 = list(np.random.choice(datasubs, int(e/2)))
                        for subject in SubList2:
                            temp = data[data.Subject == subject]
                            tempcong = temp[temp.Condition == 'cong']
                            tempincong = temp[temp.Condition == 'incong']
                            TrialListCong = list(np.random.choice(list(tempcong.Trial), int(f/2)))
                            TrialListIncong = list(np.random.choice(list(tempincong.Trial), int(f/2)))
                            tempcong.set_index("Trial", inplace=True)
                            tempincong.set_index("Trial", inplace=True)
                            tempcong = tempcong.loc[TrialListCong]
                            tempincong = tempincong.loc[TrialListIncong]
                            tempcong.reset_index(inplace=True)
                            tempincong.reset_index(inplace=True)
                            RTvalueCong = float(tempcong[["RT"]].mean())
                            RTvalueIncong = float(tempincong[["RT"]].mean())
                            RTPairList = [[RTvalueCong - RTvalueIncong]]
                            tempDF = pd.DataFrame(RTPairList,columns=['RT'])
                            SubLevDF2 = SubLevDF2.append(tempDF)
                        SubLevDF2['RT'] = SubLevDF2['RT'].apply(lambda x: x + g)                 
                        RT1 = SubLevDF1[["RT"]]
                        RT2 = SubLevDF2[["RT"]]      
                        SSE1 = ((e/2)-1)*(np.var(RT1, ddof=1))
                        SSE2 = ((e/2)-1)*(np.var(RT2, ddof=1))
                        pooledvar = (SSE1 + SSE2) / ((e/2) + (e/2) -2)
                        pooledSD = np.sqrt(pooledvar)
                        d.append(float(np.mean(RT1 - RT2)/pooledSD))
                        ttest = stats.ttest_ind(RT1, RT2, nan_policy='propagate')
                        print(str(h) + "th power test:" + str(e) + "," + str(f) + "," + str(g))
                        if ttest.pvalue < .050:
                            powercounter = powercounter + 1
                    CohenD = abs(np.mean(d))
                    finalpower = powercounter/h        
                    print("I Have The POWER: " + str(e) + "," + str(f) + "," + str(g) + ": " + str(finalpower) + "%")   
                    Experiment = [[e,f,g,CohenD,finalpower]]
                    ExpPower = pd.DataFrame(Experiment,columns=['Numb_of_Subs', 'Numb_of_Trials', 'Effect_Magnitude', 'Effect_Size', 'Power'])
                    powerResults = powerResults.append(ExpPower)                     
    elif differenceScore == True and designType == 'within':
        for e in subjectNumber:
            for f in trialNumber:
                for g in effectMag:
                    powercounter = 0
                    d = []
                    for h in range(1,simulationNumber):
                        SubLevDF = pd.DataFrame(columns=['Diff1','Diff2'])
                        SubList = list(np.random.choice(datasubs, e))
                        for subject in SubList:
                            temp = data[data.Subject == subject]
                            tempcong = temp[temp.Condition == 'cong']
                            tempincong = temp[temp.Condition == 'incong']
                            TrialListCong1 = list(np.random.choice(list(tempcong.Trial), int(f/4)))
                            TrialListCong2 = list(np.random.choice(list(tempcong.Trial), int(f/4)))
                            TrialListIncong1 = list(np.random.choice(list(tempincong.Trial), int(f/4)))
                            TrialListIncong2 = list(np.random.choice(list(tempincong.Trial), int(f/4)))
                            tempcong.set_index("Trial", inplace=True)
                            tempincong.set_index("Trial", inplace=True)
                            tempcong1 = tempcong.loc[TrialListCong1]
                            tempcong2 = tempcong.loc[TrialListCong2]
                            tempincong1 = tempincong.loc[TrialListIncong1]
                            tempincong2 = tempincong.loc[TrialListIncong2]
                            tempcong1.reset_index(inplace=True)
                            tempcong2.reset_index(inplace=True)
                            tempincong1.reset_index(inplace=True)
                            tempincong2.reset_index(inplace=True)
                            RTvalueCong1 = float(tempcong1[["RT"]].mean())
                            RTvalueCong2 = float(tempcong2[["RT"]].mean())
                            RTvalueIncong1 = float(tempincong1[["RT"]].mean())
                            RTvalueIncong2 = float(tempincong2[["RT"]].mean())
                            RTvalue1 = RTvalueCong1 - RTvalueIncong1
                            RTvalue2 = RTvalueCong2 - RTvalueIncong2
                            RTvalue2 = RTvalue2 + g
                            RTPairList = [[RTvalue1,RTvalue2]]
                            tempDF = pd.DataFrame(RTPairList,columns=['Diff1','Diff2'])
                            SubLevDF = SubLevDF.append(tempDF)
                        Diff1 = SubLevDF[["Diff1"]]
                        Diff2 = SubLevDF[["Diff2"]]
                        Diffcond = Diff1['Diff1'] - Diff2['Diff2']
                        d.append(float(np.mean(Diffcond)/np.std(Diffcond, ddof=1)))
                        ttest = stats.ttest_rel(Diff1, Diff2, nan_policy='propagate')
                        print(str(h) + "th power test:" + str(e) + "," + str(f) + "," + str(g))
                        if ttest.pvalue < .050:
                            powercounter = powercounter + 1
                    CohenD = abs(np.mean(d))
                    finalpower = powercounter/h        
                    print("I Have The POWER: " + str(e) + "," + str(f) + "," + str(g) + ": " + str(finalpower) + "%")  
                    Experiment = [[e,f,g,CohenD,finalpower]]
                    ExpPower = pd.DataFrame(Experiment,columns=['Numb_of_Subs', 'Numb_of_Trials', 'Effect_Magnitude', 'Effect_Size', 'Power'])
                    powerResults = powerResults.append(ExpPower)
    powerResults.to_csv(str(dataset + "_" + designType + "_" + str(simulationNumber) + ".txt"), sep="\t", index=False) 
    return powerResults 
	
