import React, { Component, Fragment } from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import PropTypes from 'prop-types';
import uuid from 'uuid';
import './App.css';
import axios from 'axios';
// var axios = require('axios')

const headerStyle = {
  background:'#333',
  color: '#fff',
  textAlign:'center',
  padding:'10px'
}
const linkStyle = {
  color: '#fff',
  textDecoration: 'none',
}
function Header() {
  return (
      <header style={headerStyle}>
          <h1>TodoList</h1>
          <Link style={linkStyle} to="/" >Home</Link> | 
          <Link style={linkStyle} to="/about" >About</Link>
      </header>
  )
}

class App extends Component {
  state = {
    todos_old: [
      {
        // id: 1,
        id: uuid.v4(),
        title: 'Take out the thash',
        completed: false
      },
      {
        // id: 2,
        id: uuid.v4(),
        title: 'Dinner with wife',
        completed: false
      },
      {
        // id: 3,
        id: uuid.v4(),
        title: 'Meeting with boss',
        completed: false
      }
    ],
    todos: [

    ]
  }
  componentDidMount(){
    axios.get('https://jsonplaceholder.typicode.com/todos?_limit=10')
      // .then(res => console.log(res.data))
      .then(res => this.setState({todos:res.data}))
  }
  // Toggle Complete
  markComplete = (id) => {    
    console.log(id)
    this.setState(  
      {
        todos: this.state.todos.map(
          todo => {
            if(todo.id === id){
              todo.completed = !todo.completed
            }
            return todo;
          }
        ) 
      }
    )
  }
  // Delete Todo
  delTodo = (id) => {
    console.log(id)
    axios.delete(`https://jsonplaceholder.typicode.com/todos/${id}`)
      .then(res => this.setState(
                    {
                      todos: 
                      [
                        ...this.state.todos.filter
                          (todo => todo.id !== id)
                      ]
                    }
                  )
                );
    // this.setState(
    //   {
    //     todos: 
    //     [
    //       ...this.state.todos.filter(
    //         todo => todo.id !== id
    //       )
    //     ]
    //   }
    // )
  }
  // Add Todo
  addTodo = (title) => {
    console.log(title);
    // const newTodo = {
    //   // id: 4,
    //   id: uuid.v4(),
    //   title: title,
    //   completed: false,
    // }
    // this.setState({todos: [...this.state.todos, newTodo]})
    axios.post('https://jsonplaceholder.typicode.com/todos',
    {
      title:title,
      completed:false
    })
      .then(res => this.setState({todos:[...this.state.todos, res.data] }));
  }
  render(){
    return(
    <Router>
      <div className="App">
        <div className="container">
          <Header/>
          <Route exact path="/" render={props => (
            <React.Fragment>
              <AddTodo addTodo={this.addTodo}/>
              <Todos 
                todos={this.state.todos} 
                markComplete={this.markComplete}
                delTodo={this.delTodo}/>
            </React.Fragment>
          )} />
          <Route path="/about" component={About}/>
        </div>
      </div>
    </Router>
    );
  }
}

export class AddTodo extends Component {
  state = {
      title:''
  }
  onSubmit = (e) => {
      e.preventDefault();
      this.props.addTodo(this.state.title);
      this.setState({title:''})
  }
  //onChange = (e) => this.setState({title:e.target.value});
  onChange = (e) => this.setState({[e.target.name]:e.target.value});
  // e.target.name == <input name='title'> == 'title' == App.js.state.todos.titles
  render() {
      return (
          <form onSubmit={this.onSubmit} style={{display:'flex'}}>
              <input 
                type="text" 
                name="title" 
                placeholder="Add Todo..."
                style={{flex:'10', padding:'5px'}}
                value={this.state.title}
                onChange={this.onChange}
              /> 
              <input 
                type="submit" 
                value="Submit" 
                className="btn"
                style={{flex:'1'}}
              />
          </form>
      )
  }
}
class Todos extends Component {
  render() {
    return (
      this.props.todos.map((todo) => (
        <TodoItem
          key={todo.id}
          todo={todo}
          markComplete={this.props.markComplete}
          delTodo={this.props.delTodo}></TodoItem>
      ))
    )
  }
}
const btnStyle = {
  background: '#ff0000',
  color: '#fff',
  border: 'none',
  padding: '5px 8px',
  borderRadius: '50%',
  cursor: 'pointer',
  float: 'right',
}
class TodoItem extends Component {
  getStyle = () => {
    return {
      background: 'grey',
      textDecoration: this.props.todo.completed === true ? 'line-through' : 'none',
      padding: '10px',
      borderBottom: '1px #ccc dotted'
    }
  }
  render() {
    const { id, title } = this.props.todo;
    return (
      <div style={this.getStyle()}>
        <p>
          <input type="checkbox" onChange={this.props.markComplete.bind(this, id)} /> {' '}
          {title}
          <button onClick={this.props.delTodo.bind(this, id)} style={btnStyle}>x</button>
        </p>
      </div>
    )
  }
}

// PropTypes
AddTodo.propTypes = {
  addTodo: PropTypes.func.isRequired,
  markComplete: PropTypes.func.isRequired,
  delTodo: PropTypes.func.isRequired
}
TodoItem.propTypes = {
  todo: PropTypes.object.isRequired,
  markComplete: PropTypes.func.isRequired,
  delTodo: PropTypes.func.isRequired
}
Todos.propTypes = {
  todos: PropTypes.array.isRequired,
  markComplete: PropTypes.func.isRequired,
  delTodo: PropTypes.func.isRequired
}




function About() {
    return (
        <React.Fragment>
            <h2>About</h2>
            <p>This is the TodoList v1.0.0. Its part of a React Crash Course</p>  
        </React.Fragment>
    )
}

export default App;
