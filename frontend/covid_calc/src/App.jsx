import './App.css';
import {Container} from 'react-bootstrap';
import MasterView from './components/MasterView';

function App() {
	return (
		<div className="App">
			<header className="App-header">
				<Container>
					<MasterView></MasterView>
				</Container>
			</header>
		</div>
	);
}

export default App;
