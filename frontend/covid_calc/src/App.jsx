import './App.css';
import {Container} from 'react-bootstrap';
import MasterView from './components/MasterView';
import Particles from './components/Particles';
import React from "react";

function App() {
	return (
		<div className="App">
			<Particles/>
			<header className="App-header">
				<Container>
					<MasterView></MasterView>
				</Container>
			</header>
		</div>
	);
}

export default App;
