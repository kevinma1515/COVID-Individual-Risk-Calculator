import React, { Component } from 'react';
import {DropdownButton, Dropdown, Tab, Tabs, Form, Container} from 'react-bootstrap';
import DropdownQuestion from './DropdownQuestion';
import Input from './Input';


class CommunityRisk extends Component{
    constructor(props){
        super(props);
        this.state = {
            isLoading : true,
            data : {},
            currentState : "Alabama",
            currentCounty : "Autauga",
            communityRisk : 0.0
        };
        
        fetch("http://localhost:5000/state_county_list")
        .then(
            (response) => {
                return response.json();
            }
        )
        .then(
            (response) => {
                this.setState({data : response})
                return {}
            }
        )
        .then(
            (response) => {
                this.setState({isLoading : false})
            }
        )
        .catch(console.log);
    }



    
    updateState(key, value){        
        this.setState({currentState: value, currentCounty: this.state.data[value][0]})
        this.props.updateCovidValue(0)
    }

    updateCounty(key, value){
        this.setState({currentCounty : value})
        this.calculate()
    }

    calculate(){
        console.log("calculate")
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({"state" : this.state.currentState, "county" : this.state.currentCounty})
        }
        console.log(requestOptions.body)
        fetch("http://localhost:5000/community_risk_result", requestOptions)
        .then(
            (response) => {
                return response.json();
            }
        )
        .then(
            (data) => {
                this.setState({communityRisk : data.result})
                this.props.updateCovidValue(this.state.communityRisk)
                console.log("Community risk: " + this.state.communityRisk)
            }
        )
        .catch(console.log)
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
                
                <DropdownQuestion updateValue=  {this.updateState.bind(this)} 
                                        title="Choose your state." 
                                        choices={this.state.data["states"]}
                                        name="state"/>
                <DropdownQuestion updateValue=  {this.updateCounty.bind(this)} 
                                        title="Choose your county." 
                                        choices={this.state.data[this.state.currentState]}
                                        name="county"
                                        start_value={this.state.data[this.state.currentState][0]}/>

            </div>
        )
    }

}

export default CommunityRisk;
