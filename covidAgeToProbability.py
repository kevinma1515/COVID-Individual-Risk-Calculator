# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 17:02:45 2021

@author: kevin
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from CovidAGE import covidAge

def ageToProbAnalysis():
    df = pd.read_csv('covid-age-calculator.csv')
    df = df[2:]
    x = df['covid_age'].to_numpy()
    y = df['Point_estimate'].to_numpy()
    
    print(curve_fit(lambda t,a,b: a*np.exp(b*t),  x,  y,p0=[21,0.04]))
    plt.plot(x,y,'r')
    ts = np.arange(20,85,1)
    plt.plot(ts, 0.0091882*np.exp(0.10334731*ts),'g')
    plt.xlabel('covid age')
    plt.ylabel('point estimate of fatality ratio per 1000')
    
    # Therefore, this proves that the best fit curve for an exponentail distribution of this
    # curve is y = 0.0091882*exp(0.10334731*x) 
    # where y = point estimate of the conversion from covid age to fatality ratio
    # and x = covid age
    

def getProbabilityFatality(age):
    
    if covidAge(age) >= 85:
        return 0.0091882*np.exp(0.10334731*85)/1000
    else:
        return 0.0091882*np.exp(0.10334731*covidAge(age))/1000
    
def getProbabilityHospitalized(age):
    return
    
def getProbabilityICU(age):
    return