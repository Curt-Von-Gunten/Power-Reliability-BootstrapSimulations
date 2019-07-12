# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:41:41 2019

@author: cv85
"""

import os
import pandas as pd
import numpy as np
from scipy import stats
from decimal import Decimal, ROUND_HALF_UP
path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Anti"
os.chdir(path)      
Anti_Bet = pd.read_csv('Anti_Bet_500_v1.txt', sep="\t")
Anti_With = pd.read_csv('Anti_With_500_v1.txt', sep="\t")

path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Go"
os.chdir(path)       
Go_Bet = pd.read_csv('Go_Bet_500_v1.txt', sep="\t")
Go_With = pd.read_csv('Go_With_500_v1.txt', sep="\t")

path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Stroop/Revision"
os.chdir(path)       
Stroop_Bet = pd.read_csv('Stroop_Ready_Revision_between_501.txt', sep="\t")
Stroop_With = pd.read_csv('Stroop_Ready_Revision_within_501.txt', sep="\t")

path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Simon/Revision"
os.chdir(path)       
Simon_Bet = pd.read_csv('Simon_Ready_Revision_between_501.txt', sep="\t")
Simon_With = pd.read_csv('Simon_Ready_Revision_within_501.txt', sep="\t")

path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Stop/Revision"
os.chdir(path)       
Stop_Bet = pd.read_csv('Stop_Ready_Revision_between_501_v2.txt', sep="\t")
Stop_With = pd.read_csv('Stop_Ready_Revision_within_501_v2.txt', sep="\t")

##############################################################################
##############################################################################
##############################################################################
taskList = [Anti_Bet,Anti_With,
            Go_Bet,Go_With,
            Stroop_Bet,Stroop_With,
            Simon_Bet,Simon_With,
            Stop_Bet,Stop_With]
IVList = ['Numb_of_Subs','Numb_of_Trials','Effect_Magnitude']
DVList = ['Power','Effect_Size']

tempList = []
for task in taskList:
    for dv in DVList:
        for iv in IVList:
            tempList.append(stats.spearmanr(task[iv],task[dv])[0])
tempList = ['%.2f' % elem for elem in tempList]
#tempList_round = [Decimal(str(elem)).quantize(Decimal('.01'), rounding=ROUND_HALF_UP) for elem in tempList]
tempList2 = np.reshape(tempList,(10,6))
            
#Effect size and power.
IVList2 = ['Effect_Size']
DVList2 = ['Power']
tempList = []
for task in taskList:
    for dv in DVList2:
        for iv in IVList2:
            tempList.append(stats.spearmanr(task[iv],task[dv])[0])
tempList = ['%.2f' % elem for elem in tempList]

#Looking within ranges of effect size.
Anti_Bet[(Anti_Bet['Effect_Size'] <= .35)]['Power'].max()
Go_Bet[(Go_Bet['Effect_Size'] <= .35)]['Power'].max()
Stroop_Bet[(Stroop_Bet['Effect_Size'] <= .35)]['Power'].max()
Simon_Bet[(Simon_Bet['Effect_Size'] <= .35)]['Power'].max()
Stop_Bet[(Stop_Bet['Effect_Size'] <= .35)]['Power'].max()
Anti_Bet[(Anti_Bet['Effect_Size'] <= .35)]['Power'].min()
Go_Bet[(Go_Bet['Effect_Size'] <= .35)]['Power'].min()
Stroop_Bet[(Stroop_Bet['Effect_Size'] <= .35)]['Power'].min()
Simon_Bet[(Simon_Bet['Effect_Size'] <= .35)]['Power'].min()
Stop_Bet[(Stop_Bet['Effect_Size'] <= .35)]['Power'].min()

Anti_Bet[(Anti_Bet['Effect_Size'] >= .20) & (Anti_Bet['Effect_Size'] <= .35) & (Anti_Bet['Numb_of_Subs'] <= 150)]['Power'].max()
Go_Bet[(Anti_Bet['Effect_Size'] >= .20) & (Go_Bet['Effect_Size'] <= .35) & (Go_Bet['Numb_of_Subs'] <= 150)]['Power'].max()
Stroop_Bet[(Anti_Bet['Effect_Size'] >= .20) & (Stroop_Bet['Effect_Size'] <= .35) & (Stroop_Bet['Numb_of_Subs'] <= 150)]['Power'].max()
Simon_Bet[(Anti_Bet['Effect_Size'] >= .20) & (Simon_Bet['Effect_Size'] <= .35) & (Simon_Bet['Numb_of_Subs'] <= 150)]['Power'].max()
Stop_Bet[(Stop_Bet['Effect_Size'] >= .20) & (Stop_Bet['Effect_Size'] <= .35) & (Stop_Bet['Numb_of_Subs'] <= 150)]['Power'].max()

Anti_Bet[(Anti_Bet['Effect_Size'] >= .30) & (Anti_Bet['Effect_Size'] <= .60) & (Anti_Bet['Numb_of_Subs'] <= 50)]['Power'].max()
Go_Bet[(Anti_Bet['Effect_Size'] >= .30) & (Go_Bet['Effect_Size'] <= .60) & (Go_Bet['Numb_of_Subs'] <= 50)]['Power'].max()
Stroop_Bet[(Anti_Bet['Effect_Size'] >= .30) & (Stroop_Bet['Effect_Size'] <= .60) & (Stroop_Bet['Numb_of_Subs'] <= 50)]['Power'].max()
Simon_Bet[(Anti_Bet['Effect_Size'] >= .30) & (Simon_Bet['Effect_Size'] <= .60) & (Simon_Bet['Numb_of_Subs'] <= 50)]['Power'].max()
Stop_Bet[(Stop_Bet['Effect_Size'] >= .30) & (Stop_Bet['Effect_Size'] <= .60) & (Stop_Bet['Numb_of_Subs'] <= 50)]['Power'].max()

Anti_Bet[(Anti_Bet['Effect_Size'] >= .30) & (Anti_Bet['Effect_Size'] <= .60) & (Anti_Bet['Numb_of_Subs'] <= 100)]['Power'].max()
Go_Bet[(Anti_Bet['Effect_Size'] >= .30) & (Go_Bet['Effect_Size'] <= .60) & (Go_Bet['Numb_of_Subs'] <= 100)]['Power'].max()
Stroop_Bet[(Anti_Bet['Effect_Size'] >= .30) & (Stroop_Bet['Effect_Size'] <= .60) & (Stroop_Bet['Numb_of_Subs'] <= 100)]['Power'].max()
Simon_Bet[(Anti_Bet['Effect_Size'] >= .30) & (Simon_Bet['Effect_Size'] <= .60) & (Simon_Bet['Numb_of_Subs'] <= 100)]['Power'].max()
Stop_Bet[(Stop_Bet['Effect_Size'] >= .30) & (Stop_Bet['Effect_Size'] <= .60) & (Stop_Bet['Numb_of_Subs'] <= 100)]['Power'].max()

Anti_Bet[(Anti_Bet['Effect_Size'] >= .30) & (Anti_Bet['Effect_Size'] <= .60) & (Anti_Bet['Numb_of_Subs'] == 150)]['Power'].max()
Go_Bet[(Anti_Bet['Effect_Size'] >= .30) & (Go_Bet['Effect_Size'] <= .60) & (Go_Bet['Numb_of_Subs'] == 150)]['Power'].max()
Stroop_Bet[(Anti_Bet['Effect_Size'] >= .30) & (Stroop_Bet['Effect_Size'] <= .60) & (Stroop_Bet['Numb_of_Subs'] == 150)]['Power'].max()
Simon_Bet[(Anti_Bet['Effect_Size'] >= .30) & (Simon_Bet['Effect_Size'] <= .60) & (Simon_Bet['Numb_of_Subs'] == 150)]['Power'].max()
Stop_Bet[(Stop_Bet['Effect_Size'] >= .30) & (Stop_Bet['Effect_Size'] <= .60) & (Stop_Bet['Numb_of_Subs'] == 150)]['Power'].max()

Anti_Bet[(Anti_Bet['Effect_Size'] >= .30) & (Anti_Bet['Effect_Size'] <= .60) & (Anti_Bet['Numb_of_Subs'] == 150)]['Power'].min()
Go_Bet[(Anti_Bet['Effect_Size'] >= .30) & (Go_Bet['Effect_Size'] <= .60) & (Go_Bet['Numb_of_Subs'] == 150)]['Power'].min()
Stroop_Bet[(Anti_Bet['Effect_Size'] >= .30) & (Stroop_Bet['Effect_Size'] <= .60) & (Stroop_Bet['Numb_of_Subs'] == 150)]['Power'].min()
Simon_Bet[(Anti_Bet['Effect_Size'] >= .30) & (Simon_Bet['Effect_Size'] <= .60) & (Simon_Bet['Numb_of_Subs'] == 150)]['Power'].min()
Stop_Bet[(Stop_Bet['Effect_Size'] >= .30) & (Stop_Bet['Effect_Size'] <= .60) & (Stop_Bet['Numb_of_Subs'] == 150)]['Power'].min()

Anti_Bet[(Anti_Bet['Effect_Size'] >= .60) & (Anti_Bet['Effect_Size'] <= .80) & (Anti_Bet['Numb_of_Subs'] == 100)]['Power'].min()
Go_Bet[(Anti_Bet['Effect_Size'] >= .60) & (Go_Bet['Effect_Size'] <= .80) & (Go_Bet['Numb_of_Subs'] == 100)]['Power'].min()
Stroop_Bet[(Anti_Bet['Effect_Size'] >= .60) & (Stroop_Bet['Effect_Size'] <= .80) & (Stroop_Bet['Numb_of_Subs'] == 100)]['Power'].min()
Simon_Bet[(Anti_Bet['Effect_Size'] >= .60) & (Simon_Bet['Effect_Size'] <= .80) & (Simon_Bet['Numb_of_Subs'] == 100)]['Power'].min()
Stop_Bet[(Stop_Bet['Effect_Size'] >= .60) & (Stop_Bet['Effect_Size'] <= .80) & (Stop_Bet['Numb_of_Subs'] == 100)]['Power'].min()

Anti_Bet[(Anti_Bet['Effect_Size'] >= .80) & (Anti_Bet['Numb_of_Subs'] == 50)]['Power'].min()
Go_Bet[(Anti_Bet['Effect_Size'] >= .80) & (Go_Bet['Numb_of_Subs'] == 50)]['Power'].min()
Stroop_Bet[(Anti_Bet['Effect_Size'] >= .80) & (Stroop_Bet['Numb_of_Subs'] == 50)]['Power'].min()
Simon_Bet[(Anti_Bet['Effect_Size'] >= .80) & (Simon_Bet['Numb_of_Subs'] == 50)]['Power'].min()
Stop_Bet[(Stop_Bet['Effect_Size'] >= .80) & (Stop_Bet['Numb_of_Subs'] == 50)]['Power'].min()

Anti_Bet[(Anti_Bet['Numb_of_Subs'] <= 150)]['Power'].max()
Go_Bet[(Go_Bet['Numb_of_Subs'] <= 150)]['Power'].max()
Stroop_Bet[(Stroop_Bet['Numb_of_Subs'] <= 150)]['Power'].max()
Simon_Bet[(Simon_Bet['Numb_of_Subs'] <= 150)]['Power'].max()
Stop_Bet[(Stop_Bet['Numb_of_Subs'] <= 150)]['Power'].max()
Anti_Bet[(Anti_Bet['Numb_of_Subs'] <= 150)]['Power'].min()
Go_Bet[(Go_Bet['Numb_of_Subs'] <= 150)]['Power'].min()
Stroop_Bet[(Stroop_Bet['Numb_of_Subs'] <= 150)]['Power'].min()
Simon_Bet[(Simon_Bet['Numb_of_Subs'] <= 150)]['Power'].min()
Stop_Bet[(Stop_Bet['Numb_of_Subs'] <= 150)]['Power'].min()

Anti_Bet[(Anti_Bet['Effect_Size'] >= .30) & (Anti_Bet['Effect_Size'] <= .60)]['Power'].max()
Go_Bet[(Go_Bet['Effect_Size'] >= .30) & (Go_Bet['Effect_Size'] <= .60)]['Power'].max()
Stroop_Bet[(Stroop_Bet['Effect_Size'] >= .30) & (Stroop_Bet['Effect_Size'] <= .60)]['Power'].max()
Simon_Bet[(Simon_Bet['Effect_Size'] >= .30) & (Simon_Bet['Effect_Size'] <= .60)]['Power'].max()
Stop_Bet[(Stop_Bet['Effect_Size'] >= .30) & (Stop_Bet['Effect_Size'] <= .60)]['Power'].max()
Anti_Bet[(Anti_Bet['Effect_Size'] >= .30) & (Anti_Bet['Effect_Size'] <= .60)]['Power'].min()
Go_Bet[(Go_Bet['Effect_Size'] >= .30) & (Go_Bet['Effect_Size'] <= .60)]['Power'].min()
Stroop_Bet[(Stroop_Bet['Effect_Size'] >= .30) & (Stroop_Bet['Effect_Size'] <= .60)]['Power'].min()
Simon_Bet[(Simon_Bet['Effect_Size'] >= .30) & (Simon_Bet['Effect_Size'] <= .60)]['Power'].min()
Stop_Bet[(Stop_Bet['Effect_Size'] >= .30) & (Stop_Bet['Effect_Size'] <= .60)]['Power'].min()


Anti_Bet[(Anti_Bet['Numb_of_Subs'] == 150) & (Anti_Bet['Power'] >= .80)]['Effect_Size'].min()
Go_Bet[(Go_Bet['Numb_of_Subs'] == 150) & (Go_Bet['Power'] >= .80)]['Effect_Size'].min()
Stroop_Bet[(Stroop_Bet['Numb_of_Subs'] == 150) & (Stroop_Bet['Power'] >= .80)]['Effect_Size'].min()
Simon_Bet[(Simon_Bet['Numb_of_Subs'] == 150) & (Simon_Bet['Power'] >= .80)]['Effect_Size'].min()
Stop_Bet[(Stop_Bet['Numb_of_Subs'] == 150) & (Stop_Bet['Power'] >= .80)]['Effect_Size'].min()



Anti_Bet[(Anti_Bet['Numb_of_Subs'] == 100) & (Anti_Bet['Power'] >= .80)]['Effect_Size'].min()
Go_Bet[(Go_Bet['Numb_of_Subs'] == 100) & (Go_Bet['Power'] >= .80)]['Effect_Size'].min()
Stroop_Bet[(Stroop_Bet['Numb_of_Subs'] == 100) & (Stroop_Bet['Power'] >= .80)]['Effect_Size'].min()
Simon_Bet[(Simon_Bet['Numb_of_Subs'] == 100) & (Simon_Bet['Power'] >= .80)]['Effect_Size'].min()
Stop_Bet[(Stop_Bet['Numb_of_Subs'] == 100) & (Stop_Bet['Power'] >= .80)]['Effect_Size'].min()

Anti_Bet[(Anti_Bet['Numb_of_Subs'] == 50) & (Anti_Bet['Power'] >= .80)]['Effect_Size'].min()
Go_Bet[(Go_Bet['Numb_of_Subs'] == 50) & (Go_Bet['Power'] >= .80)]['Effect_Size'].min()
Stroop_Bet[(Stroop_Bet['Numb_of_Subs'] == 50) & (Stroop_Bet['Power'] >= .80)]['Effect_Size'].min()
Simon_Bet[(Simon_Bet['Numb_of_Subs'] == 50) & (Simon_Bet['Power'] >= .80)]['Effect_Size'].min()
Stop_Bet[(Stop_Bet['Numb_of_Subs'] == 50) & (Stop_Bet['Power'] >= .80)]['Effect_Size'].min()




Anti_Bet[(Anti_Bet['Numb_of_Trials'] == 200) & (Anti_Bet['Numb_of_Subs'] == 50) & (Anti_Bet['Effect_Size'] <= .55)]['Power'].max()
Anti_Bet[(Anti_Bet['Numb_of_Trials'] == 200) & (Anti_Bet['Numb_of_Subs'] == 50)]['Effect_Size'].max()

#Hold sub num and effect magnitude constant, how much can effect_size deviation by varying trials number.
Anti_Bet[(Anti_Bet['Numb_of_Subs'] == 50) & (Anti_Bet['Effect_Magnitude'] == .05)]['Effect_Size'].max()
Anti_Bet[(Anti_Bet['Numb_of_Subs'] == 50) & (Anti_Bet['Effect_Magnitude'] == .05)]['Effect_Size'].min()
Anti_Bet[(Anti_Bet['Numb_of_Subs'] == 50) & (Anti_Bet['Effect_Magnitude'] == .10)]['Effect_Size'].max()
Anti_Bet[(Anti_Bet['Numb_of_Subs'] == 50) & (Anti_Bet['Effect_Magnitude'] == .10)]['Effect_Size'].min()
Anti_Bet[(Anti_Bet['Numb_of_Subs'] == 50) & (Anti_Bet['Effect_Magnitude'] == .125)]['Effect_Size'].max()
Anti_Bet[(Anti_Bet['Numb_of_Subs'] == 50) & (Anti_Bet['Effect_Magnitude'] == .125)]['Effect_Size'].min()

#Efect sizes for 150 subs and 200 trials.
Anti_Bet[(Anti_Bet['Numb_of_Subs'] == 150) & (Anti_Bet['Numb_of_Trials'] == 200) & (Anti_Bet['Effect_Magnitude'] == .075)]['Effect_Size'].max()
Anti_Bet[(Anti_Bet['Numb_of_Subs'] == 150) & (Anti_Bet['Numb_of_Trials'] == 200) & (Anti_Bet['Effect_Magnitude'] == .05)]['Power'].max()
#########Within####################
Anti_With[(Anti_With['Numb_of_Trials'] == 200)]['Power'].min()
Go_With[(Go_With['Numb_of_Trials'] == 40)]['Power'].min()



Anti_Bet[(Anti_Bet['Effect_Size'] >= .30) & (Anti_Bet['Effect_Size'] <= .60)]

Go_Bet[(Go_Bet['Numb_of_Subs'] == 150) & (Go_Bet['Power'] >= .80)]['Effect_Size'].min()
Stroop_Bet[(Stroop_Bet['Numb_of_Subs'] == 150) & (Stroop_Bet['Power'] >= .80)]['Effect_Size'].min()
Simon_Bet[(Simon_Bet['Numb_of_Subs'] == 150) & (Simon_Bet['Power'] >= .80)]['Effect_Size'].min()
Stop_Bet[(Stop_Bet['Numb_of_Subs'] == 150) & (Stop_Bet['Power'] >= .80)]['Effect_Size'].min()
