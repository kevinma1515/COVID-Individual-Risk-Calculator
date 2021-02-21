# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 18:44:34 2021

@author: kevin
"""




def covidAge(age, gender, race, bmi, asthma, severityAsthma, respiratoryDisease, hypertension, heartFailure, type1Diabetes,
            type2Diabetes, chronicKidneyDisease, liverDisease, chronicNeurlogical,
              organTransplant, rheumatoid, immunoSuppressive, spleenDisease, nonHematologicalCancer, 
             hematologicalCancer, cerebroVascularDisease):
    # need a real age inputted for it to be valid
    # all data gathered from covid-Age calculator
    
    covidage = 0
    covidage += age
    # gender = input("Are you male or female? ").lower()
    if gender == "Female":
        covidage = covidage - 5
    else:
        covidage += 0
    # ethnicity factor
    # race = input("Are you White, Asian, Black, Hispanic, or other non-White? ").lower()
    
    if race == "White":
        covidage += 0
    elif race == "Asian":
        covidage += 5
    elif race == "Black":
        covidage += 7
    elif race == "Hispanic":
        covidage += 6
    else:
        covidage += 4
        
    # account for BMI
    
    # bmi = int(input("What is your Body Mass Index (round down please)? "))
    
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
    
    # asthma = input("Do you have asthma (please input Y/N)? ").lower()
    if asthma == "Yes":
        # severityAsthma = input("Is your asthma severe? (Please enter Y/N)? ").lower()
        if severityAsthma == "Yes":
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
            
    # respiratoryDisease = input("Do you have any other chronic respiratory diseases? (Y/N) ").lower()
    if respiratoryDisease == "Yes":
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
    
    # hypertension = input("Do you have hypertension? (Y/N) ").lower()
    if hypertension == "Yes":
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
    
    # heartFailure = input("Any heart failures or other chronic heart diseases? Write ""heart failure or other or none""").lower()
    if heartFailure == "Heart Failure":
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
    elif heartFailure == "Other":
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
    
    # type1Diabetes = input("Do you have type 1 diabetes? (Y/N) ").lower()
    
    if type1Diabetes == "Yes":
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
    
    # type2Diabetes = input("Do you have type 2 diabetes? (Y/N) ").lower()
    
    if type2Diabetes == 'Yes':
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
        
    #chronicKidneyDisease = input("Do you have chronic kidney disease? (Y/N) ").lower()
    
    if chronicKidneyDisease == 'Estimated GFR 30-60 mL/min':
        # GFR3060 = input("Is your estimated GFR 30-60 mL/min?(Y/N) ").lower()
        # note else means that it is lower than 30 mL/min
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
    elif chronicKidneyDisease == 'Estimated GFR less than 30 mL/min (includes patients on dialysis':
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
    # liverDisease = input("Do you have liver disease? (Y/N) ").lower()
    if liverDisease == 'Yes':
        
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
        
    # chronicNeurlogical= input("Do you have chronic neurlogical disease other than stroke or dementia? (Y/N) ").lower()
    if chronicNeurlogical == 'Yes':

        
        if age == 20:
            covidage += 23
        elif age == 21:
            covidage += 23
        elif age == 22:
            covidage += 22 
        elif 23 <= age <= 24:
            covidage += 22
        elif age == 25:
            covidage += 22
        elif age == 26:
            covidage += 22
        elif age == 27:
            covidage += 22
        elif age == 28:
            covidage += 22
        elif age == 29:
            covidage += 22
        elif age == 30:
            covidage += 22
        elif age == 31:
            covidage += 22
        elif age == 32:
            covidage += 21
        elif age == 33:
            covidage += 21
        elif age == 34:
            covidage += 21
        elif age == 35:
            covidage += 21
        elif age == 36:
            covidage += 21
        elif age == 37:
            covidage += 21
        elif age == 38:
            covidage += 21
        elif age == 39:
            covidage += 20
        elif age == 40:
            covidage += 20
        elif age == 41:
            covidage += 20
        elif age == 42:
            covidage += 20
        elif age == 43:
            covidage += 20
        elif age == 44:
            covidage += 20
        elif age == 45:
            covidage += 20
        elif age == 46:
            covidage += 19
        elif age == 47:
            covidage += 19
        elif age == 48:
            covidage += 19
        elif age == 49:
            covidage += 19
        elif age == 50:
            covidage += 18
        elif age == 51:
            covidage += 18
        elif age == 52:
            covidage += 18
        elif age == 53:
            covidage += 18
        elif age == 54:
            covidage += 17
        elif age == 55:
            covidage += 17
        elif age == 56:
            covidage += 17
        elif age == 57:
            covidage += 16
        elif age == 58:
            covidage += 16
        elif age == 59:
            covidage += 16
        elif age == 60:
            covidage += 16
        elif age == 61:
            covidage += 15
        elif age == 62:
            covidage += 15
        elif age == 63:
            covidage += 15
        elif age == 64:
            covidage += 14
        elif age == 65:
            covidage += 14
        elif age == 66:
            covidage += 14
        elif age == 67:
            covidage += 14
        elif age == 68:
            covidage += 13
        elif age == 69:
            covidage += 13
        elif age == 70:
            covidage += 13
        elif age == 71:
            covidage += 13
        elif age == 72:
            covidage += 12
        elif age == 73:
            covidage += 12
        elif age >= 74:
            covidage += 12
    else:
        covidage += 0


 
    # organTransplant = input("Did you receive any organ transplants? (Y/N) ").lower()
    if organTransplant == 'Yes':
        
        if age == 20:
            covidage += 25
        elif age == 21:
            covidage += 25
        elif age == 22:
            covidage += 24 
        elif 23 <= age <= 24:
            covidage += 24
        elif age == 25:
            covidage += 24
        elif age == 26:
            covidage += 24
        elif age == 27:
            covidage += 24
        elif age == 28:
            covidage += 24
        elif age == 29:
            covidage += 24
        elif age == 30:
            covidage += 23
        elif age == 31:
            covidage += 23
        elif age == 32:
            covidage += 23
        elif age == 33:
            covidage += 23
        elif age == 34:
            covidage += 23
        elif age == 35:
            covidage += 23
        elif age == 36:
            covidage += 22
        elif age == 37:
            covidage += 22
        elif age == 38:
            covidage += 22
        elif age == 39:
            covidage += 22
        elif age == 40:
            covidage += 22
        elif age == 41:
            covidage += 22
        elif age == 42:
            covidage += 21
        elif age == 43:
            covidage += 21
        elif age == 44:
            covidage += 21
        elif age == 45:
            covidage += 21
        elif age == 46:
            covidage += 21
        elif age == 47:
            covidage += 20
        elif age == 48:
            covidage += 20
        elif age == 49:
            covidage += 20
        elif age == 50:
            covidage += 19
        elif age == 51:
            covidage += 19
        elif age == 52:
            covidage += 19
        elif age == 53:
            covidage += 18
        elif age == 54:
            covidage += 18
        elif age == 55:
            covidage += 18
        elif age == 56:
            covidage += 17
        elif age == 57:
            covidage += 17
        elif age == 58:
            covidage += 16
        elif age == 59:
            covidage += 16
        elif age == 60:
            covidage += 15
        elif age == 61:
            covidage += 15
        elif age == 62:
            covidage += 14
        elif age == 63:
            covidage += 14
        elif age == 64:
            covidage +=13
        elif age == 65:
            covidage += 13
        elif age == 66:
            covidage += 12
        elif age == 67:
            covidage += 12
        elif age == 68:
            covidage += 11
        elif age == 69:
            covidage += 11
        elif age == 70:
            covidage += 10
        elif age == 71:
            covidage += 10
        elif age == 72:
            covidage += 9
        elif age == 73:
            covidage += 9
        elif age >= 74:
            covidage += 8
    else:
        covidage += 0
        
    # input("Do you have rheumatoid/pupus/psoriasis?")
    if rheumatoid == 'Yes':
        covidage += 2
    else:
        covidage += 0
        
     # input("Do you have other immunosuppressive condition (Y/N) ").lower()
    if immunoSuppressive == 'Yes':
                
        if age == 20:
            covidage += 23
        elif age == 21:
            covidage += 23
        elif age == 22:
            covidage += 22 
        elif 23 <= age <= 24:
            covidage += 22
        elif age == 25:
            covidage += 22
        elif age == 26:
            covidage += 22
        elif age == 27:
            covidage += 22
        elif age == 28:
            covidage += 22
        elif age == 29:
            covidage += 22
        elif age == 30:
            covidage += 22
        elif age == 31:
            covidage += 22
        elif age == 32:
            covidage += 21
        elif age == 33:
            covidage += 21
        elif age == 34:
            covidage += 21
        elif age == 35:
            covidage += 21
        elif age == 36:
            covidage += 21
        elif age == 37:
            covidage += 21
        elif age == 38:
            covidage += 21
        elif age == 39:
            covidage += 20
        elif age == 40:
            covidage += 20
        elif age == 41:
            covidage += 20
        elif age == 42:
            covidage += 20
        elif age == 43:
            covidage += 20
        elif age == 44:
            covidage += 20
        elif age == 45:
            covidage += 20
        elif age == 46:
            covidage += 19
        elif age == 47:
            covidage += 19
        elif age == 48:
            covidage += 19
        elif age == 49:
            covidage += 19
        elif age == 50:
            covidage += 18
        elif age == 51:
            covidage += 18
        elif age == 52:
            covidage += 18
        elif age == 53:
            covidage += 18
        elif age == 54:
            covidage += 17
        elif age == 55:
            covidage += 17
        elif age == 56:
            covidage += 17
        elif age == 57:
            covidage += 16
        elif age == 58:
            covidage += 16
        elif age == 59:
            covidage += 16
        elif age == 60:
            covidage += 16
        elif age == 61:
            covidage += 15
        elif age == 62:
            covidage += 15
        elif age == 63:
            covidage += 15
        elif age == 64:
            covidage += 14
        elif age == 65:
            covidage += 14
        elif age == 66:
            covidage += 14
        elif age == 67:
            covidage += 14
        elif age == 68:
            covidage += 13
        elif age == 69:
            covidage += 13
        elif age == 70:
            covidage += 13
        elif age == 71:
            covidage += 13
        elif age == 72:
            covidage += 12
        elif age == 73:
            covidage += 12
        elif age >= 74:
            covidage += 12
    else:
        covidage += 0


 
    # organTransplant = input("Did you receive any organ transplants? (Y/N) ").lower()
    if organTransplant == 'Yes':
        
        if age == 20:
            covidage += 25
        elif age == 21:
            covidage += 25
        elif age == 22:
            covidage += 24 
        elif 23 <= age <= 24:
            covidage += 24
        elif age == 25:
            covidage += 24
        elif age == 26:
            covidage += 24
        elif age == 27:
            covidage += 24
        elif age == 28:
            covidage += 24
        elif age == 29:
            covidage += 24
        elif age == 30:
            covidage += 23
        elif age == 31:
            covidage += 23
        elif age == 32:
            covidage += 23
        elif age == 33:
            covidage += 23
        elif age == 34:
            covidage += 23
        elif age == 35:
            covidage += 23
        elif age == 36:
            covidage += 22
        elif age == 37:
            covidage += 22
        elif age == 38:
            covidage += 22
        elif age == 39:
            covidage += 22
        elif age == 40:
            covidage += 22
        elif age == 41:
            covidage += 22
        elif age == 42:
            covidage += 21
        elif age == 43:
            covidage += 21
        elif age == 44:
            covidage += 21
        elif age == 45:
            covidage += 21
        elif age == 46:
            covidage += 21
        elif age == 47:
            covidage += 20
        elif age == 48:
            covidage += 20
        elif age == 49:
            covidage += 20
        elif age == 50:
            covidage += 19
        elif age == 51:
            covidage += 19
        elif age == 52:
            covidage += 19
        elif age == 53:
            covidage += 18
        elif age == 54:
            covidage += 18
        elif age == 55:
            covidage += 18
        elif age == 56:
            covidage += 17
        elif age == 57:
            covidage += 17
        elif age == 58:
            covidage += 16
        elif age == 59:
            covidage += 16
        elif age == 60:
            covidage += 15
        elif age == 61:
            covidage += 15
        elif age == 62:
            covidage += 14
        elif age == 63:
            covidage += 14
        elif age == 64:
            covidage +=13
        elif age == 65:
            covidage += 13
        elif age == 66:
            covidage += 12
        elif age == 67:
            covidage += 12
        elif age == 68:
            covidage += 11
        elif age == 69:
            covidage += 11
        elif age == 70:
            covidage += 10
        elif age == 71:
            covidage += 10
        elif age == 72:
            covidage += 9
        elif age == 73:
            covidage += 9
        elif age >= 74:
            covidage += 8
    else:
        covidage += 0
        
    # input("Do you have rheumatoid/pupus/psoriasis?")
    if rheumatoid == 'Yes':
        covidage += 2
    else:
        covidage += 0
        
     # input("Do you have other immunosuppressive condition (Y/N) ").lower()
    if immunoSuppressive == 'Yes':
        
        if age == 20:

            covidage += 30
        elif age == 21:
            covidage += 30
        elif age == 22:
            covidage += 29 
        elif age == 23:
            covidage += 29
        elif age == 24:
            covidage += 28
        elif age == 25:
            covidage += 28
        elif age == 26:
            covidage += 27
        elif age == 27:
            covidage += 27
        elif age == 28:
            covidage += 26
        elif age == 29:
            covidage += 26
        elif age == 30:
            covidage += 25
        elif age == 31:
            covidage += 25
        elif age == 32:
            covidage += 24
        elif age == 33:
            covidage += 24
        elif age == 34:
            covidage += 23
        elif age == 35:
            covidage += 23
        elif age == 36:
            covidage += 22
        elif age == 37:
            covidage += 22
        elif age == 38:
            covidage += 21
        elif age == 39:
            covidage += 21
        elif age == 40:
            covidage += 20
        elif age == 41:
            covidage += 20
        elif age == 42:
            covidage += 19
        elif age == 43:
            covidage += 19
        elif age == 44:
            covidage += 18
        elif age == 45:
            covidage += 17
        elif age == 46:
            covidage += 17
        elif age == 47:
            covidage += 16
        elif age == 48:
            covidage += 16
        elif age == 49:
            covidage += 15
        elif age == 50:
            covidage += 15
        elif age == 51:
            covidage += 15
        elif age == 52:
            covidage += 14
        elif age == 53:
            covidage += 14
        elif age == 54:
            covidage += 13
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
            covidage += 11
        elif age == 62:
            covidage += 10
        elif age == 63:
            covidage += 10
        elif age == 64:
            covidage +=9
        elif age == 65:
            covidage += 9
        elif age == 66:
            covidage += 9
        elif age == 67:
            covidage += 8
        elif age == 68:
            covidage += 8
        elif age == 69:
            covidage += 7
        elif age == 70:
            covidage += 7
        elif age == 71:
            covidage += 7
        elif age == 72:
            covidage += 6
        elif age == 73:
            covidage += 6
        elif age >= 74:
            covidage += 5
    else:
        covidage += 0

    if spleenDisease == 'Yes':
        if age in range(20,22):
            covidage += 14
        elif age in range(22,33):
            covidage += 13
        elif age in range(33,39):
            covidage += 12
        elif age in range(39,46):
            covidage += 11
        elif age in range(46,50):
            covidage += 10
        elif age in range(50,53):
            covidage += 9
        elif age in range(53,57):
            covidage += 8
        elif age in range(57,60):
            covidage += 7
        elif age in range(60,63):
            covidage += 6
        elif age in range(63,67):
            covidage += 5
        elif age in range(67,69):
            covidage += 4
        elif age in range(69,71):
            covidage += 3
        elif age in range(71,73):
            covidage += 2
        elif age in range(73,75):
            covidage += 1



            

    if nonHematologicalCancer == 'Diagnosed less than 1 year ago':
    #diagnosis year less than 1 year
        if age==20:
            covidage += 34
        elif age in range(21,23):
            covidage += 33
        elif age in range(23,25):
            covidage += 32
        elif age in range(25,27):
            covidage += 31
        elif age in range(27,29):
            covidage += 30
        elif age in range(29,31):
            covidage += 29
        elif age in range(31,33):
            covidage += 28
        elif age in range(33,35):
            covidage += 27
        elif age in range(35,37):
            covidage += 26
        elif age in range(37,39):
            covidage += 25
        elif age in range(39,41):
            covidage += 24
        elif age in range(41,43):
            covidage += 23
        elif age in range(43,45):
            covidage += 22
        elif age in range(45,47):
            covidage += 21
        elif age in range(47,49):
            covidage += 20
        elif age in range(49,51):
            covidage += 19
        elif age in range(51,53):
            covidage += 18
        elif age in range(53,54):
            covidage += 17
        elif age in range(54,56):
            covidage += 16
        elif age in range(56,58):
            covidage += 15
        elif age in range(58,60):
            covidage += 14
        elif age in range(60,62):
            covidage += 13
        elif age in range(62,64):
            covidage += 12
        elif age in range(64,66):
            covidage += 11
        elif age in range(66,68):
            covidage += 10
        elif age in range(68,71):
            covidage += 9
        elif age in range(71,74):
            covidage += 8
        elif age in range(74,76):
            covidage += 7
