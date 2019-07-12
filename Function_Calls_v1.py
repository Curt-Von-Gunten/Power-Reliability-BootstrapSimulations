# -*- coding: utf-8 -*-
"""
Created on Mon May 20 14:42:07 2019

@author: cv85
"""
import os
path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Revision/Power"
os.chdir(path)
import PowerFunction_v1 as pf
from importlib import reload
reload(pf)
#Template:
#def PowerSimulation(path,dataset,subjectNumber,trialNumber,effectMag,simulationNumber=50,designType='between',differenceScore=False,stopSignal=False):

###Anti###
###Between, diff=False###
path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Anti/Revision"
dataset = "Anti_Ready_Revision"
subjectNumber = [20,35,50,100,150]
trialNumber = [26,50,100,200]
effectMag = [.05,.075,.10,.125]
simulationNumber = 501 
designType = 'between' 
differenceScore = False 
Result1 = pf.PowerSimulation(path,dataset,subjectNumber,trialNumber,effectMag,simulationNumber,designType,differenceScore)
###Anti###
###Within, diff=False###
path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Anti/Revision"
dataset = "Anti_Ready_Revision" 
subjectNumber = [20,35,50,100,150]
trialNumber = [26,50,100,200]
effectMag = [.05,.075,.10,.125]
simulationNumber = 501 
designType = 'within' 
differenceScore = False 
Result2 = pf.PowerSimulation(path,dataset,subjectNumber,trialNumber,effectMag,simulationNumber,designType,differenceScore)


###Go###
###Between, diff=False###
path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Go/Revision"
dataset = "Go_Ready_Revision"
subjectNumber = [20,35,50,100,150]
trialNumber = [6,10,20,40]
effectMag = [.05,.075,.10,.125]
simulationNumber = 501 
designType = 'between' 
differenceScore = False 
Result1 = pf.PowerSimulation(path,dataset,subjectNumber,trialNumber,effectMag,simulationNumber,designType,differenceScore)
###Go###
###Within, diff=False###
path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Go/Revision"
dataset = "Go_Ready_Revision" 
subjectNumber = [20,35,50,100,150]
trialNumber = [6,10,20,40]
effectMag = [.05,.075,.10,.125]
simulationNumber = 501 
designType = 'within' 
differenceScore = False 
Result2 = pf.PowerSimulation(path,dataset,subjectNumber,trialNumber,effectMag,simulationNumber,designType,differenceScore)


###Stroop
###Between, diff=True###
path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Stroop/Revision"
dataset = "Stroop_Ready_Revision" 
subjectNumber = [20,35,50,100,150]
trialNumber = [28,52,104,208]
effectMag = [50,75,100,125]
simulationNumber = 501 
designType = 'between' 
differenceScore = True 
Result3 = pf.PowerSimulation(path,dataset,subjectNumber,trialNumber,effectMag,simulationNumber,designType,differenceScore)
###Stroop
###Within, diff=True###
path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Stroop/Revision"
dataset = "Stroop_Ready_Revision" 
subjectNumber = [20,35,50,100,150]
trialNumber = [28,52,104,208]
effectMag = [50,75,100,125]
simulationNumber = 501 
designType = 'within'
differenceScore = True  
Result4 = pf.PowerSimulation(path,dataset,subjectNumber,trialNumber,effectMag,simulationNumber,designType,differenceScore)


###Simon
###Between, diff=True###
path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Simon/Revision"
dataset = "Simon_Ready_Revision" 
subjectNumber = [20,35,50,100,150]
trialNumber = [28,52,104,208]
effectMag = [10,15,20,25]
simulationNumber = 501
designType = 'between' 
differenceScore = True 
Result3 = pf.PowerSimulation(path,dataset,subjectNumber,trialNumber,effectMag,simulationNumber,designType='between',differenceScore=True)
###Simon
###Within, diff=True###
path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Simon/Revision"
dataset = "Simon_Ready_Revision" 
subjectNumber = [20,35,50,100,150]
trialNumber = [28,52,104,208]
effectMag = [10,15,20,25]
simulationNumber = 501 
designType = 'within'
differenceScore = True 
Result4 = pf.PowerSimulation(path,dataset,subjectNumber,trialNumber,effectMag,simulationNumber,designType,differenceScore)


###Between, stopSignal=True###
path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Stop/Revision"
dataset = "Stop_Ready_Revision" 
subjectNumber = [20,35,50,100,150]
trialNumber = [6,10,20,40]
effectMag = [25,50,75,100]
designType = 'between'
differenceScore = False 
stopSignal = True 
simulationNumber = 501 
Result5 = pf.PowerSimulation(path,dataset,subjectNumber,trialNumber,effectMag,simulationNumber,designType,stopSignal=True)

###Within, stopSignal=True###
path = "S:/IRB/Wu/VonGunten_2018/Simulation Project_10-32/Data_Code_Output/Stop/Revision"
dataset = "Stop_Ready_Revision" 
subjectNumber = [20,35,50,100,150]
trialNumber = [6,10,20,40]
effectMag = [25,50,75,100]
designType = 'within' 
differenceScore = False 
stopSignal = True 
simulationNumber = 501 
Result6 = pf.PowerSimulation(path,dataset,subjectNumber,trialNumber,effectMag,simulationNumber,designType,stopSignal=True)