import React, { Component, useState, createContext, useContext } from "react";
import "./TinyURL.css";
import { Input, Button, Form } from "antd";
import { Col, Row } from "antd";
import { Select } from "antd";
const { Option } = Select;

const URLContext = createContext();

const URL_BASE = "http://0.0.0.0:8001";
const handleChange = (value) => {
  console.log(`selected ${value}`);
};

class TinyURL extends Component {
  constructor(props) {
    super(props);
    this.state = {
      tinyurl: "not found",
    };
    this.makeTinyURL = this.makeTinyURL.bind(this);
  }
  makeTinyURL(values){
    console.log(values.long_url, values.alias);
    let urlData = {
      long_url: values.long_url,
      domain: URL_BASE,
      alias: values.alias,
    };
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(urlData),
    };
    const res = fetch(`${URL_BASE}/v1/api/update_tinyurl`, requestOptions)
      .then((response) => response.json())
      .then((data) => {
        console.log("setTinyURL", data);
        this.setState({ tinyurl: data });
      });
  };

  render() {
    return (
      <div>
        <Form name="tinyurl" onFinish={(values) => this.makeTinyURL(values)}>
          <Form.Item label="URL" name="long_url">
            <Input size="large" />
          </Form.Item>
          <Form.Item label="Alias" name="alias">
            <Input size="large" />
          </Form.Item>
          <Form.Item>
            <Button size="large" type="primary" htmlType="submit">
              MakeTinyURL
            </Button>
          </Form.Item>
        </Form>
        <h2>{this.state.tinyurl}</h2>
		<a href={this.state.tinyurl}>tinyurl</a>
      </div>
      // 	<div>
      //   <Form name="tinyurl" onFinish={(values) => this.makeTinyURL(values)}>
      //     <Form.Item label="URL" name = "long_url">
      //       <Input size="large"/>
      //     </Form.Item>
      // 	<Form.Item label="Alias" name = "alias">
      //       <Input size="large"/>
      //     </Form.Item>
      //     <Form.Item>
      //       <Button size="large" type="primary" htmlType="submit">
      //         MakeTinyURL
      //       </Button>
      //     </Form.Item>
      // 	</Form>
      // 	</div>
    );
  }
}
export default TinyURL;
