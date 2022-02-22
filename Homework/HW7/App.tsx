import React from 'react';
import './App.css';
import ToDoPanel from './ToDoPanel'

/**
 * Sean Nishi
 * Homework 7 12/16/2021
 * Creating a To Do list using React typescript similar to https://ragged-cattle.surge.sh/
 * Initial code is from https://github.com/ecerami/oopl/tree/main/react/react-state4/src
 */

class App extends React.Component {
  
  render(): JSX.Element{
    return (
      <div>
        <ToDoPanel />
      </div>
    );
  }
  
}

export default App;
