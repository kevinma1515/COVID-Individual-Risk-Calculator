import logo from './logo.svg';
import './App.css';
import Button from 'react-bootstrap/Button';
import {Container, Row, Col, Dropdown} from 'react-bootstrap';
import Input from './components/Input'
import MultipleChoice from './components/MultipleChoice'
import DropdownQuestion from './components/DropdownQuestion'
import SymptomPredictionModelView from './components/SymptomPredictionModelView'
import COVID_AGE_VIEW from './components/COVID_Age_View';
import MasterView from './components/MasterView';
function App() {
	return (
		<div className="App">
			<header className="App-header">

				<Container>
					<MasterView></MasterView>
				</Container>
			</header>
			<footer className="App-footer">

			</footer>
		</div>
	);
}

export default App;
