import React, { Component } from "react";
import Box from "@mui/material/Box";
import Paper from "@mui/material/Paper";
import TextField from "@mui/material/TextField";
import Button from "@mui/material/Button";
import TextareaAutosize from "@mui/material/TextareaAutosize";


const URL_BASE = "http://0.0.0.0:8001";

class AddProduct extends Component {
  constructor(props) {
    super(props);
    this.state = {
        image: 'none',
    }
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleImageChange = this.handleImageChange.bind(this);
  }
  handleImageChange(event) {
    console.log("here")
    console.log(event.target.files)
    this.setState({"image": event.target.files[0]})
  }
  handleSubmit(event) {
    event.preventDefault();
    // const data = new FormData(event.currentTarget);
    // const postData = {
    //     "title": data.get("title"),
    //     "description": data.get("description"),
    //     "image": this.state["image"]
    // }
    // console.log(postData);
    const formdata = new FormData();
    // formdata.append("title", event.target.title.value);
    // formdata.append("description", event.target.description.value);
    console.log("image name: ", this.state["image"].name);
    
    console.log("formdata", event.target.title.value)
    console.log("formdata: ", formdata);
    formdata.append("file", this.state.image, this.state.image.name);
    const requestOptions = {
        method: "POST",
        headers: { 'content-type': 'multipart/form-data' },
        body: formdata,
      };
      const res = fetch(`${URL_BASE}/v1/api/ecom/add_product`, requestOptions)
        .then(
            response => {
                if(response.ok) {
                    return response.json();
                } else {
                    throw new Error("Something wrong")
                }
            }
        )
        .then((data) => {
          console.log("data", data);
        });
  }
  render() {
    return (    
      <Paper
        component="form"
        onSubmit={this.handleSubmit}
        sx={{ p: "4px 6px", display: "flex", alignItems: "center" }}
      >
          <TextField id="outlined-name" label="Title" name="title" />
          <Button variant="contained" component="label">
            Upload Image
            <input hidden accept="image/*"  type="file" onChange={this.handleImageChange} />
          </Button>
          <TextareaAutosize
            aria-label="minimum height"
            minRows={5}
            placeholder="description"
            name="description"
            style={{ width: 500 }}
          />

          <Button variant="contained" component="label">
            Submit
          </Button>
      </Paper>
    );
  }
}

export default AddProduct;
