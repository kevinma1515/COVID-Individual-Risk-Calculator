import React, { Component } from 'react';
import {DropdownButton, Dropdown, Tab, Tabs, Form} from 'react-bootstrap';


class DropdownQuestion extends Component{
    constructor(props){
        super(props);
        this.state = {
            value : this.props.choices[0]
        };
    }

    
    componentDidMount(){
       

    }

    changeName(choice){
        this.setState({value : choice})
    }

  

    render(){

     
        return (
            <div>
                {this.props.name}
                <DropdownButton id="dropdown-basic-button" title={this.state.value} onSelect={this.changeName.bind(this)}>
                    {this.props.choices.map((choice)=>{
                        return(
                            <Dropdown.Item as="button" eventKey={choice}>{choice}</Dropdown.Item>
                        )
                    })}
                    
                </DropdownButton>
            </div>
        )
        

    }
}

export default DropdownQuestion;
