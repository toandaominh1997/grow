import React, { Component } from "react";
import ReactPlayer from "react-player/lazy";

import Paper from "@mui/material/Paper";
import Grid from "@mui/material/Grid";
import InputBase from "@mui/material/InputBase";
import IconButton from "@mui/material/IconButton";
import SearchIcon from "@mui/icons-material/Search";

const URL_BASE = "http://0.0.0.0:8001";
class Youtube extends Component {
  constructor(props) {
    super(props);
    this.state = { url: "https://www.youtube.com/watch?v=P_tEFRNEnXI" };
    this.handleSearch = this.handleSearch.bind(this);
  }
  handleSearch(event) {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    let searchData = {
      text: data.get("search_text"),
    };
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(searchData),
    };
    const res = fetch(`${URL_BASE}/search`, requestOptions)
      .then((response) => response.json())
      .then((data) => {
        console.log("data", data.url);
        this.setState({ url: data.url });
      });
  }
  render() {
    return (
      <div className="root">
        <h1>Youtube</h1>
        <Grid container spacing={1} direction="column">
          <Grid item>
            <Paper
              component="form"
              onSubmit={this.handleSearch}
              sx={{ p: "4px 6px", display: "flex", alignItems: "center" }}
            >
              <InputBase
                sx={{ ml: 1, flex: 1 }}
                placeholder="search"
                name="search_text"
                inputProps={{ "aria-label": "search" }}
              />
              <IconButton type="submit" sx={{ p: "10px" }} aria-label="search">
                <SearchIcon />
              </IconButton>
            </Paper>
          </Grid>
          <Grid item>
            <ReactPlayer url={this.state.url} 
            controls={true} 
            width="60%"
            />
          </Grid>
        </Grid>
      </div>
    );
  }
}
export default Youtube;
