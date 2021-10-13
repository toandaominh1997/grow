import React from "react";
import { Switch, Route } from "react-router-dom";
import logo from "./logo.svg";
import Login from "./pages/login/login";
import Register from "./pages/register/register";
import "./App.css";

class App extends React.Component {
  state = {
    isLog: false,
  };

  handleLogin = (isLog) => this.setState({ isLog });
  render() {
    const { isLog } = this.state;
    return (
      <div>
        <Switch>
          <Route path="/login">
            <Login />
          </Route>
          <Route path="/register">
            <Register />
          </Route>
        </Switch>
      </div>
    );
  }
}

export default App;
