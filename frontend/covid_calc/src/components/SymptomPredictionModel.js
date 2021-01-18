import React, { Component } from 'react';
import {DropdownButton, Dropdown, Tab, Tabs, Form, Container} from 'react-bootstrap';
import DropdownQuestion from './DropdownQuestion';
import Input from './Input';


class SymptomPredictionModel extends Component{
    constructor(props){
        super(props);
        this.state = {
            isLoading : true,
            questionList: false
        };
        
        fetch("http://localhost:5000/symptom_prediction_model_questions")
        .then(
            (response) => {
                return response.json();
            }
        )
        .then(
            (data) => {
                console.log(data);
                this.setState({questionList : data});
                console.log(this.state.questionList);
                console.log("ahdsfalsdflajsklj");
                return {}
            }
        )
        .then(
            (data) => {
            console.log("alsdjflajsdkfjalsdjfajsdlfjlajsdfj");
            this.setState({isLoading : false})}
        )
        .catch(console.log);
    }

    

    changeName(choice){
        this.setState({value : choice})
    }

  

    render(){

        if(this.state.isLoading === true){
            return(
                <h3>
                    ... Loading ...
                </h3>
            )
        }


        return (
            <div>
                <h2>
                    SymptomPredictionModel
                </h2>
                {this.state.questionList.questions.map(
                    (question) => {
                        if(question.question_type === 'dropdown'){
                            return (
                                <DropdownQuestion name={question.name} choices={question.choices}/>
                            )
                        }
                        if(question.question_type === 'input'){
                            return <Input name={question.name}/>
                        }
                    }
                )}
            </div>
        )
    }

}

export default SymptomPredictionModel;
