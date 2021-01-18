from flask import Flask, request, abort, jsonify, make_response
from flask_cors import cross_origin
import ProbabilityOfCOVID 
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'




"""
{
    age: int/float
    sex: M 1.0, F 1.0
    smellTasteSymptom:
    coughSymptoms:
    severeFatigues:
    skippedMeal:
}
"""
@app.route('/symptom_prediction_model_questions', methods=['GET'])
@cross_origin()
def symptom_prediction_model_questions():
    if request.method == 'GET':
        with open('question_jsons/symptom_prediction_model.json', 'r') as f:
            data = json.load(f)
            return make_response(data, 200)


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



                                
        