#diagnosis year between 1 to 5 years
    elif nonHematologicalCancer == 'Diagnosed 1-4.9 years ago':
        if age in range(20,23):
            covidage += 25
        elif age in range(23,26):
            covidage += 24
        elif age in range(26,28):
            covidage += 23
        elif age in range(28,31):
            covidage += 22
        elif age in range(31,34):
            covidage += 21
        elif age in range(34,36):
            covidage += 20
        elif age in range(36,38):
            covidage += 19
        elif age in range(38,41):
            covidage += 18
        elif age in range(41,43):
            covidage += 17
        elif age in range(43,46):
            covidage += 16
        elif age in range(46,48):
            covidage += 15
        elif age ==48:
            covidage += 14
        elif age in range(49,51):
            covidage += 13
        elif age ==51:
            covidage += 12
        elif age in range(52,54):
            covidage += 11
        elif age in range(54,56):
            covidage += 10
        elif age in range(56,58):
            covidage += 9
        elif age in range(58,61):
            covidage += 8
        elif age in range(61,64):
            covidage += 7
        elif age in range(64,67):
            covidage += 6
        elif age in range(67,69):
            covidage += 5
        elif age in range(69,71):
            covidage += 4
        elif age in range(71,74):
            covidage += 3
        elif age in range(74,76):
            covidage += 2
