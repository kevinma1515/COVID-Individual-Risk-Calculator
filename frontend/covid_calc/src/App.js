import logo from './logo.svg';
import './App.css';
import Button from 'react-bootstrap/Button';
import {Container, Row, Col} from 'react-bootstrap';
function App() {
  return (
    <div className="App">
      <header className="App-header">
       
        <Container>
          <Row>
            tabs
          </Row>
          <Row>
            <Col>
              hi
            </Col>
            <Col>
              <Row>
                Calc
              </Row>
              <Row>
                Text
              </Row>
            </Col>
          </Row>
        </Container>
      </header>
    </div>
  );
}

export default App;
