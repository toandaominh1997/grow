import logo from "./logo.svg";
import "./App.css";
import Test from "./components/Test";
import Home from "./components/Home";
import SignIn from "./components/SignIn";
import Search from "./components/Search";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Button from "@mui/material/Button";



function App() {
	return (
		<Router>
			<div className="App">
				<Routes>
					<Route exact path="/" element={<Home/>}></Route>
					<Route path="/signin" element={<SignIn/>}></Route>
					<Route path="/search" element={<Search/>}></Route>
					<Route path="/test" element={<Test/>}></Route>
				</Routes>
			</div>
		</Router>
	);
}

export default App;
