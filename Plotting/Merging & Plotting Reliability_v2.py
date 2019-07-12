
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 16:47:14 2018

@author: cv85
"""
import os
import pandas as pd
import numpy as np
path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Anti/Revision"
os.chdir(path)      
Anti = pd.read_csv('Anti_rel_seqonly.txt', sep="\t")

path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Go/Revision"
os.chdir(path)      
Go = pd.read_csv('Go_rel_seqonly.txt', sep="\t")

path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Stroop/Revision"
os.chdir(path)      
Stroop = pd.read_csv('Stroop_Rel_Seq_seqonly.txt', sep="\t")

path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Simon/Revision"
os.chdir(path)      
Simon = pd.read_csv('Simon_Rel_Seq_seqonly.txt', sep="\t")

path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Stop/Revision"
os.chdir(path)      
Stop = pd.read_csv('Stop_Rel_Seq_seqonly.txt', sep="\t")


Anti.columns = ["Participant Number", "Trial Number", "Reliability"]
Go.columns = ["Participant Number", "Trial Number", "Reliability"]
Stroop.columns = ["Participant Number", "Trial Number", "Reliability"]
Simon.columns = ["Participant Number", "Trial Number", "Reliability"]
Stop.columns = ["Participant Number", "Trial Number", "Reliability"]

Anti["Task"] = "antisaccade"
Go["Task"] = "go/no-go"
Stroop["Task"] = "Stroop"
Simon["Task"] = "Simon"
Stop["Task"] = "stop signal"
       
AllTasks = pd.concat([Anti, Go, Stroop, Simon, Stop])
AllTasks['cardTrialNumber'] = np.tile([0,1,2,3,4],5*5)
AllTasks['cardSublNumber'] = np.tile(np.repeat([0,1,2,3,4],5),5)

path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Revision/Plotting"
os.chdir(path) 
AllTasks.to_csv("AllTasks_seqonly.txt", sep="\t", index=False)
######################################################################################
######################################################################################
######################################################################################
path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Revision/Plotting"
os.chdir(path)   
AllTasks = pd.read_csv('AllTasks_seqonly.txt', sep="\t")

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", font_scale=1.2)
paletteChoice = sns.cubehelix_palette(5, start=0, rot=-.4, hue=1, dark=.2, light=.8)

#Anti.
Anti_Graph = sns.catplot(x="Trial Number", y="Reliability", hue="Participant Number", kind="point",
col="Task", aspect=.8, data=Anti, palette=paletteChoice, legend=False)
plt.ylim(0, 1)
plt.title("Antisaccade")
plt.xlabel("Number of antisaccade trials")
plt.ylabel("Cronbach's alpha")
plt.legend(loc='best', title='Participants')
plt.tight_layout()
plt.savefig('Anti_Rel.tiff', dpi=300)

#Go.
Go_Graph = sns.catplot(x="Trial Number", y="Reliability", hue="Participant Number", kind="point",
col="Task", aspect=.8, data=Go, palette=paletteChoice, legend=False)
plt.ylim(0, 1)
plt.title("Go/no-go")
plt.xlabel("Number of go trials")
plt.ylabel("Cronbach's alpha")
plt.legend(loc='lower right', title='Participants')
plt.tight_layout()
plt.savefig('Go_Rel.tiff', dpi=300)

#Stroop.
Stroop_Graph = sns.catplot(x="Trial Number", y="Reliability", hue="Participant Number", kind="point",
col="Task", aspect=.8, data=Stroop, palette=paletteChoice, legend=False)
plt.ylim(0, 1)
plt.title("Stroop")
plt.xlabel("Number of trials per trial-type")
plt.ylabel("Split-half")
plt.legend(loc='best', title='Participants')
plt.tight_layout()
plt.savefig('Stroop_Rel.tiff', dpi=300)

#Simon.
Simon_Graph = sns.catplot(x="Trial Number", y="Reliability", hue="Participant Number", kind="point",
col="Task", aspect=.8, data=Simon, palette=paletteChoice, legend=False)
plt.ylim(0, 1)
plt.title("Simon")
plt.xlabel("Number of trials per trial-type")
plt.ylabel("Split-half")
plt.legend(loc='upper left', title='Participants')
plt.tight_layout()
plt.savefig('Simon_Rel.tiff', dpi=300)

#Stop.
Stop_Graph = sns.catplot(x="Trial Number", y="Reliability", hue="Participant Number", kind="point",
col="Task", aspect=.8, data=Stop, palette=paletteChoice, legend=False)
plt.ylim(0, 1)
plt.title("Stop-signal")
plt.xlabel("Number of stop trials")
plt.ylabel("Split-half")
plt.legend(loc='lower right', title='Participants')
plt.tight_layout()
plt.savefig('Stop_Rel.tiff', dpi=300)

