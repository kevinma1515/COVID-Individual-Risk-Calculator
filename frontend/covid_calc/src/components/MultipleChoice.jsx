import React, { Component } from 'react';
import {Row, Col, Tab, Tabs, Form} from 'react-bootstrap';

class MultipleChoice extends Component{
    constructor(props){
        super(props);
        this.state = {

        };
    }

    componentDidMount(){}

    render(){
        return (
            <fieldset>
                <Form.Group >
                <Form.Label column sm={2}>
                    {this.props.name}
                </Form.Label>
                        {this.props.choices.map((choice, id) =>
                            {
                                return(
                                    <Row>
                                        <Form.Check inline
                                            type="radio"
                                            label={choice}
                                            name={this.props.name}
                                            id={this.props.name + choice + id}
                                        />
                                    </Row>
                                )
                            })
                        }
                </Form.Group>
            </fieldset>
        )
    }
}

export default MultipleChoice;
