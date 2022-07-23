import React, { Component } from "react";
import Paper from "@mui/material/Paper";
import InputBase from "@mui/material/InputBase";
import IconButton from "@mui/material/IconButton";
import SearchIcon from "@mui/icons-material/Search";

import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import { CardContent, CardMedia, Divider } from "@mui/material";
import Typography from "@mui/material/Typography";
import CardActions from "@mui/material/CardActions";
import Button from "@mui/material/Button";

class EcomHome extends Component {
  constructor(props) {
    super(props);
  }

  cards = [
    {
        "title": "Tonne",
        "image_url": "https://ftsdlskits.com/wp-content/uploads/2019/07/barcelona-logo-300x300.png",
        "description": "The description"
    },
    {
        "title": "Elastic Search",
        "image_url": "https://it.amid.com/wp-content/uploads/2018/11/elastic-logo-V-full-color.png",
        "description": "The description"
    },
    {
        "title": "MeliSearch",
        "image_url": "https://i.pinimg.com/736x/04/43/8a/04438a69ce2fe19faf3818e2a16fef2f.jpg",
        "description": "The description"
    },
    {
        "title": "Django",
        "image_url": "https://i.pinimg.com/736x/04/43/8a/04438a69ce2fe19faf3818e2a16fef2f.jpg",
        "description": "The description"
    },
    {
        "title": "Django",
        "image_url": "https://i.pinimg.com/736x/04/43/8a/04438a69ce2fe19faf3818e2a16fef2f.jpg",
        "description": "The description"
    },
    {
        "title": "Django",
        "image_url": "https://i.pinimg.com/736x/04/43/8a/04438a69ce2fe19faf3818e2a16fef2f.jpg",
        "description": "The description"
    },
    {
        "title": "Django",
        "image_url": "https://i.pinimg.com/736x/04/43/8a/04438a69ce2fe19faf3818e2a16fef2f.jpg",
        "description": "The description"
    },
    {
        "title": "Django",
        "image_url": "https://i.pinimg.com/736x/04/43/8a/04438a69ce2fe19faf3818e2a16fef2f.jpg",
        "description": "The description"
    },
  ];

  render() {
    return (
      <div className="root">
        <Paper sx ={{p: "10px 10px", alighItems: "center"}}>
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
        <Button variant="contained" href="/ecom/addproduct">Add</Button>
        
        <Grid container spacing={{ xs: 2, md: 0.5 }} columns={{ xs: 4, sm: 8, md: 12 }}>
          {this.cards.map((card) => {
            const { title, image_url, description } = card;
            return (
              <Grid item xs={2} sm={5} md={2}>
                <Card >
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
    );
  }
}
export default EcomHome;
