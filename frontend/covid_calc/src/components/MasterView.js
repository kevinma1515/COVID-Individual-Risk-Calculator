import React, { Component } from 'react';
import {Container, Row, Col} from 'react-bootstrap';
import '../App.css'
import SymptomPredictionModelView from './SymptomPredictionModelView'
import COVID_AGE_VIEW from './COVID_Age_View';

class MasterView extends Component{
    constructor(props){
        super(props);
        this.state = {
            communityRisk : 0
        };
        
    }

   

    communityRisk(risk){
        console.log(risk)
        this.setState({communityRisk: risk})
    }
    

    
  

    render(){
        return (
				<Container>
					<Row>
						<SymptomPredictionModelView updateRisk={this.communityRisk.bind(this)}/>
					</Row>
					<Row>
						<COVID_AGE_VIEW communityRisk={this.state.communityRisk}/>
					</Row>
				</Container>	
        )}

}

export default MasterView;
