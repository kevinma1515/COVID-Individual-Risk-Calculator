# COVID-Individual-Risk-Calculator
Calculate your individual risk of COVID based on your age, sex, ethnicity, symptoms, health conditions, behaviors, and more...

> Risk = ((Proportion of Community with Active Cases)(Symptom Probability)(Susceptibility))/(Normalization Factor) 

Please note that the "us-counties.csv" file can be retrieved from the NYTimes COVID-19 github  
Link here https://github.com/nytimes/covid-19-data

The symptomatic risk was calculated using a logistic regression based off of symptom reports by people who did not have COVID and who had COVID.

The health risk was integrated into our calculator from a paper posted by ALAMA.         
Link here https://alama.org.uk/covid-19-medical-risk-assessment/       
Conversion from COVID age to probability of death, ICU, and hospitalization were converted using an exponential distribution based off of different studies on how age can affect your chances of dying, going into the ICU and getting hospitalized.       

The community risk was calculated by using the us-counties.csv file retrieved from the NYTimes COVID-19 github. File is updated on a weekly basis.

# Contributors
## Team
- Kevin Ma - *team lead*
- Timothy Gan - *full-stack developer*
- Bishal Thapa - *back-end developer*
- Daniel Ajisafe - *front-end developer/UI designer*
- Anaya Mehta - *front-end developer*



## Advisor
- Dr. Michael Lachmann - *Professor at Santa Fe Institute*
- Dr. Jennifer Johnson-Leung - *Assistant Professor at University of Idaho*
