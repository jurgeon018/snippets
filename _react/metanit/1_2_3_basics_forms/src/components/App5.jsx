var React = require('react');

class App5 extends React.Component{
    constructor(props){
        super(props);
        this.state = {class:"off", label:"Нажми"};
        // Главная сложность, которая может возникнуть при использовании событий, это работа с ключевым словом this, которое указывает на текущий объект, в данном случае компонент. 
        // По умолчанию в функцию обработчика не передается текущий объект, поэтому this будет иметь значение undefined. 
        // И ни к каким свойствам и методам компонента через this мы обратиться не сможем. 
        // И чтобы в метод press корректно передавалась ссылка на текущий объект через this, в конструкторе класса прописывается вызов:
        this.press = this.press.bind(this);
    }
    // React использует концепцию SyntheticEvent - специальных объектов, которые представляют собой обертки для объектов событий, передаваемых в функцию события. 
    // И используя такой объект, мы можем получить в обработчике события всю информацию о событии.
    press(event){
        let className = (this.state.class==="off")?"on":"off"
        this.setState({class:className});
        console.log(event) 
        // event - необязательный аргумент, можно и не передавать.
        console.log('Constructor');
    }
    componentWillMount(){
        console.log('componentWillMount()');
    }
    componentDidMount(){
        console.log('componentDidMount()');
    }
    componentWillUpdate(){
        console.log('componentWillUpdate()');
    }
    componentDidUpdate(){
        console.log('componentDidUpdate()');
    }
    componentWillReveiveProps(nextProps){
        console.log('componentWillReceiveProps()');
    }
    componentWillUnmount(){
        console.log('componentWillUnmount()');
    }
    shouldComponenUpdate(){
        console.log('shouldComponenUpdate()');
    }
    render(){
        return(
            <div>
                <h2>App5</h2>
                <button onClick={this.press} className={this.state.class}>
                {this.state.label}({this.state.class})
            </button>
            </div>
            
        )
    }
};



module.exports = App5;