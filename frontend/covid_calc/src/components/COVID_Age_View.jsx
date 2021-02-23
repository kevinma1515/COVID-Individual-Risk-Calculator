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
                    <Col style={{margin: "auto", maxWidth : "45vw"}}>
                        <COVID_Age updateInfo={this.props.info} communityRisk={this.props.communityRisk}/>
                    </Col>
                </Row>
            </Container>
        )
    }
}

export default COVID_AGE_VIEW;
