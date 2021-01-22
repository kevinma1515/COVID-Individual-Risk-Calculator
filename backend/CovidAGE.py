# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 18:44:34 2021

@author: kevin
"""

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
    
    asthma = input("Do you have asthma (please input Y/N)? ").lower()
    if asthma == "y":
        severityAsthma = input("Is your asthma severe? (Please enter Y/N)? ").lower()
        if severityAsthma == "y":
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
            
    respiratoryDisease = input("Do you have any other chronic respiratory diseases? (Y/N) ").lower()
    if respiratoryDisease == "y":
        if age <= 24:
            covidage += 17
        elif 25 <= age <= 30:
            covidage += 16
        elif 31<=age<=35:
            covidage += 15
        elif 36 <= age <= 40:
            covidage += 14
        elif 41 <= age <= 46:
            covidage += 13
        elif 47 <= age <= 51:
            covidage += 12
        elif 52 <= age <= 55:
            covidage += 11
        elif 56 <= age <= 58:
            covidage += 10
        elif 59 <= age <= 61:
            covidage += 9
        elif 62 <= age <= 64:
            covidage += 8
        elif 65 <= age <= 69:
            covidage += 7
        elif age >= 70:
            covidage += 6
    else:
        covidage += 0
    
    hypertension = input("Do you have hypertension? (Y/N) ").lower()
    if hypertension == "y":
        if age <= 26:
            covidage += 12
        elif 27 <= age <= 33:
            covidage += 11
        elif 34 <= age <= 39:
            covidage += 10
        elif 40 <= age <= 44:
            covidage += 9
        elif 45 <= age <= 49:
            covidage += 8
        elif 50 <= age <= 54:
            covidage += 7
        elif 55 <= age <= 57:
            covidage += 6
        elif 58 <= age <= 61:
            covidage += 5
        elif 62 <= age <= 64:
            covidage += 4
        elif 65 <= age <= 67:
            covidage += 3
        elif 68 <= age <= 70:
            covidage += 2
        elif 71 <= age <= 72:
            covidage += 1
        else:
            covidage += 0
    else:
        covidage += 0
    
    heartFailure = input("Any heart failures or other chronic heart diseases? Write ""heart failure or other or none""").lower()
    if heartFailure == "heart failure":
        if age <= 25:
            covidage += 25
        elif 24 <= age <= 30:
            covidage += 24
        elif 31 <= age <= 33:
            covidage += 23
        elif 34 <= age <= 37:
            covidage += 22
        elif 38 <= age <= 40:
            covidage += 21
        elif 41 <= age <= 43:
            covidage += 20
        elif 44 <= age <= 46:
            covidage += 19
        elif 47 <= age <= 49:
            covidage += 18
        elif 50 <= age <= 52:
            covidage += 17
        elif 53 <= age <= 55:
            covidage += 16
        elif 56 <= age <= 57:
            covidage += 15
        elif 58 <= age <= 59:
            covidage += 14
        elif 60 <= age <= 61:
            covidage += 13
        elif 62 <= age <= 63:
            covidage += 12
        elif 64 <= age <= 66:
            covidage += 11
        elif 67 <= age <= 69:
            covidage += 10
        elif 70 <= age <= 72:
            covidage += 9
        elif age >= 73:
            covidage += 8
    elif heartFailure == "other":
        if age <= 25:
            covidage += 20
        elif 26 <= age <= 30:
            covidage += 19
        elif 31 <= age <= 33:
            covidage += 18
        elif 34 <= age <= 37:
            covidage += 17
        elif 38 <= age <= 40:
            covidage += 16
        elif 41 <= age <= 43:
            covidage += 15
        elif 44 <= age <= 46:
            covidage += 14
        elif 47 <= age <= 50:
            covidage += 13
        elif 51 <= age <= 54:
            covidage += 12
        elif 55 <= age <= 56:
            covidage += 11
        elif 57 <= age <= 58:
            covidage += 10
        elif 59 <= age <= 60:
            covidage += 9
        elif 61 <= age <= 62:
            covidage += 8
        elif 63 <= age <= 64:
            covidage += 7
        elif 65 <= age <= 66:
            covidage += 6
        elif 67 <= age <= 69:
            covidage += 5
        elif 70 <= age <= 72:
            covidage += 4
        elif age >= 73:
            covidage += 3
    else:
        covidage += 0
    
    type1Diabetes = input("Do you have type 1 diabetes? (Y/N) ").lower()
    
    if type1Diabetes == "y":
        if age <= 24:
            covidage += 29
        elif 25 <= age <= 32:
            covidage += 28

        elif 33 <= age <= 37:
            covidage += 27
        elif 38 <= age <= 41:
            covidage += 26
        elif 42 <= age <= 45:
            covidage += 25
        elif 46 <= age <= 48:
            covidage += 24
        elif 49 <= age <= 51:
            covidage += 23
        elif 52 <= age <= 53:
            covidage += 22
        elif 54 <= age <= 55:
            covidage += 21
        elif 56 <= age <= 57:
            covidage += 20
        elif 58 <= age <= 59:
            covidage += 19
        elif 60 <= age <= 61:
            covidage += 18
        elif 62 <= age <= 63:
            covidage += 17
        elif 64 <= age <= 65:
            covidage += 16
        elif 66 <= age <= 67:
            covidage += 15
        elif 68 <= age <= 70:
            covidage += 14
        elif 71 <= age <= 72:
            covidage += 13
        elif age >= 73:
            covidage += 12
    else:
        covidage += 0
    
    type2Diabetes = input("Do you have type 2 diabetes? (Y/N) ").lower()
    
    if type2Diabetes == 'y':
        if age <= 24:
            covidage += 22
        elif 25 <= age <= 37:
            covidage += 21
        elif 38 <= age <= 45:
            covidage += 20
        elif 46 <= age <= 48:
            covidage += 19
        elif 49 <= age <= 51:
            covidage += 18
        elif 52 <= age <= 53:
            covidage += 17
        elif 54 <= age <= 56:
            covidage += 16
        elif 57 <= age <= 58:
            covidage += 15
        elif 59 <= age <= 60:
            covidage += 14
        elif 61 <= age <= 62:
            covidage += 13
        elif 63 <= age <= 64:
            covidage += 12
        elif 65 <= age <= 67:
            covidage += 11
        elif 68 <= age <= 69:
            covidage += 10
        elif 70 <= age <= 72:
            covidage += 9
        elif age >= 73:
            covidage += 8
    else:
        covidage += 0
        
    chronicKidneyDisease = input("Do you have chronic kidney disease? (Y/N) ").lower()
    
    if chronicKidneyDisease == 'y':
        GFR3060 = input("Is your estimated GFR 30-60 mL/min?(Y/N) ").lower()
        # note else means that it is lower than 30 mL/min
        if GFR3060 == 'y':
            if age == 20:
                covidage += 42
            elif age == 21:
                covidage += 41
            elif age == 22:
                covidage += 40
            elif age == 23:
                covidage += 39
            elif age == 24:
                covidage += 38
            elif 25 <= age <= 26:
                covidage += 37
            elif age == 27:
                covidage += 36
            elif age == 28:
                covidage += 35
            elif age == 29:
                covidage += 34
            elif age == 30:
                covidage += 33
            elif 31 <= age <= 32:
                covidage += 32
            elif age == 33:
                covidage += 31
            elif age == 34:
                covidage += 30
            elif age == 35:
                covidage += 29
            elif age == 36:
                covidage += 28
            elif age == 37:
                covidage += 27
            elif 38 <= age <= 39:
                covidage += 26
            elif age == 40:
                covidage += 25
            elif age == 41:
                covidage += 24
            elif age == 42:
                covidage += 23
            elif age == 43:
                covidage += 22
            elif age == 44:
                covidage += 21
            elif age == 45:
                covidage += 20
            elif 46 <= age <= 47:
                covidage += 19
            elif 48 <= age <= 49:
                covidage += 18
            elif age == 50:
                covidage += 17
            elif 51 <= age <= 52:
                covidage += 16
            elif age == 53:
                covidage += 15
            elif 54 <= age <= 55:
                covidage += 14
            elif 56 <= age <=57:
                covidage += 13
            elif age == 58:
                covidage += 12
            elif 59 <= age <= 60:
                covidage += 11
            elif age == 61:
                covidage += 10
            elif 62 <= age <= 63:
                covidage += 9
            elif 64 <= age <= 65:
                covidage += 8
            elif 66 <= age <= 67:
                covidage += 7
            elif 68 <= age <= 69:
                covidage += 6
            elif 70 <= age <= 71:
                covidage += 5
            elif 72 <= age <= 73:
                covidage += 4
            elif age >= 74:
                covidage += 3
        else:
            if age == 20:
                covidage += 53
            elif age == 21:
                covidage += 52
            elif age == 22:
                covidage += 51 
            elif 23 <= age <= 24:
                covidage += 50
            elif age == 25:
                covidage += 49
            elif age == 26:
                covidage += 48
            elif age == 27:
                covidage += 47
            elif age == 28:
                covidage += 46
            elif age == 29:
                covidage += 46
            elif age == 30:
                covidage += 45
            elif age == 31:
                covidage += 44
            elif age == 32:
                covidage += 44
            elif age == 33:
                covidage += 43
            elif age == 34:
                covidage += 42
            elif age == 35:
                covidage += 41
            elif age == 36:
                covidage += 40
            elif age == 37:
                covidage += 39
            elif age == 38:
                covidage += 38
            elif age == 39:
                covidage += 37
            elif age == 40:
                covidage += 36
            elif age == 41:
                covidage += 35
            elif age == 42:
                covidage += 35
            elif age == 43:
                covidage += 34
            elif age == 44:
                covidage += 33
            elif age == 45:
                covidage += 33
            elif age == 46:
                covidage += 32
            elif age == 47:
                covidage += 32
            elif age == 48:
                covidage += 31
            elif age == 49:
                covidage += 30
            elif age == 50:
                covidage += 30
            elif age == 51:
                covidage += 29
            elif age == 52:
                covidage += 28
            elif age == 53:
                covidage += 28
            elif age == 54:
                covidage += 27
            elif age == 55:
                covidage += 26
            elif age == 56:
                covidage += 26
            elif age == 57:
                covidage += 25
            elif age == 58:
                covidage += 24
            elif age == 59:
                covidage += 23
            elif age == 60:
                covidage += 23
            elif age == 61:
                covidage += 22
            elif age == 62:
                covidage += 22
            elif age == 63:
                covidage += 21
            elif age == 64:
                covidage += 20
            elif age == 65:
                covidage += 20
            elif age == 66:
                covidage += 19
            elif age == 67:
                covidage += 19
            elif age == 68:
                covidage += 18
            elif age == 69:
                covidage += 18
            elif age == 70:
                covidage += 17
            elif age == 71:
                covidage += 17
            elif age == 72:
                covidage += 16
            elif age == 73:
                covidage += 16
            elif age >= 74:
                covidage += 15
                
        
    else:
        covidage += 0
        
        
    liverDisease = input("Do you have liver disease? (Y/N) ").lower()
    if liverDisease == 'y':
        
        if age == 20:
            covidage += 32
        elif age == 21:
            covidage += 31
        elif age == 22:
            covidage += 31 
        elif 23 <= age <= 24:
            covidage += 30
        elif age == 25:
            covidage += 29
        elif age == 26:
            covidage += 29
        elif age == 27:
            covidage += 28
        elif age == 28:
            covidage += 28
        elif age == 29:
            covidage += 27
        elif age == 30:
            covidage += 27
        elif age == 31:
            covidage += 26
        elif age == 32:
            covidage += 26
        elif age == 33:
            covidage += 25
        elif age == 34:
            covidage += 25
        elif age == 35:
            covidage += 24
        elif age == 36:
            covidage += 24
        elif age == 37:
            covidage += 23
        elif age == 38:
            covidage += 23
        elif age == 39:
            covidage += 22
        elif age == 40:
            covidage += 22
        elif age == 41:
            covidage += 21
        elif age == 42:
            covidage += 21
        elif age == 43:
            covidage += 20
        elif age == 44:
            covidage += 20
        elif age == 45:
            covidage += 19
        elif age == 46:
            covidage += 19
        elif age == 47:
            covidage += 18
        elif age == 48:
            covidage += 17
        elif age == 49:
            covidage += 17
        elif age == 50:
            covidage += 16
        elif age == 51:
            covidage += 15
        elif age == 52:
            covidage += 15
        elif age == 53:
            covidage += 14
        elif age == 54:
            covidage += 14
        elif age == 55:
            covidage += 13
        elif age == 56:
            covidage += 13
        elif age == 57:
            covidage += 12
        elif age == 58:
            covidage += 12
        elif age == 59:
            covidage += 11
        elif age == 60:
            covidage += 11
        elif age == 61:
            covidage += 10
        elif age == 62:
            covidage += 10
        elif age == 63:
            covidage += 9
        elif age == 64:
            covidage +=9
        elif age == 65:
            covidage += 8
        elif age == 66:
            covidage += 8
        elif age == 67:
            covidage += 7
        elif age == 68:
            covidage += 6
        elif age == 69:
            covidage += 6
        elif age == 70:
            covidage += 5
        elif age == 71:
            covidage += 5
        elif age == 72:
            covidage += 4
        elif age == 73:
            covidage += 4
        elif age >= 74:
            covidage += 3
    else:
        covidage += 0
    
        
        
    return covidage
