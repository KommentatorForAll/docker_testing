import './App.css';
import React, { Component } from 'react';
import {handleRequest} from './apiFunctions';

export const opts = {
  audience: process.env.REACT_APP_API_URL,
  scope: 'read:everything',
};

function EncoderArea (props) {

  const [state, setState] = React.useState();
  /*
  constructor() {
    super();
    this.state = {
      type: "hex",
      message: ""
    }
    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }
  */

  const handleChange = (event) => {
    setState({ message: event.target.value });
  };

  const handleSubmit = () => {
    //handleRequest("/encoders/list", "GET", {}, (res) => console.log(res), () => {console.log("error in get")});
    console.log("doing request");
    const path = "/";
    const method = "GET";
    const body = { blu: "blob" }; 
    console.log(body); 
    const onOK = () => { console.log("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"); }; 
    const onERROR = () => { }; 
    handleRequest(path, method, body, onOK, onERROR);
    //useApi("/encoders/list");
  };

  return (
      <div>
        <form onSubmit={handleSubmit}>
          <label>
            <textarea
              onChange={handleChange}
              rows={5}
              cols={20}
            /></label>
          <input type="submit" value="convert!" />
        </form>
      </div>
    );
}

export default EncoderArea;