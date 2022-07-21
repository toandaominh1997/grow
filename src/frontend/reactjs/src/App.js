import logo from "./logo.svg";
import "./App.css";
import Navbar from "./components/Navbar";
import Test from "./pages/Home";
import Home from "./pages/Home";
import SignIn from "./pages/Search";
import Search from "./pages/Search";
import TinyURL from "./components/TinyURL";
import Blog from "./pages/Blog";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Grid from "@mui/material/Grid";
import { Layout } from "antd";

const { Header, Footer, Sider, Content } = Layout;

function App() {
  return (
    <div className="container">
      <Layout>
        <Router>
          <Sider>
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

export default App;
