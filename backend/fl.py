from flask import Flask, request, abort, jsonify, make_response
import ProbabilityOfCOVID 

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
@app.route('/symptom_prediction_model', methods=['GET'])
def symptom_prediction_model():
    if request.method == 'GET':
        data = request.form
        print(data)
        result = ProbabilityOfCOVID.symptomPredictionModel(float(data['age']), 
                                                        data['sex'], 
                                                        data['smellTasteSymptom'],
                                                        data['coughSymptoms'],
                                                        data['severeFatigues'],
                                                        data['skippedMeal'])
        return make_response(jsonify({"result" : result}), 200)



                                
        