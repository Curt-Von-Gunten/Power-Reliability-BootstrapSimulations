# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:40:36 2019

@author: cv85
"""

import os
import pandas as pd
from decimal import Decimal, ROUND_HALF_UP
import matplotlib.pyplot as plt
import seaborn as sns

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

####################################################################################################################
#################Getting min and max values of effect size for each effect magnitude for each task##################
####################################################################################################################
#I tried looping over tasks, but couldn't get it to work. Ran into several annoying problems. In particular couldn't assign values to variables that are strings that take value of the current loop as a name.
#taskList = ['Anti_Bet', 'Anti_With', 'Go_Bet', 'Go_With', 'Stroop_Bet', 'Stroop_With', 'Simon_Bet', 'Simon_With', 'Stop_Bet', 'Stop_With']
#minmaxDF = pd.DataFrame(columns = ('Task','Effect_Size','Effect_Magnitude ','Min', 'Max'))
#minmaxDF['Task'] = np.repeat(taskList, 4)
#for task in taskList:
#    minmaxDF['Effect_Size'][minmaxDF['Task'] == task] = Anti_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude', as_index=False).min()[['Effect_Size']]
#    str(task + "_max") = Anti_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').max()
#minmaxList = []
#for task in taskList:
#    minmaxList.append(Anti_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude', as_index=False).min().iloc[:,0].values)

Anti_Bet_min = Anti_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').min()
Anti_Bet_max = Anti_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').max()
Anti_Bet_min = Anti_Bet_min.iloc[:,0].tolist()
Anti_Bet_max = Anti_Bet_max.iloc[:,0].tolist()
Anti_With_min = Anti_With[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').min()
Anti_With_max = Anti_With[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').max()
Anti_With_min = Anti_With_min.iloc[:,0].tolist()
Anti_With_max = Anti_With_max.iloc[:,0].tolist()

Go_Bet_min = Go_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').min()
Go_Bet_max = Go_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').max()
Go_Bet_min = Go_Bet_min.iloc[:,0].tolist()
Go_Bet_max = Go_Bet_max.iloc[:,0].tolist()
Go_With_min = Go_With[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').min()
Go_With_max = Go_With[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').max()
Go_With_min = Go_With_min.iloc[:,0].tolist()
Go_With_max = Go_With_max.iloc[:,0].tolist()

Stroop_Bet_min = Stroop_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').min()
Stroop_Bet_max = Stroop_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').max()
Stroop_Bet_min = Stroop_Bet_min.iloc[:,0].tolist()
Stroop_Bet_max = Stroop_Bet_max.iloc[:,0].tolist()
Stroop_With_min = Stroop_With[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').min()
Stroop_With_max = Stroop_With[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').max()
Stroop_With_min = Stroop_With_min.iloc[:,0].tolist()
Stroop_With_max = Stroop_With_max.iloc[:,0].tolist()

Simon_Bet_min = Simon_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').min()
Simon_Bet_max = Simon_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').max()
Simon_Bet_min = Simon_Bet_min.iloc[:,0].tolist()
Simon_Bet_max = Simon_Bet_max.iloc[:,0].tolist()
Simon_With_min = Simon_With[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').min()
Simon_With_max = Simon_With[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').max()
Simon_With_min = Simon_With_min.iloc[:,0].tolist()
Simon_With_max = Simon_With_max.iloc[:,0].tolist()

Stop_Bet_min = Stop_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').min()
Stop_Bet_max = Stop_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').max()
Stop_Bet_min = Stop_Bet_min.iloc[:,0].tolist()
Stop_Bet_max = Stop_Bet_max.iloc[:,0].tolist()
Stop_With_min = Stop_With[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').min()
Stop_With_max = Stop_With[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').max()
Stop_With_min = Stop_With_min.iloc[:,0].tolist()
Stop_With_max = Stop_With_max.iloc[:,0].tolist()

roundList = [Anti_Bet_min, Anti_Bet_max, Anti_With_min, Anti_With_max, 
             Go_Bet_min, Go_Bet_max, Go_With_min, Go_With_max, 
             Stroop_Bet_min, Stroop_Bet_max, Stroop_With_min, Stroop_With_max, 
             Simon_Bet_min, Simon_Bet_max, Simon_With_min, Simon_With_max, 
             Stop_Bet_min, Stop_Bet_max, Stop_With_min, Stop_With_max]   
for descList in roundList: 
    for i, elem in enumerate(descList):
        descList[i] = Decimal(str(elem)).quantize(Decimal('.11'), rounding=ROUND_HALF_UP)

####################################################################################################################
# =============================================================================
# AntiBet_min = Anti_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').min()
# AntiBet_max = Anti_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').max()
# AntiWith_min = Anti_With[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').min()
# AntiWith_max = Anti_With[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').max()
# 
# GoBet_min = Go_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').min()
# GoBet_max = Go_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').max()
# GoWith_min = Go_With[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').min()
# GoWith_max = Go_With[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').max()
# 
# AntiBet_min = Stroop_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').min()
# AntiBet_max = Stroop_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').max()
# AntiWith_min = Stroop_With[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').min()
# AntiWith_max = Stroop_With[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').max()
# 
# AntiBet_min = Anti_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').min()
# AntiBet_max = Anti_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').max()
# AntiWith_min = Anti_With[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').min()
# AntiWith_max = Anti_With[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').max()
# 
# AntiBet_min = Anti_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').min()
# AntiBet_max = Anti_Bet[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').max()
# AntiWith_min = Anti_With[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').min()
# AntiWith_max = Anti_With[['Effect_Magnitude', 'Effect_Size']].groupby('Effect_Magnitude').max()
# 
# =============================================================================

Anti_Bet.columns = ["Participant Number", "Trial Number", "Effect Magnitude",  "Cohen's d", "Power"]
Anti_With.columns = ["Participant Number", "Trial Number", "Effect Magnitude",  "Cohen's d", "Power"]
Go_Bet.columns = ["Participant Number", "Trial Number", "Effect Magnitude",  "Cohen's d", "Power"]
Go_With.columns = ["Participant Number", "Trial Number", "Effect Magnitude",  "Cohen's d", "Power"]
Stroop_Bet.columns = ["Participant Number", "Trial Number", "Effect Magnitude",  "Cohen's d", "Power"]
Stroop_With.columns = ["Participant Number", "Trial Number", "Effect Magnitude",  "Cohen's d", "Power"]
Simon_Bet.columns = ["Participant Number", "Trial Number", "Effect Magnitude",  "Cohen's d", "Power"]
Simon_With.columns = ["Participant Number", "Trial Number", "Effect Magnitude",  "Cohen's d", "Power"]
Stop_Bet.columns = ["Participant Number", "Trial Number", "Effect Magnitude",  "Cohen's d", "Power"]
Stop_With.columns = ["Participant Number", "Trial Number", "Effect Magnitude",  "Cohen's d", "Power"]

Anti_Bet["Task"] = "antisaccade"
Anti_With["Task"] = "antisaccade"
Go_Bet["Task"] = "go/no-go"
Go_With["Task"] = "go/no-go"
Stroop_Bet["Task"] = "Stroop"
Stroop_With["Task"] = "Stroop"
Simon_Bet["Task"] = "Simon"
Simon_With["Task"] = "Simon"
Stop_Bet["Task"] = "stop signal"
Stop_With["Task"] = "stop signal"

Anti_Bet["Design"] = "Between"
Anti_With["Design"] = "Within"
Go_Bet["Design"] = "Between"
Go_With["Design"] = "Within"
Stroop_Bet["Design"] = "Between"
Stroop_With["Design"] = "Within"
Simon_Bet["Design"] = "Between"
Simon_With["Design"] = "Within"
Stop_Bet["Design"] = "Between"
Stop_With["Design"] = "Within"

#Renaming effect magnitude in order to use different tasks in the same facet grid.
Anti_Bet.loc[Anti_Bet['Effect Magnitude']==0.05, 'Effect Magnitude 2'] = 'One'
Anti_Bet.loc[Anti_Bet['Effect Magnitude']==0.075, 'Effect Magnitude 2'] = 'Two'
Anti_Bet.loc[Anti_Bet['Effect Magnitude']==0.10, 'Effect Magnitude 2'] = 'Three'
Anti_Bet.loc[Anti_Bet['Effect Magnitude']==0.125, 'Effect Magnitude 2'] = 'Four'

Anti_With.loc[Anti_With['Effect Magnitude']==0.05, 'Effect Magnitude 2'] = 'One'
Anti_With.loc[Anti_With['Effect Magnitude']==0.075, 'Effect Magnitude 2'] = 'Two'
Anti_With.loc[Anti_With['Effect Magnitude']==0.10, 'Effect Magnitude 2'] = 'Three'
Anti_With.loc[Anti_With['Effect Magnitude']==0.125, 'Effect Magnitude 2'] = 'Four'

Go_Bet.loc[Go_Bet['Effect Magnitude']==0.050, 'Effect Magnitude 2'] = 'One'
Go_Bet.loc[Go_Bet['Effect Magnitude']==0.075, 'Effect Magnitude 2'] = 'Two'
Go_Bet.loc[Go_Bet['Effect Magnitude']==0.100, 'Effect Magnitude 2'] = 'Three'
Go_Bet.loc[Go_Bet['Effect Magnitude']==0.125, 'Effect Magnitude 2'] = 'Four'

Go_With.loc[Go_With['Effect Magnitude']==0.050, 'Effect Magnitude 2'] = 'One'
Go_With.loc[Go_With['Effect Magnitude']==0.075, 'Effect Magnitude 2'] = 'Two'
Go_With.loc[Go_With['Effect Magnitude']==0.100, 'Effect Magnitude 2'] = 'Three'
Go_With.loc[Go_With['Effect Magnitude']==0.125, 'Effect Magnitude 2'] = 'Four'

Stroop_Bet.loc[Stroop_Bet['Effect Magnitude']==50, 'Effect Magnitude 2'] = 'One'
Stroop_Bet.loc[Stroop_Bet['Effect Magnitude']==75, 'Effect Magnitude 2'] = 'Two'
Stroop_Bet.loc[Stroop_Bet['Effect Magnitude']==100, 'Effect Magnitude 2'] = 'Three'
Stroop_Bet.loc[Stroop_Bet['Effect Magnitude']==125, 'Effect Magnitude 2'] = 'Four'

Stroop_With.loc[Stroop_With['Effect Magnitude']==50, 'Effect Magnitude 2'] = 'One'
Stroop_With.loc[Stroop_With['Effect Magnitude']==75, 'Effect Magnitude 2'] = 'Two'
Stroop_With.loc[Stroop_With['Effect Magnitude']==100, 'Effect Magnitude 2'] = 'Three'
Stroop_With.loc[Stroop_With['Effect Magnitude']==125, 'Effect Magnitude 2'] = 'Four'

Simon_Bet.loc[Simon_Bet['Effect Magnitude']==10, 'Effect Magnitude 2'] = 'One'
Simon_Bet.loc[Simon_Bet['Effect Magnitude']==15, 'Effect Magnitude 2'] = 'Two'
Simon_Bet.loc[Simon_Bet['Effect Magnitude']==20, 'Effect Magnitude 2'] = 'Three'
Simon_Bet.loc[Simon_Bet['Effect Magnitude']==25, 'Effect Magnitude 2'] = 'Four'

Simon_With.loc[Simon_With['Effect Magnitude']==10, 'Effect Magnitude 2'] = 'One'
Simon_With.loc[Simon_With['Effect Magnitude']==15, 'Effect Magnitude 2'] = 'Two'
Simon_With.loc[Simon_With['Effect Magnitude']==20, 'Effect Magnitude 2'] = 'Three'
Simon_With.loc[Simon_With['Effect Magnitude']==25, 'Effect Magnitude 2'] = 'Four'

Stop_Bet.loc[Stop_Bet['Effect Magnitude']==25, 'Effect Magnitude 2'] = 'One'
Stop_Bet.loc[Stop_Bet['Effect Magnitude']==50, 'Effect Magnitude 2'] = 'Two'
Stop_Bet.loc[Stop_Bet['Effect Magnitude']==75, 'Effect Magnitude 2'] = 'Three'
Stop_Bet.loc[Stop_Bet['Effect Magnitude']==100, 'Effect Magnitude 2'] = 'Four'

Stop_With.loc[Stop_With['Effect Magnitude']==25, 'Effect Magnitude 2'] = 'One'
Stop_With.loc[Stop_With['Effect Magnitude']==50, 'Effect Magnitude 2'] = 'Two'
Stop_With.loc[Stop_With['Effect Magnitude']==75, 'Effect Magnitude 2'] = 'Three'
Stop_With.loc[Stop_With['Effect Magnitude']==100, 'Effect Magnitude 2'] = 'Four'
              
All500 = pd.concat([Anti_Bet, Anti_With, Go_Bet, Go_With, Stroop_Bet, Stroop_With, Simon_Bet, Simon_With, Stop_Bet, Stop_With])
AllBet = pd.concat([Anti_Bet, Go_Bet, Stroop_Bet, Simon_Bet, Stop_Bet])
AllWith = pd.concat([Anti_With, Go_With,  Stroop_With, Simon_With,  Stop_With])
AntiAll = pd.concat([Anti_Bet, Anti_With])
GoAll = pd.concat([Go_Bet, Go_With])
StroopAll = pd.concat([Stroop_Bet, Stroop_With])
SimonAll = pd.concat([Simon_Bet, Simon_With])
StopAll = pd.concat([Stop_Bet, Stop_With])


#####################################################################################
#####################################################################################
#####################################################################################
path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Revision/Plotting"
os.chdir(path)       

sns.set(style="whitegrid", font_scale=1.2)

AntiAllGraph = sns.catplot(x="Participant Number", y="Power", hue="Trial Number", kind="point",
style = "Trial Number", col="Effect Magnitude", row = "Design", aspect=.8, margin_titles= True,
data=AntiAll, palette=sns.cubehelix_palette(4, start=.1, rot=-.2, hue=1.5, dark=.25, light=.75))
AntiAllGraph.axes[0,0].set_title("Effect = 5%, d = (" + str(Anti_Bet_min[0]) + " - " + str(Anti_Bet_max[0]) + ")")
AntiAllGraph.axes[0,1].set_title("Effect = 7.5%, d = (" + str(Anti_Bet_min[1]) + " - " + str(Anti_Bet_max[1]) + ")")
AntiAllGraph.axes[0,2].set_title("Effect = 10%, d = (" + str(Anti_Bet_min[2]) + " - " + str(Anti_Bet_max[2]) + ")")
AntiAllGraph.axes[0,3].set_title("Effect = 12.5%, d = (" + str(Anti_Bet_min[3]) + " - " + str(Anti_Bet_max[3]) + ")")
AntiAllGraph.axes[1,0].set_title("Effect = 5%, d = (" + str(Anti_With_min[0]) + " - " + str(Anti_With_max[0]) + ")")
AntiAllGraph.axes[1,1].set_title("Effect = 7.5%, d = (" + str(Anti_With_min[1]) + " - " + str(Anti_With_max[1]) + ")")
AntiAllGraph.axes[1,2].set_title("Effect = 10%, d = (" + str(Anti_With_min[2]) + " - " + str(Anti_With_max[2]) + ")")
AntiAllGraph.axes[1,3].set_title("Effect = 12.5%, d = (" + str(Anti_With_min[3]) + " - " + str(Anti_With_max[3]) + ")")
plt.subplots_adjust(hspace=0.15, wspace=0.1)
plt.subplots_adjust(top=.91)
AntiAllGraph.fig.suptitle('Antisaccade Task')
plt.savefig('Anti_Norm2.pdf')
plt.savefig('Anti_Norm2.tiff', dpi=300)

GoAllGraph = sns.catplot(x="Participant Number", y="Power", hue="Trial Number", kind="point",
style = "Trial Number", col="Effect Magnitude", row = "Design", aspect=.8, margin_titles= True,
data=GoAll, palette=sns.cubehelix_palette(4, start=.1, rot=-.2, hue=1.5, dark=.25, light=.75))
GoAllGraph.axes[0,0].set_title("Effect = 5%, d = (" + str(Go_Bet_min[0]) + " - " + str(Go_Bet_max[0]) + ")")
GoAllGraph.axes[0,1].set_title("Effect = 7.5%, d = (" + str(Go_Bet_min[1]) + " - " + str(Go_Bet_max[1]) + ")")
GoAllGraph.axes[0,2].set_title("Effect = 10%, d = (" + str(Go_Bet_min[2]) + " - " + str(Go_Bet_max[2]) + ")")
GoAllGraph.axes[0,3].set_title("Effect = 12.5%, d = (" + str(Go_Bet_min[3]) + " - " + str(Go_Bet_max[3]) + ")")
GoAllGraph.axes[1,0].set_title("Effect = 5%, d = (" + str(Go_With_min[0]) + " - " + str(Go_With_max[0]) + ")")
GoAllGraph.axes[1,1].set_title("Effect = 7.5%, d = (" + str(Go_With_min[1]) + " - " + str(Go_With_max[1]) + ")")
GoAllGraph.axes[1,2].set_title("Effect = 10%, d = (" + str(Go_With_min[2]) + " - " + str(Go_With_max[2]) + ")")
GoAllGraph.axes[1,3].set_title("Effect = 12.5%, d = (" + str(Go_With_min[3]) + " - " + str(Go_With_max[3]) + ")")
plt.subplots_adjust(hspace=0.15, wspace=0.1)
plt.subplots_adjust(top=.91)
GoAllGraph.fig.suptitle('Go/no-go Task')
plt.savefig('Go_Norm2.pdf')
plt.savefig('Go_Norm2.tiff', dpi=300)

StroopAllGraph = sns.catplot(x="Participant Number", y="Power", hue="Trial Number", kind="point",
style = "Trial Number", col="Effect Magnitude", row = "Design", aspect=.8, margin_titles= True,
data=StroopAll, palette=sns.cubehelix_palette(4, start=.1, rot=-.2, hue=1.5, dark=.25, light=.75))
StroopAllGraph.axes[0,0].set_title("Effect = 50ms, d = (" + str(Stroop_Bet_min[0]) + " - " + str(Stroop_Bet_max[0]) + ")")
StroopAllGraph.axes[0,1].set_title("Effect = 75ms, d = (" + str(Stroop_Bet_min[1]) + " - " + str(Stroop_Bet_max[1]) + ")")
StroopAllGraph.axes[0,2].set_title("Effect = 100ms, d = (" + str(Stroop_Bet_min[2]) + " - " + str(Stroop_Bet_max[2]) + ")")
StroopAllGraph.axes[0,3].set_title("Effect = 125ms, d = (" + str(Stroop_Bet_min[3]) + " - " + str(Stroop_Bet_max[3]) + ")")
StroopAllGraph.axes[1,0].set_title("Effect = 50ms, d = (" + str(Stroop_With_min[0]) + " - " + str(Stroop_With_max[0]) + ")")
StroopAllGraph.axes[1,1].set_title("Effect = 75ms, d = (" + str(Stroop_With_min[1]) + " - " + str(Stroop_With_max[1]) + ")")
StroopAllGraph.axes[1,2].set_title("Effect = 100ms, d = (" + str(Stroop_With_min[2]) + " - " + str(Stroop_With_max[2]) + ")")
StroopAllGraph.axes[1,3].set_title("Effect = 125ms, d = (" + str(Stroop_With_min[3]) + " - " + str(Stroop_With_max[3]) + ")")
plt.subplots_adjust(hspace=0.15, wspace=0.1)
plt.subplots_adjust(top=.91)
StroopAllGraph.fig.suptitle('Stroop Task')
plt.savefig('Stroop_Norm2.pdf')
plt.savefig('Stroop_Norm2.tiff', dpi=300)

SimonAllGraph = sns.catplot(x="Participant Number", y="Power", hue="Trial Number", kind="point",
style = "Trial Number", col="Effect Magnitude", row = "Design", aspect=.8, margin_titles= True,
data=SimonAll, palette=sns.cubehelix_palette(4, start=.1, rot=-.2, hue=1.5, dark=.25, light=.75))
SimonAllGraph.axes[0,0].set_title("Effect = 10ms, d = (" + str(Simon_Bet_min[0]) + " - " + str(Simon_Bet_max[0]) + ")")
SimonAllGraph.axes[0,1].set_title("Effect = 15ms, d = (" + str(Simon_Bet_min[1]) + " - " + str(Simon_Bet_max[1]) + ")")
SimonAllGraph.axes[0,2].set_title("Effect = 20ms, d = (" + str(Simon_Bet_min[2]) + " - " + str(Simon_Bet_max[2]) + ")")
SimonAllGraph.axes[0,3].set_title("Effect = 25ms, d = (" + str(Simon_Bet_min[3]) + " - " + str(Simon_Bet_max[3]) + ")")
SimonAllGraph.axes[1,0].set_title("Effect = 10ms, d = (" + str(Simon_With_min[0]) + " - " + str(Simon_With_max[0]) + ")")
SimonAllGraph.axes[1,1].set_title("Effect = 15ms, d = (" + str(Simon_With_min[1]) + " - " + str(Simon_With_max[1]) + ")")
SimonAllGraph.axes[1,2].set_title("Effect = 20ms, d = (" + str(Simon_With_min[2]) + " - " + str(Simon_With_max[2]) + ")")
SimonAllGraph.axes[1,3].set_title("Effect = 25ms, d = (" + str(Simon_With_min[3]) + " - " + str(Simon_With_max[3]) + ")")
plt.subplots_adjust(hspace=0.15, wspace=0.1)
plt.subplots_adjust(top=.91)
SimonAllGraph.fig.suptitle('Simon Task')
plt.savefig('Simon_Norm2.pdf')
plt.savefig('Simon_Norm2.tiff', dpi=300)

sns.set(style="whitegrid", font_scale=1.2)
StopAllGraph = sns.catplot(x="Participant Number", y="Power", hue="Trial Number", kind="point",
style = "Trial Number", col="Effect Magnitude", row = "Design", aspect=.8, margin_titles= True,
data=StopAll, palette=sns.cubehelix_palette(4, start=.1, rot=-.2, hue=1.5, dark=.25, light=.75))
StopAllGraph.axes[0,0].set_title("Effect = 10ms, d = (" + str(Stop_Bet_min[0]) + " - " + str(Stop_Bet_max[0]) + ")")
StopAllGraph.axes[0,1].set_title("Effect = 15ms, d = (" + str(Stop_Bet_min[1]) + " - " + str(Stop_Bet_max[1]) + ")")
StopAllGraph.axes[0,2].set_title("Effect = 20ms, d = (" + str(Stop_Bet_min[2]) + " - " + str(Stop_Bet_max[2]) + ")")
StopAllGraph.axes[0,3].set_title("Effect = 25ms, d = (" + str(Stop_Bet_min[3]) + " - " + str(Stop_Bet_max[3]) + ")")
StopAllGraph.axes[1,0].set_title("Effect = 10ms, d = (" + str(Stop_With_min[0]) + " - " + str(Stop_With_max[0]) + ")")
StopAllGraph.axes[1,1].set_title("Effect = 15ms, d = (" + str(Stop_With_min[1]) + " - " + str(Stop_With_max[1]) + ")")
StopAllGraph.axes[1,2].set_title("Effect = 20ms, d = (" + str(Stop_With_min[2]) + " - " + str(Stop_With_max[2]) + ")")
StopAllGraph.axes[1,3].set_title("Effect = 25ms, d = (" + str(Stop_With_min[3]) + " - " + str(Stop_With_max[3]) + ")")
plt.subplots_adjust(hspace=0.15, wspace=0.1)
plt.subplots_adjust(top=.91)
StopAllGraph.fig.suptitle('Stop-signal Task')
plt.savefig('Stop_Norm2.pdf')
plt.savefig('Stop_Norm2.tiff', dpi=300)