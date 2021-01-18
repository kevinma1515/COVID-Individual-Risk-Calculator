"""
Created on Thu Jan 14 17:02:45 2021

@author: kevin
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from CovidAGE import covidAge
from ProbabilityOfCOVID import totalSusceptibility

def ageToProbAnalysis():
    # Data analysis of the covid age to prob(ICU) + prob(Hospitalization) + prob(fatality)
    df = pd.read_csv('covid-age-calculator.csv')
    df = df[2:]
    x = df['covid_age'].to_numpy()
    y = df['Point_estimate'].to_numpy()
    
    print(curve_fit(lambda t,a,b: a*np.exp(b*t),  x,  y,p0=[21,0.04]))
    plt.plot(x,y,'r')
    ts = np.arange(20,85,1)
    plt.plot(ts, 0.0091882*np.exp(0.10334731*ts),'g')
    plt.plot(ts,0.0091882*1.3*np.exp(0.10334731*ts), 'r')
    plt.plot(ts,0.0091882*1.3*4*np.exp(0.10334731*ts)+10, 'r')
    plt.xlabel('covid age')
    plt.ylabel('point estimate of fatality ratio per 1000')
    
    # Therefore, this proves that the best fit curve for an exponentail distribution of this
    # curve is y = 0.0091882*exp(0.10334731*x) 
    # where y = point estimate of the conversion from covid age to fatality ratio
    # and x = covid age
    

def conversionToRisk(age):
    
    covidAges = covidAge(age)
    if covidAges >= 85:
        probDeath = 0.0091882*np.exp(0.10334731*85)/1000
    else:
        probDeath = 0.0091882*np.exp(0.10334731*covidAges)/1000

    if covidAges >= 85:
        probICU = 0.0091882*1.3*np.exp(0.10334731*85)/1000
    else:
        probICU = 0.0091882*1.3*np.exp(0.10334731*covidAges)/1000

    if covidAges >= 85:
        probHosp = (0.0091882*1.3*4*np.exp(0.10334731*85)+10)/1000
    elif covidAges <= 18:
        probHosp = 1/1000
    else:
        probHosp = (0.0091882*1.2*5.5*np.exp(0.10334731*covidAges)+10)/1000
    print('this is your prob death', probDeath)
    print('this is your prob hosp', probHosp)
    print("This is your prob ICU", probICU)
    
    riskScore = totalSusceptibility()*(probDeath + probHosp + probICU)/0.0000015
    
    return riskScore