#diagnosis year more than 5 year
    elif nonHematologicalCancer == 'Diagnosed greater than or equal to 5 years ago':
        if age in range(20,24):
            covidage += 18
        elif age in range(24,27):
            covidage += 17
        elif age in range(27,30):
            covidage += 16
        elif age in range(30,33):
            covidage += 15
        elif age in range(33,35):
            covidage += 14
        elif age in range(35,37):
            covidage += 13
        elif age in range(37,39):
            covidage += 12
        elif age in range(39,42):
            covidage += 11
        elif age in range(42,45):
            covidage += 10
        elif age in range(45,48):
            covidage += 9
        elif age in range(48,51):
            covidage += 8
        elif age in range(51,54):
            covidage += 7
        elif age in range(54,57):
            covidage += 6
        elif age in range(57,59):
            covidage += 5
        elif age in range(59,61):
            covidage += 4
        elif age in range(61,63):
            covidage += 3
        elif age in range(63,5):
            covidage += 2
        elif age in range(65,69):
            covidage += 1
    else:
        covidage+= 0

    if hematologicalCancer == 'Diagnosed less than 1 year ago':

        if age in range(20,22):
            covidage += 33
        elif age in range(22,26):
            covidage += 32
        elif age in range(26,30):
            covidage += 31
        elif age in range(30,34):
            covidage += 30
        elif age in range(34,38):
            covidage += 29
        elif age in range(38,42):
            covidage += 28
        elif age in range(42,45):
            covidage += 27
        elif age in range(45,48):
            covidage += 26
        elif age in range(48,50):
            covidage += 25
        elif age in range(50,52):
            covidage += 24
        elif age in range(52,54):
            covidage += 23
        elif age in range(54,56):
            covidage += 22
        elif age in range(56,58):
            covidage += 21
        elif age in range(58,60):
            covidage += 20
        elif age in range(60,62):
            covidage += 19
        elif age in range(62,63):
            covidage += 18
        elif age in range(63,65):
            covidage += 17
        elif age in range(65,67):
            covidage += 16
        elif age in range(67,69):
            covidage += 15
        elif age in range(69,71):
            covidage += 14
        elif age in range(71,73):
            covidage += 13
        elif age in range(73,75):
            covidage += 12
        elif age in range(75,76):
            covidage += 11
            
