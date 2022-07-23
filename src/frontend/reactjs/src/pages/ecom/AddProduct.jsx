import React, { Component } from "react";
import Box from "@mui/material/Box";
import Paper from "@mui/material/Paper";
import TextField from "@mui/material/TextField";
import Input from "@mui/material/Input";
import Button from "@mui/material/Button";
import TextareaAutosize from "@mui/material/TextareaAutosize";
import { createTheme, ThemeProvider } from "@mui/material/styles";
import Container from "@mui/material/Container";
import CssBaseline from "@mui/material/CssBaseline";
import Avatar from "@mui/material/Avatar";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";

import { Routes, Route, Navigate } from "react-router-dom";

const URL_BASE = "http://0.0.0.0:8001";

class AddProduct extends Component {
  constructor(props) {
    super(props);
    this.theme = createTheme();
    this.state = {
      image: "none",
	  toEcom: false,
    };
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleImageChange = this.handleImageChange.bind(this);
  }
  handleImageChange(event) {
    console.log("here");
    console.log(event.target.files);
    this.setState({ image: event.target.files[0] });
  }
  handleSubmit(event) {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const postData = {
      title: data.get("title"),
      description: data.get("description"),
      image_url: data.get("image_url"),
    };
    console.log(postData);
    // const formdata = new FormData();
    // formdata.append("title", event.target.title.value);
    // formdata.append("description", event.target.description.value);
    // console.log("image name: ", this.state["image"].name);

    // console.log("formdata", event.target.title.value)
    // console.log("formdata: ", formdata);
    // formdata.append("file", this.state.image, this.state.image.name);
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(postData),
    };
    const res = fetch(`${URL_BASE}/v1/api/ecom/add_product`, requestOptions)
      .then((response) => response.json())
      .then((data) => {
        console.log("data", data);
		this.setState({toEcom: true});
      });
  }

  render() {
	if (this.state.toEcom) {
		return <Navigate replace to="/ecom" />;
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
              Upload Product
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
                id="title"
                label="Title"
                name="title"
                autoFocus
              />
              <TextField
                margin="normal"
                required
                fullWidth
                id="image_url"
                label="Image URL"
                name="image_url"
                autoFocus
              />
              <TextField
                margin="normal"
                required
                fullWidth
                id="description"
                label="Descriptions"
                name="description"
                autoFocus
              />
              <Button
                type="submit"
                fullWidth
                variant="contained"
                sx={{ mt: 3, mb: 2 }}
              >
                Submit
              </Button>
            </Box>
          </Box>
        </Container>
      </ThemeProvider>
    );
  }
}

export default AddProduct;
