import React, { Component } from 'react';

import { useSelector, useDispatch } from "react-redux";
import { increment, decrement } from "./../actions/counter";
import { userPostFetch, loginUser} from "./../actions/user";

const URL_BASE = "http://0.0.0.0:8001";

function Test(){
	const counter = useSelector((state) => state.counter);
	const user = useSelector((state) => state.user);
	const dispatch = useDispatch();
	function postUser(user) {
		const requestOptions = {
		method: "POST",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify(user)
		};
		const res = fetch(`${URL_BASE}/v1/api/user`, requestOptions)
		.then((response) => {if(response.ok) return response.json()})
		.then((data) => {
			console.log("data", data);
			localStorage.setItem("token", data.jwt);
			dispatch(loginUser({"token": data.jwt}));
		});
	}
	return(
		<div>
			<h1>Test Ne</h1>
			<h1>Counter {counter}</h1>
			<h1> User {user.token}</h1>

      <button onClick={() => dispatch(increment(5))}>Increment</button>
      <button onClick={() => dispatch(decrement(5))}>Decrement</button>

	  {/* <button onClick={() => postUser({"email": "admin", "password": "admin"})}>Login</button> */}
		</div>
	)
}

export default Test;