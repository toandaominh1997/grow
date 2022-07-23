import React, { Component } from "react";
import Container from "@mui/material/Container";

import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import { CardContent, CardMedia, Divider } from "@mui/material";
import Typography from "@mui/material/Typography";
import CardActions from "@mui/material/CardActions";
import Button from "@mui/material/Button";

import Paper from "@mui/material/Paper";
import InputBase from "@mui/material/InputBase";
import IconButton from "@mui/material/IconButton";
import SearchIcon from "@mui/icons-material/Search";

const URL_BASE = "http://0.0.0.0:8001";
class Blog extends Component {
  constructor(props) {
    super(props);

    this.fetchData();
    this.state = {
      card: "none",
    };
    this.handleSearch = this.handleSearch.bind(this);
  }
  cards = [];
  fetchData() {
    const requestOptions = {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    };
    const res = fetch(`${URL_BASE}/v1/api/recommend`, requestOptions)
      .then((response) => response.json())
      .then((data) => {
        console.log("data", data);
        this.setState({ card: 0 });
        this.cards = data;
      });
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
    const res = fetch(`${URL_BASE}/v1/api/search`, requestOptions)
      .then((response) => response.json())
      .then((data) => {
        console.log("data", data);
        this.setState({ card: 0 });
        this.cards = data;
      });
  }
  render() {
    return (
      <div className="root">
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
        <h1>Divider</h1>
        <Button variant="contained" href="/blog/write">
          Write
        </Button>

        <Grid container spacing={{ xs: 2, md: 3 }} columns={{ xs: 4, sm: 8, md: 12 }}>
          {this.cards.map((card) => {
            const { user_id, title, image_url, description } = card;
            return (
              <Grid item xs={2} sm={4} md={4}>
                <Card sx={{ minWidth: 768 }}>
                  <CardMedia
                    component="img"
                    height="140"
                    image={image_url}
                    alt="green iguana"
                  />
                  <CardContent>
                    <Typography gutterBottom variant="h5" component="div">
                      {title}
                    </Typography>

                    <Typography variant="body2" color="text.secondary">
                      {description}
                    </Typography>
                  </CardContent>
                  <Divider light />
                  <CardActions>
                    <Button size="small">Share</Button>
                    <Button size="small">Learn More</Button>
                  </CardActions>
                </Card>
              </Grid>
            );
          })}
        </Grid>
      </div>

      // <Container maxWidth="sm">
      //     <div>
      //         <h1>Tonne</h1>
      //     </div>
      // </Container>
    );
  }
}

export default Blog;
