# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 18:44:34 2021

@author: kevin
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def covidAge(age):
    # need a real age inputted for it to be valid
    # all data gathered from covid-Age calculator
    
    covidage = 0
    covidage += age
    gender = input("Are you male or female? ").lower()
    if gender == "female":
        covidage = covidage - 5
    else:
        covidage += 0
    # ethnicity factor
    race = input("Are you White, Asian, Black, Hispanic, or other non-White? ").lower()
    
    if race == "white":
        covidage += 0
    elif race == "asian":
        covidage += 5
    elif race == "black":
        covidage += 7
    elif race == "hispanic":
        covidage += 6
    else:
        covidage += 4
        
    # account for BMI
    
    bmi = int(input("What is your Body Mass Index (round down please)? "))
    
    if bmi < 30:
        covidage += 0
    elif 30 <= bmi < 35:
        if age <= 24:
            covidage += 7
        elif 25 <= age <= 37:
            covidage += 6
        elif 38 <= age <= 46:
            covidage += 5
        elif 47 <= age <= 52:
            covidage += 4
        elif 53 <= age <= 60:
            covidage += 3
        elif 61 <= age <= 70:
            covidage += 2
        else:
            covidage += 1
    elif 35 <= bmi < 40:
        if age <= 22:
            covidage += 19
        elif 23 <= age <= 26:
            covidage += 18
        elif 27 <= age <= 30:
            covidage += 17
        elif 31 <= age <= 34:
            covidage += 16
        elif 35 <= age <= 39:
            covidage += 15
        elif 40 <= age <= 43:
            covidage += 14
        elif 44 <= age <= 47:
            covidage += 13
        elif 48<= age <= 50:
            covidage += 12
        elif 51<=age<=53:
            covidage+= 11
        elif 54 <= age <= 57:
            covidage += 10
        elif 58 <= age <= 60:
            covidage += 9
        elif 61 <= age <= 63:
            covidage += 8
        elif 64 <= age <= 66:
            covidage += 7
        elif 67 <= age <= 68:
            covidage += 6
        elif 69 <= age <= 71:
            covidage += 5
        elif age == 72 or age == 73:
            covidage+= 4
        else:
            covidage += 3
        
    else:
        if age <= 21:
            covidage += 25
        elif 22 <= age <= 24:
            covidage += 24
        elif 25 <= age <= 27:
            covidage += 23
        elif 28 <= age <= 30:
            covidage += 22
        elif 31 <= age <= 33:
            covidage += 21
        elif 34 <= age <= 35:
            covidage += 20
        elif 36 <= age <= 38:
            covidage += 19
        elif 39 <= age <= 40:
            covidage += 18
        elif 41 <= age <= 43:
            covidage += 17
        elif 44 <= age <= 45:
            covidage += 16
        elif 47 <= age <= 48:
            covidage += 15
        elif 49 <= age <= 51:
            covidage += 14
        elif 52 <= age <= 53:
            covidage += 13
        elif 54 <= age <= 56:
            covidage += 12
        elif 57 <= age <= 59:
            covidage += 11
        elif 60 <= age <= 62:
            covidage += 10
        elif 63 <= age <= 65:
            covidage += 9
        elif 66 <= age <= 67:
            covidage += 8
        elif 68 <= age <= 70:
            covidage += 7
        elif 71 <= age<= 72:
            covidage += 6
        else:
            covidage += 5
            
    # account for asthma as a symptom
    
    asthma = input("Do you have asthma (please input Y/N)? ")
    if asthma == "Y":
        severityAsthma = input("Is your asthma severe? (Please enter Y/N)? ")
        if severityAsthma == "Y":
            if age <= 25:
                covidage += 15
            elif 26 <= age <= 32:
                covidage += 14
            elif 33 <= age <= 37:
                covidage += 13
            elif 38 <= age <= 42:
                covidage += 12
            elif 43 <= age <= 46:
                covidage += 11
            elif 47 <= age <= 49:
                covidage += 10
            elif 50 <= age <= 53:
                covidage += 9
            elif 54 <= age <= 56:
                covidage += 8
            elif 57 <= age <= 59:
                covidage += 7
            elif 60 <= age <= 61:
                covidage += 6
            elif 62 <= age <= 63:
                covidage += 5
            elif 64 <= age <= 67:
                covidage += 4
            elif 68 <= age <= 71:
                covidage += 3
            else:
                covidage += 2
        else:
            covidage += 1


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
    