import React, { Component } from 'react';
import { styled, alpha } from "@mui/material/styles";
import Paper from "@mui/material/Paper";
import InputBase from "@mui/material/InputBase";
import Divider from "@mui/material/Divider";
import IconButton from "@mui/material/IconButton";
import SearchIcon from "@mui/icons-material/Search";
import Box from "@mui/material/Box";
import Container from '@mui/material/Container';


const URL_BASE = "http://0.0.0.0:1234";
class Search extends Component {
	constructor(props) {
		super(props);
		this.state = {
			toSearch: 'search',
			description: '<h1>dsaf</h1>',
		};
		this.searchSubmit = this.searchSubmit.bind(this);
	}
	searchSubmit(event) {
		event.preventDefault();
		const data = new FormData(event.currentTarget);
		console.log(data.get("search_text"))
		let searchData = {
			"text": data.get("search_text"),
		}
		const requestOptions = {
			method: "POST",
			headers: { "Content-Type": "application/json" },
			body: JSON.stringify(searchData),
		};

		const res = fetch(`${URL_BASE}/v1/api/search`, requestOptions)
			.then((response) => response.json())
			.then((data) => {
				console.log("data", data);
				this.setState({description: data})
			});
	}

	render() {
		return (
			<Container maxWidth="sm">
				<Paper
					component="form"
					onSubmit={this.searchSubmit}
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
				<div dangerouslySetInnerHTML={{ __html: this.state.description }} />
			</Container>
		);
	};
};

export default Search;
