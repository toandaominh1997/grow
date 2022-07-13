import logo from "./logo.svg";
import "./App.css";
import Test from "./components/Test";
import Home from "./components/Home";
import SignIn from "./components/SignIn";
import Search from "./components/Search";
import TinyURL from "./components/TinyURL";
import Blog from "./components/Blog";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Button from "@mui/material/Button";

function App() {
  return (
    <div className="container">
      <Router>
        <div className="App">
          <Routes>
            <Route exact path="/" element={<Home />}></Route>
            <Route path="/signin" element={<SignIn />}></Route>
            <Route path="/search" element={<Search />}></Route>
            <Route path="/test" element={<Test />}></Route>
            <Route path="/tinyurl" element={<TinyURL />}></Route>
            <Route path="/blog" element={<Blog />}></Route>
          </Routes>
        </div>
      </Router>
	  <footer>
		<small>
		made by <a href="https://twitter.com/krzysu">Henry</a>, source code available on <a href="https://github.com/krzysu/reactjs-shopping-cart">github</a>
		</small>
	  </footer>
    </div>
  );
}

export default App;
