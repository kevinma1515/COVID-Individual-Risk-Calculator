import React, { Component } from 'react';
import {Container, Row, Col} from 'react-bootstrap';
import SymptomPredictionModel from './SymptomPredictionModel';
import CommunityRisk from './CommunityRisk';
import '../App.css'


class SymptomPredictionModelView extends Component{
    constructor(props){
        super(props);
        this.state = {
            symptomRisk: 0.00,
            communityRisk: 0.00,
            symptomColor : 'white',
            communityColor : 'white',
            totalRisk : 0.00,
            totalRiskColor : 'white'
        };
        
    }

    updateSymptom(risk){
        this.setState({symptomRisk: (risk * 100).toFixed(2), symptomColor : ((1-risk)*120).toString(10)}, () => {
            this.updateTotalRisk()
            console.log(this.state.symptomColor)
        })
    }

    updateCommunity(risk){
        console.log(risk)
        this.setState({communityRisk: (risk * 100).toFixed(2), communityColor : ((1-risk)*120).toString(10)}, () => {
            this.updateTotalRisk()
            console.log(this.state.communityColor)
        })
    }

    updateTotalRisk(){
        
        this.setState({ totalRisk: (this.state.symptomRisk * this.state.communityRisk / 10000).toFixed(3), 
                        totalRiskColor : ((1-(this.state.symptomRisk * this.state.communityRisk / 10000))*120).toString(10)},
                        () => {
                            console.log(this.state.symptomRisk * this.state.communityRisk/10000)
                           this.props.updateRisk(this.state.symptomRisk * this.state.communityRisk/10000)
                        })
    
    }

    
  

    render(){
        return (
            <Container className="symptomPredView">
                <Row>
                    <Col style={{maxWidth : "45vw"}}>
                        <SymptomPredictionModel updateCovidValue={this.updateSymptom.bind(this)}/>
                        <CommunityRisk updateCovidValue={this.updateCommunity.bind(this)}/>
                    </Col>
                    <Col>
                        <div className="symptomRiskNumber" style={{color : ["hsl(",this.state.symptomColor,",100%,50%)"].join("")}}>
                            Symptom Risk <br/>
                            {this.state.symptomRisk}%
                        </div>
                        <div className="symptomRiskNumber" style={{color : ["hsl(",this.state.communityColor,",100%,50%)"].join("")}}>
                            Community Risk <br/>
                            {this.state.communityRisk}%
                        </div>
                        <div className="symptomRiskNumber" style={{color : ["hsl(",this.state.totalRiskColor,",100%,50%)"].join("")}}>
                            Total Risk <br/>
                            {this.state.totalRisk}%
                        </div>
                    </Col>
                </Row>
            </Container>
        )
    }

}

export default SymptomPredictionModelView;
