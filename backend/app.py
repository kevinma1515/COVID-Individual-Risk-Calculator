from flask import request, jsonify, make_response
from flask_cors import cross_origin
from app_config import app
import ProbabilityOfCOVID
import covidAgeToProbability
import CovidAGE
import json
import pandas as pd

df = pd.read_csv('us-counties.csv')  # data collected from NYTimes github
hf = pd.read_csv('co-est2019-alldata.csv', encoding="ISO-8859-1")  # data collected from US census
df = df.sort_values(by=['county', 'state'])

with open('question_jsons/symptom_prediction_model.json', 'r') as f:
    symptom_prediction_model_questions_json = json.load(f)
with open('question_jsons/covid_age.json', 'r') as f:
    covid_age_questions_json = json.load(f)
with open('state-county.json', 'r') as f:
    state_county_json = json.load(f)


del df['date']
del hf['SUMLEV']
del hf['REGION']
del hf['DIVISION']
del hf['STATE']


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/symptom_prediction_model_questions', methods=['GET'])
@cross_origin()
def symptom_prediction_model_questions():
    if request.method == 'GET':
        return make_response(symptom_prediction_model_questions_json, 200)


@app.route('/covid_age_model_questions', methods=['GET'])
@cross_origin()
def covid_age_model_questions():
    if request.method == 'GET':
        return make_response(covid_age_questions_json, 200)


@app.route('/state_county_list', methods=['GET'])
@cross_origin()
def state_county_list():
    if request.method == 'GET':
        return make_response(state_county_json, 200)


@app.route('/symptom_prediction_model_result', methods=['POST'])
@cross_origin()
def symptom_prediction_model():
    if request.method == 'POST':
        data = request.get_json()
        if len(data['age']) == 0:
            data['age'] = 0
        result = ProbabilityOfCOVID.symptomPredictionModel(float(data['age']),
                                                        data['sex'],
                                                        data['smellTasteSymptom'],
                                                        data['coughSymptoms'],
                                                        data['severeFatigues'],
                                                        data['skippedMeal'])
        print(result)
        return make_response(jsonify({"result" : result}), 200)


@app.route('/community_risk_result', methods=['POST'])
@cross_origin()
def community_risk():
    if request.method == 'POST':
        data = request.get_json()
        state_name = data['state']
        county_name = data['county']

        # narrowing the rows to just the state and county desired
        df_rowValue = df.loc[(df['state']== state_name) & (df['county'] == county_name)]
        # find the row number of a specific county and state for census dataframe
        hf_row = hf['Combined'].str.contains(state_name + county_name,na = False).idxmax()
        # reverse the dataframe
        df_rowValue = df_rowValue[::-1]

        # locate the county population and county active cases
        county_population = hf.iloc[hf_row, 14]
        print("The population of", state_name + " " + county_name, "County is", county_population, "people.")
        county_totalCasesToday = df_rowValue.iloc[0,3]
        county_totalCasesTenDays = df_rowValue.iloc[10,3]
        county_activeCases = county_totalCasesToday - county_totalCasesTenDays
        print(county_name, "has", county_activeCases, "active cases.")
        # calculate the community risk
        comm_risk = int(county_activeCases)/int(county_population)

        return make_response(jsonify({"result" : comm_risk}), 200)


@app.route('/covid_age_result', methods=['POST'])
@cross_origin()
def covid_age_result():
    if request.method == 'POST':
        data = request.get_json()
        if len(str(data['age'])) == 0:
            data['age'] = 0
        if len(str(data['bmi'])) == 0:
            data['bmi'] = 0
        print(data)
        covidAge = CovidAGE.covidAge(int(data['age']), 
                                        data['gender'], 
                                        data['race'],
                                        int(data['bmi']),
                                        data['asthma'],
                                        data['severityAsthma'],
                                        data['respiratoryDisease'],
                                        data['hypertension'],
                                        data['heartFailure'],
                                        data['type1Diabetes'],
                                        data['type2Diabetes'],
                                        data['chronicKidneyDisease'],
                                        data['liverDisease'],
                                        data['chronicNeurlogical'],
                                        data['organTransplant'],
                                        data['rheumatoid'],
                                        data['immunoSuppressive'],
                                        data['spleenDisease'],
                                        data['nonHematologicalCancer'],
                                        data['hematologicalCancer'],
                                        data['cerebroVascularDisease'])
        print(covidAge)
        results = covidAgeToProbability.conversionToRisk(covidAge, float(data['community_risk']))
        print(results)
        return make_response(jsonify(results), 200)

