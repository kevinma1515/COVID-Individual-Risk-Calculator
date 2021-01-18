import React, { Component } from 'react';
import {Container, Row, Col} from 'react-bootstrap';
import SymptomPredictionModel from './SymptomPredictionModel';
import '../App.css'


class SymptomPredictionModelView extends Component{
    constructor(props){
        super(props);
        this.state = {
            covidRisk: 0.0,
            color : 'white'
        };
        
    }

    updateCovid(risk){
        this.setState({covidRisk: (risk * 100).toFixed(2), color : ((1-risk)*120).toString(10)})
    }
    
  

    render(){
        return (
            <Container>
                <Row>
                    <Col>
                        <SymptomPredictionModel updateCovidValue={this.updateCovid.bind(this)}/>
                    </Col>
                    <Col>
                        <div className="covidRiskNumber" style={{color : ["hsl(",this.state.color,",100%,50%)"].join("")}}>
                            {this.state.covidRisk}%
                        </div>
                    </Col>
                </Row>
            </Container>
        )
    }

}

export default SymptomPredictionModelView;
