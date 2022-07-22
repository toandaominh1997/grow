import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import Navbar from "./components/Navbar";
import Test from "./pages/Test";
import Home from "./pages/Home";
import SignIn from "./pages/SignIn";
import Search from "./pages/Search";
import TinyURL from "./pages/TinyURL";
import Blog from "./pages/Blog";
import Youtube from "./pages/Youtube";
import Chat from "./pages/Chat";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Grid from "@mui/material/Grid";
import { Layout } from "antd";
import { loginUser } from "./actions/user";
import { connect } from "react-redux";

const { Header, Footer, Sider, Content } = Layout;

class App extends Component {
  constructor(props) {
    super(props);
  }
  componentDidMount() {
    if (localStorage.getItem("token") != null) {
      this.props.loginUser({ token: localStorage.getItem("token") });
    }
  }
  render() {
    return (
      <div className="container">
        <Layout>
          <Router>
            <Sider width={200}>
              <Navbar />
            </Sider>
            <Layout>
              <Header>Header</Header>
              <Content>
                <Routes>
                  <Route extra path="/" element={<Home />}></Route>
                  <Route path="/signin" element={<SignIn />}></Route>
                  <Route path="/search" element={<Search />}></Route>
                  <Route path="/test" element={<Test />}></Route>
                  <Route path="/tinyurl" element={<TinyURL />}></Route>
                  <Route path="/blog" element={<Blog />}></Route>
                  <Route path="/youtube" element={<Youtube />}></Route>
                  <Route path="/chat" element={<Chat />}></Route>
                </Routes>
              </Content>
              <Footer>
                <small>
                  made by <a href="https://twitter.com/krzysu">Henry</a>, source
                  code available on{" "}
                  <a href="https://github.com/krzysu/reactjs-shopping-cart">
                    github
                  </a>
                </small>
              </Footer>
            </Layout>
          </Router>
        </Layout>
      </div>
    );
  }
}

const mapDispatchToProps = (dispatch) => ({
  loginUser: (user) => dispatch(loginUser(user)),
});
export default connect(null, mapDispatchToProps)(App);
