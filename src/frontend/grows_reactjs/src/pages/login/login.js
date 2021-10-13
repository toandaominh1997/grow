import React from "react";
import axios from "axios";
import "./login.css";
import { ReactComponent as Logo } from "../../assets/instagram.svg";
axios.defaults.headers.post["Content-Type"] =
  "application/x-www-form-urlencoded";
class Login extends React.Component {
  state = {
    username: "",
    password: "",
  };
  handleChange = (e) => {
    const { name, value } = e.target;
    this.setState({ [name]: value });
  };
  handleSubmit = (e) => {
    e.preventDefault();
    console.log(e);
    const { username, password } = this.state;
    const headers = {
      "Access-Control-Allow-Origin": "*",
      "Content-Type": "application/json",
    };
    axios
      .post("http://0.0.0.0:11000/login", { username, password }, { headers })
      .then((res) => {
        console.log(res);
        console.log(res.data);
      });
  };
  render() {
    return (
      <div className="div-login">
        <div className="div-login-logo">
          <Logo />
        </div>
        <div>
          <form onSubmit={this.handleSubmit}>
            <input
              type="text"
              name="username"
              placeholder="username..."
              required
              onChange={this.handleChange}
            />
            <input
              type="password"
              name="password"
              placeholder="password..."
              required
              onChange={this.handleChange}
            />
            <button onSubmit={this.handleSubmit}>Log In</button>
          </form>
        </div>
      </div>
    );
  }
}

export default Login;
