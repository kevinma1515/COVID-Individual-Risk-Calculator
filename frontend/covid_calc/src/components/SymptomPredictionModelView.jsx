import React, { Component } from 'react';
import {Container, Row, Col} from 'react-bootstrap';
import SymptomPredictionModel from './SymptomPredictionModel';
import CommunityRisk from './CommunityRisk';
import '../App.css'

class SymptomPredictionModelView extends Component{
    constructor(props){
        super(props);
    }



    render(){
        return (
            <Container className="symptomPredView">
                <Row>
                    <Col style={{margin: "auto", maxWidth : "45vw"}}>
                        <SymptomPredictionModel updateCovidValue={this.props.symptom}/>
                        <CommunityRisk updateCovidValue={this.props.community}/>
                    </Col>
                </Row>
            </Container>
        )
    }

}

export default SymptomPredictionModelView;
