import React, { Component } from 'react';
import {Col, Container, Row} from 'react-bootstrap';
import '../App.css'
import SymptomPredictionModelView from './SymptomPredictionModelView'
import COVID_AGE_VIEW from './COVID_Age_View';

class MasterView extends Component{
    constructor(props){
        super(props);
        this.state = {
            communityRisk: 0.00,
            symptomRisk: 0.00,
            symptomColor : 'white',
            communityColor : 'white',
            totalRisk : 0.00,
            totalRiskColor : 'white',
            death: 0.00,
            hospitalization: 0.00,
            deathColor : 'white',
            hospitalizationColor : 'white',
            icu : 0.00,
            icuColor : 'white',
            score : 0.00,
            scoreColor : 'white'
        };
    }

    communityRisk(risk){
        console.log(risk)
        this.setState({communityRisk: risk})
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
                            this.communityRisk(this.state.symptomRisk * this.state.communityRisk/10000)
                        })

    }

    updateInfo(info){
        this.setState({ death : (info['probDeath'] * 100).toFixed(3),
                        hospitalization: (info['probHosp']*100).toFixed(3),
                        icu: (info['probICU']*100).toFixed(3),
                        score: (info['riskScore']).toFixed(3)})
    }

    render() {
        return (
            <Container className="form-g" style={{marginTop: "24%"}}>
                <nav className="navbar navbar-light bg-dark fixed-top">
                    <Row style={{width: "100%"}}>
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
                    </Row>
                    <Row style={{width: "100%"}}>
                        <div className="riskNumber">
                            Probability of Death <br/>
                            {this.state.death}%
                        </div>
                        <div className="riskNumber" >
                            Probability of Hospitalization <br/>
                            {this.state.hospitalization}%
                        </div>
                        <div className="riskNumber" >
                            Probability of ICU <br/>
                            {this.state.icu}%
                        </div>
                        <div className="riskNumber" >
                            Risk Score <br/>
                            {this.state.score}
                        </div>
                    </Row>
                </nav>
                <Col>
                    <SymptomPredictionModelView style={{textAlign: "center"}} symptom={this.updateSymptom.bind(this)} community={this.updateCommunity.bind(this)}/>
                </Col>
                <Col>
                    <COVID_AGE_VIEW info={this.updateInfo.bind(this)} communityRisk={this.state.communityRisk}/>
                </Col>
            </Container>
        )}
}

export default MasterView;
