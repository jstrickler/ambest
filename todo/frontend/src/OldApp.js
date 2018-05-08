import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

const todo_list = [
  {
    'id': 1,
    'title': '1st Item',
    'description': 'Description here.'
  },
  {
    'id': 2,
    'title': '2nd Item',
    'description': 'Another description here.'
  },
  {
    'id': 3,
    'title': '3rd Item',
    'description': 'Third description here.'
  }
];

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { todo_list };
  }

  render() {
    return (
      <div>
        {this.state.todo_list.map(item => (
          <div>
            <h1>{item.title}</h1>
            <span>{item.description}</span>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
