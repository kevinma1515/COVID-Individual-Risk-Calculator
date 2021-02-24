import React, { Component } from 'react';
import {Form} from 'react-bootstrap';

class Input extends Component{
    constructor(props){
        super(props);
        this.state = {
            value : '',
            name : this.props.name
        };
    }

    componentDidMount(){}

    change(event){
        this.props.updateValue(this.state.name, event.target.value);
    }

    stopSubmit(event){
        if (event.which === 13 /* Enter */) {
          event.preventDefault();
        }
    }

    render(){
        return (
            <div style={{fontSize: "8pt"}}>
                <Form>
                    <Form.Group size="sm" controlId={this.props.title}>
                        <Form.Label style={{fontSize: "24pt"}}  size="sm">{this.props.title}</Form.Label>
                        <Form.Control onKeyPress={this.stopSubmit.bind(this)} as='input' onChange={this.change.bind(this)} type="text"/>
                    </Form.Group>
                </Form>
            </div>
        )
    }
}

export default Input;
