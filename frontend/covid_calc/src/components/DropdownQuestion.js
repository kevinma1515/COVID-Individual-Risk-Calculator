import React, { Component } from 'react';
import {DropdownButton, Dropdown, Tab, Tabs, Form} from 'react-bootstrap';


class DropdownQuestion extends Component{
    constructor(props){
        super(props);
        this.state = {
            value: this.props.choices[0],
            name : this.props.name,
            isLoading: true,
            
        };
        

        
    }

    
    

    changeName(choice){
        this.setState({value : choice})
    }

    change(event){
        this.props.updateValue(this.state.name, event);
    }

  

    render(){
        
        if(this.props.reset != undefined && this.props.reset === true){
            this.state.value = this.props.choices[0]
        }
        

        return (
            <div>
                {this.props.title}
                <DropdownButton 
                                id="dropdown-basic-button" 
                                title={this.state.value} 
                                onSelect={this.changeName.bind(this)}>
                    {this.props.choices.map((choice, i)=>{
                        return(
                            <Dropdown.Item  key={i}
                                            as="button" 
                                            eventKey={choice} 
                                            onSelect={this.change.bind(this)}>
                                {choice}
                            </Dropdown.Item>
                        )
                    })}
                    
                </DropdownButton>
            </div>
        )
        

    }
}

export default DropdownQuestion;
