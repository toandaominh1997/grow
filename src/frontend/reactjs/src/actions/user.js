const URL_BASE = "http://0.0.0.0:8001";

export const loginUser = (userObj) => ({
  type: "LOGIN_USER",
  payload: userObj,
});

export const userPostFetch = (user) => {
  return dispatch => {
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({user}),
    };
    const res = fetch(`${URL_BASE}/v1/api/user`, requestOptions)
      .then((response) => response.json())
      .then((data) => {
        console.log("data", data);
        localStorage.setItem("token", data.jwt);
        dispatch(loginUser(data.user));
      });
    return res 
  };
};
