import React, { Component } from 'react';
import {DropdownButton, Dropdown} from 'react-bootstrap';
import '../styles/Dropdown.css'

class DropdownQuestion extends Component{
    constructor(props){
        super(props);
        this.state = {
            value: this.props.choices[0],
            name : this.props.name,
            isLoading: true,
            tempChoices : this.props.choices
        };
    }

    changeName(choice){
        this.setState({value : choice})
    }

    change(event){
        this.props.updateValue(this.state.name, event);
    }

    render(){

        if(JSON.stringify(this.props.choices)!=JSON.stringify(this.state.tempChoices)){
            this.state.value = this.props.choices[0]
            this.state.tempChoices = this.props.choices
        }

        return (
            <div>
                {this.props.title}
                <DropdownButton
                                id="dropdown-basic-button"
                                title={this.state.value}
                                onSelect={this.changeName.bind(this)}>
                    <div className='dropdown-div'>
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
                    </div>

                </DropdownButton>
            </div>
        )
    }
}

export default DropdownQuestion;
