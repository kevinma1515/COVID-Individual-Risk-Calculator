import React, { Component } from 'react';
import {Row, Col, Tab, Tabs, Form} from 'react-bootstrap';


class Input extends Component{
    constructor(props){
        super(props);
        this.state = {
            value : ''
        };
    }

    
    componentDidMount(){
       

    }

 

    render(){
        
     
        return (
            <div style={{fontSize: "8pt"}}>
                <Form>
                    <Form.Group size="sm" controlId={this.props.name}>
                        <Form.Label size="sm">{this.props.name}</Form.Label>
                        <Form.Control type="text"/>
                    </Form.Group>
                </Form>
            </div>
                
        )
        

    }
}

export default Input;
