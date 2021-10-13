import React from "react";
import axios from "axios";
import "./register.css";
import { ReactComponent as Logo } from "../../assets/instagram.svg";

class Register extends React.Component {
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
    const { username, password } = this.state;
    const headers = {
      "Access-Control-Allow-Origin": "*",
      "Content-Type": "application/json",
    };
    axios
      .post(
        "http://0.0.0.0:11000/register",
        { username, password },
        { headers }
      )
      .then((res) => {
        console.log(res);
        console.log(res.data);
      });
  };
  render() {
    return (
      <div className="div-register">
        <div className="div-register-logo">
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
            <button onSubmit={this.handleSubmit}>Sign Up</button>
          </form>
        </div>
      </div>
    );
  }
}

export default Register;
