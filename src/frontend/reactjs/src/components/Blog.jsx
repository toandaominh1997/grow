import React, { Component } from "react";
import Container from "@mui/material/Container";

import Grid from "@mui/material/Grid";
import Card from "@mui/material/Card";
import { CardContent, CardMedia, Divider } from "@mui/material";
import Typography from "@mui/material/Typography";
import CardActions from "@mui/material/CardActions";
import Button from "@mui/material/Button";

class Blog extends Component {
  cards = [
    {
      image:
        "https://image.freepik.com/free-photo/river-foggy-mountains-landscape_1204-511.jpg",
      title: "tonne",
      category: "milk",
    },
    {
      image:
        "https://image.freepik.com/free-photo/river-foggy-mountains-landscape_1204-511.jpg",
      title: "tonne",
      category: "milk",
    },
    {
      image:
        "https://image.freepik.com/free-photo/river-foggy-mountains-landscape_1204-511.jpg",
      title: "Image 5",
      category: "lala",
    },
  ];
  render() {
    return (
      <div className="root">
        <h1>New Feed</h1>

        <Grid container spacing={1} direction="column" alignItems="center">
          {this.cards.map((card) => {
            const { image, title, category } = card;
            return (
              <Grid item>
                <Card sx={{ minWidth: 768 }}>
                  <CardMedia
                    component="img"
                    height="140"
                    image={image}
                    alt="green iguana"
                  />
                  <CardContent>
                    <Typography gutterBottom variant="h5" component="div">
                      {title}
                    </Typography>

                    <Typography variant="body2" color="text.secondary">
                      {category}
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
