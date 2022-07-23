import React, { Component } from "react";
import ReactDOM from "react-dom";
import { Editor, EditorState, RichUtils } from "draft-js";
import ReactMarkdown from 'react-markdown'
const styles = {
  editor: {
    border: "1px solid blue",
    minHeight: "6em",
    cursor: "text",
    background: "#fefefe"
  },
};
class BlogWrite extends Component {
  constructor(props) {
    super(props);
  }


  render() {
    return (
      <div>
        <ReactMarkdown># Hello, *world*!</ReactMarkdown>

      </div>
    );
  }
}

export default BlogWrite;
