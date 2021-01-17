import logo from './logo.svg';
import './App.css';
import Button from 'react-bootstrap/Button';
import {Container, Row, Col, Dropdown} from 'react-bootstrap';
import Input from './components/Input'
import MultipleChoice from './components/MultipleChoice'
import DropdownQuestion from './components/DropdownQuestion'
import SymptomPredictionModel from './components/SymptomPredictionModel'
function App() {
  return (
    <div className="App">
      <header className="App-header">
       
        <Container>
          <Row>
            <Col>
                <SymptomPredictionModel/>
              </Col>
            <Col>
            </Col>
          </Row>
            
        </Container>
      </header>
    </div>
  );
}

export default App;
