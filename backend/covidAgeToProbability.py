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
    
    plt.plot(x,y,'y')
    ts = np.arange(20,85,1)
    plt.plot(ts, 0.0091882*np.exp(0.10334731*ts),'g')
    # plt.plot(ts,0.0091882*1.3*np.exp(0.10334731*ts), 'or')
    # plt.plot(ts,0.0091882*1.3*4*np.exp(0.10334731*ts)+10, 'b')
    # plt.yscale("log")
    plt.xlabel('covid age')
    plt.ylabel('point estimate of fatality ratio per 1000')
    
    # Therefore, this proves that the best fit curve for an exponentail distribution of this
    # curve is y = 0.0091882*exp(0.10334731*x) 
    # where y = point estimate of the conversion from covid age to fatality ratio
    # and x = covid age
    
    # from excel sheet, prob of hospitalization is 0.009exp(0.0679*x)
    # note that P(Hosp)*P(ICU|Hosp) = P(ICU) due to P(Hosp|ICU) = 1
    # so P(ICU) = 0.0001*exp(0.0784*x)
    # In literature P(ICU) is lower for elderlies since their chances of surviving in an ICU
    # is lower therefore the P(ICU) for them is lower

def conversionToRisk(covidAges, totalSusceptibility):
    if covidAges >= 85:
        probDeath = 0.0091882*np.exp(0.10334731*85)/1000
    else:
        probDeath = 0.0091882*np.exp(0.10334731*covidAges)/1000

    if covidAges >= 80:
        probICU = 0.0256
    elif 70 >= covidAges >= 79:
        probICU = 0.0332
    else:
        probICU = 0.0001*np.exp(0.0784*covidAges)

    if covidAges >= 85:
        probHosp = 0.0009*np.exp(0.0679*85)
    else:
        probHosp = 0.0009*np.exp(0.0679*covidAges)
    
    print("community risk: ", totalSusceptibility)
    print("probability of death: ", probDeath)
    print("probability of hospitlization: ", probHosp)
    print("probability of icu: ", probICU)
    riskScore = totalSusceptibility*(probDeath + probHosp + probICU)/0.0000015
    print("risk score: ", riskScore)
    if riskScore >= 100:
        riskScore = 100
    return {
        "probDeath" : probDeath,
        "probHosp"  : probHosp,
        "probICU" : probICU,
        "riskScore" : riskScore
    }
