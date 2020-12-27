import React, {Component, Fragment} from 'react';
import {BrowserRouter as Router, Route, Link} from 'react-router-dom'

class App extends Component{
  // список заданий
  state = {
    todos:[
      {id:1,title:'title1',completed:false},
      {id:2,title:'title2',completed:false},
      {id:3,title:'title3',completed:false}
    ]
  }
  // Путь markComplete: App -> Main -> Todos -> TodoItem. 
  // Арр: метод класса, у которого есть доступ к состоянию списка заданий. 
  // Main: транзит от Todos
  // Todos(список элементов): транзит от TodoItem
  // TodoItem(отдельный элемент): через onChange передает изменение состояния поля completed отдельного checkbox-элемента на который нажали, и его id.
  // функция markComplete имеет доступ к id измененного элемента, проходится в цикле по всем элементам списка заданий, проверяет по id, и изменяет поле complete нужного элемента на противоположное
  // У TodoItem'a есть доступ к отдельному элементу и его полям(в том числе completed). Если поле сcompleted после срабатывания функции markComplete true - то в стилях textDecoration:'line-through', иначе - none

  markComplete(id){
    this.setState({todos: this.state.todos.map(todo=>{
      if(todo.id===id){
        todo.completed = !todo.completed
      }
      return todo;
    })})
  }
  render(){
    return(
      <Main 
        todos={this.state.todos}
        markComplete={this.markComplete.bind(this)}
      ></Main>
    )
  }
}
class Main extends Component{
  render(){
    return(
      <Fragment>
        <Todos 
        todos={this.props.todos}
        // транзит
        markComplete={this.props.markComplete.bind(this)}
        />
      </Fragment>
    )
  }
}
class Todos extends Component{
  render(){
    return(
      this.props.todos.map(todo => 
      <TodoItem 
      todo={todo}
      // транзит
      markComplete={this.props.markComplete.bind(this)}
      />
      )
    )
  }
}
class TodoItem extends Component{
  getStyle = () => {
    return {
      textDecoration: this.props.todo.completed === true?'line-through':'none'
    }
  }

  render(){
    return(
      <div style={this.getStyle()}>
        <input
          type="checkbox"

          onChange={this.props.markComplete.bind(this, this.props.todo.id)}
          />
        {this.props.todo.title}
      </div>
    )
  }
}
export default App;