import React, { Component } from "react";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import CssBaseline from "@mui/material/CssBaseline";
import TextField from "@mui/material/TextField";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import Link from "@mui/material/Link";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import { Routes, Route, Navigate } from "react-router-dom";

import { loginUser } from "./../actions/user";
import { connect } from "react-redux";

const URL_BASE = "http://0.0.0.0:8001";

class SignIn extends Component {
  constructor(props) {
    super(props);
    this.theme = createTheme();
    this.state = {
      toSignin: false,
    };
    this.handleSubmit = this.handleSubmit.bind(this);
  }
  handleSubmit(event) {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const userData = {
      email: data.get("email"),
      password: data.get("password"),
    };
    console.log("Start fetch");
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(userData),
    };
    const res = fetch(`${URL_BASE}/v1/api/add_user`, requestOptions)
      .then((response) => response.json())
      .then((data) => {
        console.log("data", data);
        if (data != false) {
          localStorage.setItem("token", data.jwt);
          this.setState({ toSignin: true });
          this.props.loginUser({ token: data.jwt });
        }
      });
    console.log(res);
  }
  render() {
    if (this.state.toSignin) {
      return <Navigate replace to="/signin" />;
    }
    return (
      <ThemeProvider theme={this.theme}>
        <Container component="main" maxWidth="xs">
          <CssBaseline />
          <Box
            sx={{
              marginTop: 8,
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
            }}
          >
            <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
              <LockOutlinedIcon />
            </Avatar>
            <Typography component="h1" variant="h5">
              Sign up
            </Typography>
            <Box
              component="form"
              onSubmit={this.handleSubmit}
              noValidate
              sx={{ mt: 1 }}
            >
              <TextField
                margin="normal"
                required
                fullWidth
                id="email"
                label="Email Address"
                name="email"
                autoComplete="email"
                autoFocus
              />
              <TextField
                margin="normal"
                required
                fullWidth
                name="password"
                label="Password"
                type="password"
                id="password"
                autoComplete="current-password"
              />
              <FormControlLabel
                control={<Checkbox value="remember" color="primary" />}
                label="Remember me"
              />
              <Button
                type="submit"
                fullWidth
                variant="contained"
                sx={{ mt: 3, mb: 2 }}
              >
                Sign Up
              </Button>
            </Box>
          </Box>
        </Container>
      </ThemeProvider>
    );
  }
}

const mapDispatchToProps = (dispatch) => ({
  loginUser: (user) => dispatch(loginUser(user)),
});
export default connect(null, mapDispatchToProps)(SignIn);