import logo from './logo.svg';
import './App.css';
import Test from './components/Test';
import { BrowserRouter as Router, Route} from 'react-router-dom';

function App() {
	return (
		<div className="App">
			<header className="App-header">
				<img src={logo} className="App-logo" alt="logo" />
				<p>
					Edit <code>src/App.js</code> and save to reload.
				</p>
				<a
					className="App-link"
					href="https://reactjs.org"
					target="_blank"
					rel="noopener noreferrer"
				>
					Learn React
				</a>
			</header>
			<div className="container">
				<h1>divfd</h1>
				<Router>
					
				</Router>
			</div>
		</div>
	);
}

export default App;
