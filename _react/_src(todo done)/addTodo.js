import React, {Component, Fragment} from 'react'



class App extends Component{
  state = {
    todos:[
      {id:1,title:'title1',completed:false},
      {id:2,title:'title2',completed:false},
      {id:3,title:'title3',completed:false}
    ]
  }  
  addTodo = (title) => {
    const id = this.state.todos[this.state.todos.length-1].id
    const newTodo = {
      id:id+1,
      title: title,
      completed:false
    }
    // при каждом добавлении нового элемента все старые удаляются, и остается один новый
    // this.setState({todos:[newTodo]}) 
    // при каждом добавлении нового элемента старые остаются
    this.setState({todos:[...this.state.todos, newTodo]}) 
    // todos - список. ...this.state.todos - содержит в себе все старые элементы
    // newTodo - новый элемент, который добавляется в конец либо в начало
  }
  // при нажатии на button в компоненте TodoItem
  delTodo = (id) => {
    this.setState({todos: [...this.state.todos.filter(
      function(todo){return todo.id !== id}
    )]})
  }
  render(){
    return(
      <div>
        <AddTodo addTodo={this.addTodo} />
        <Todos delTodo={this.delTodo} todos={this.state.todos}/>
      </div>
    )
  }
}

class AddTodo extends Component{
  state = {
    title:''
  }
  onSubmit = (e) => {
    e.preventDefault()
    this.props.addTodo(this.state.title);
    this.setState({title:''})
    
  }
  onChange = (e) => {
    console.log(e.target.value)
    this.setState({title:e.target.value})
  }
  render(){
    return(
      <form onSubmit={this.onSubmit}>
        <input 
          onChange={this.onChange} 
          value={this.state.title}
          type="text" />
        <input 
          value="Add Todo"
          type="submit"/>
      </form>
    )
  }
}
class Todos extends Component{
  render(){
    return(
      this.props.todos.map( (todo) => 
        <TodoItem delTodo={this.props.delTodo} todo={todo}/>
      )
    )
  }
}

class TodoItem extends Component{
  render(){
    return(
      <div>
        {this.props.todo.title}
        <button 
          onClick={this.props.delTodo.bind(this, this.props.todo.id)}
          >X</button>
      </div>
    )
  }
}
export default App;