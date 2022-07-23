import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import Navbar from "./components/Navbar";
import Test from "./pages/Test";
import Home from "./pages/Home";
import SignIn from "./pages/SignIn";
import SignUp from "./pages/SignUp";
import Search from "./pages/Search";
import TinyURL from "./pages/TinyURL";
import Blog from "./pages/Blog";
import BlogWrite from "./pages/blogs/Write";
import Youtube from "./pages/Youtube";
import Chat from "./pages/Chat";
import About from "./pages/About";
import FooterCpt from "./components/Footer";
import EcomHome from "./pages/ecom/EcomHome"; 
import AddProduct from "./pages/ecom/AddProduct";


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
                  <Route path="/signin/signup" element={<SignUp />}></Route>
                  <Route path="/search" element={<Search />}></Route>
                  <Route path="/test" element={<Test />}></Route>
                  <Route path="/tinyurl" element={<TinyURL />}></Route>
                  <Route path="/blog" element={<Blog />}></Route>
                  <Route path="/blog/write" element={<BlogWrite />}></Route>
                  <Route path="/youtube" element={<Youtube />}></Route>
                  <Route path="/chat" element={<Chat />}></Route>
                  <Route path="/about" element={<About />}></Route>
                  <Route path="/ecom" element={<EcomHome />}></Route>
                  <Route path="/ecom/addproduct" element={<AddProduct />}></Route>

                </Routes>
              </Content>
              <Footer>
                <FooterCpt />
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