#diagnosis year between 1 to 5 years
    elif hematologicalCancer == 'Diagnosed 1-4.9 years ago':
        if age ==20:
            covidage += 32
        elif age in range(21,24):
            covidage += 31
        elif age in range(24,27):
            covidage += 30
        elif age in range(27,30):
            covidage += 29
        elif age in range(30,33):
            covidage += 28
        elif age in range(33,36):
            covidage += 27
        elif age in range(36,38):
            covidage += 26
        elif age in range(38,41):
            covidage += 25
        elif age in range(41,43):
            covidage += 24
        elif age in range(43,45):
            covidage += 23
        elif age in range(45,50):
            covidage += 22
        elif age in range(50,54):
            covidage += 21
        elif age in range(54,57):
            covidage += 20
        elif age in range(57,59):
            covidage += 19
        elif age in range(59,61):
            covidage += 18
        elif age in range(61,63):
            covidage += 17
        elif age in range(63,65):
            covidage += 16
        elif age in range(65,67):
            covidage += 15
        elif age in range(67,69):
            covidage += 14
        elif age in range(69,71):
            covidage += 13
        elif age in range(71,73):
            covidage += 12
        elif age in range(73,76):
            covidage += 11
#diagnosis year more than 5 year
    elif hematologicalCancer == 'Greater than or equal to 5 years ago':
        if age in range(20,25):
            covidage += 21
        elif age in range(25,31):
            covidage += 20
        elif age in range(31,35):
            covidage += 19
        elif age in range(35,39):
            covidage += 18
        elif age in range(39,43):
            covidage += 17
        elif age in range(43,46):
            covidage += 16
        elif age in range(46,48):
            covidage += 15
        elif age in range(48,50):
            covidage += 14
        elif age in range(50,51):
            covidage += 13
        elif age in range(51,53):
            covidage += 12
        elif age in range(53,55):
            covidage += 11
        elif age in range(55,58):
            covidage += 10
        elif age in range(58,61):
            covidage += 9
        elif age in range(61,64):
            covidage += 8
        elif age in range(64,68):
            covidage += 7
        elif age in range(68,72):
            covidage += 6
        elif age in range(72,76):
            covidage += 5

    else:
        covidage += 0

    if cerebroVascularDisease == 'Yes':

        if age in range(20,23):
            covidage += 17
        elif age in range(23,37):
            covidage +=16
        elif age in range(37,47):
            covidage +=15
        elif age in range(47,53):
            covidage +=14
        elif age in range(53,58):
            covidage +=13
        elif age in range(58,63):
            covidage +=12
        elif age in range(63,68):
            covidage +=11
        elif age in range(68,72):
            covidage +=10
        elif age in range(72,76):
            covidage +=9

    else:
        covidage += 0
    return covidage

