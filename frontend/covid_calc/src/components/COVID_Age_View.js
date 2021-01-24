import React, { Component } from 'react';
import {Container, Row, Col} from 'react-bootstrap';
import COVID_Age from './COVID_Age';
import '../App.css'


class COVID_AGE_VIEW extends Component{
    constructor(props){
        super(props);
        this.state = {
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

    updateInfo(info){
        this.setState({ death : (info['probDeath'] * 100).toFixed(3), 
                        hospitalization: (info['probHosp']*100).toFixed(3),
                        icu: (info['probICU']*100).toFixed(3),
                        score: (info['riskScore']).toFixed(3)})
    }


    
  

    render(){
        console.log(this.props.communityRisk)
        return (
            <Container className="symptomPredView">
                <Row>
                    <Col style={{maxWidth : "45vw"}}>
                        <COVID_Age updateInfo={this.updateInfo.bind(this)} communityRisk={this.props.communityRisk}/>
                    </Col>
                    <Col>
                    <div className="symptomRiskNumber">
                            Probability of Death <br/>
                            {this.state.death}%
                        </div>
                        <div className="symptomRiskNumber" >
                            Probability of Hospitalization <br/>
                            {this.state.hospitalization}%
                        </div>
                        <div className="symptomRiskNumber" >
                            Probability of ICU <br/>
                            {this.state.icu}%
                        </div>
                        <div className="symptomRiskNumber" >
                            Risk Score <br/>
                            {this.state.score}
                        </div>
                        
                    </Col>
                </Row>
            </Container>
        )
    }

}

export default COVID_AGE_VIEW;
