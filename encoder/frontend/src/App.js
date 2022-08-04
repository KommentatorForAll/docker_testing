import './App.css';
import React, { Component } from 'react';

class EncoderArea extends Component {
  constructor() {
    super();
    this.type = "string";
    this.state = {
      name: "React"
    }
    this.textAreaId = this.type+"_txtar";
  }

  handleChange(event) {
    
  }

  buttonClicked() {
    const message = document.getElementById(this.textAreaId).value
    fetch("http://localhost:8000/encoders/encode/", {
      method: "POST",
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        "type": this.type,
        "message": message
      })
    }).then(response => {alert("got response"); return response.json();})
    .catch(err => {alert(err); throw err;})
    .then(response => alert(response))
  }

  render() {
    return (
      <div>
        <label> {this.type}</label>
        <br/>
        <textarea
          id={this.type+"_txtar"}
          onChange={this.handleChange}
          rows={5}
          cols={20}
        />
        <br/>
        <button onClick={this.buttonClicked}>convert!</button>
      </div>
    )
  }
}

export default EncoderArea