




//////////// 1_1, 1_2, 1_3, 1_4
const user = {
    id: 5,
    firstName:"Andrew",
    lastName:"Mendela",
    age:"21",
    getFullName:function(){
        {/* return `${this.firstName} ${this.lastName}` */}
        return this.firstName + ' ' + this.lastName
    }
}
const styleObj = {
    color:'red',
    fontFamily:'Verdana',
};
const userClassName = 'user-info'
class App1 extends React.Component{
    render(){ 
        return(
            <div className={userClassName} style={styleObj}>
                <p>User.id: {user.id}</p>
                <p>user.firstName: {user.firstName}</p>
                <p>user.lastName{user.lastName}</p>
                <p>user.age{user.age}</p>
                <p>user.getFullName(): {user.getFullName()}</p>
                <p>this.props.name: {this.props.name} - argument</p>
                <p>this.props.age: {this.props.age} - argument</p>
                <p>this.props.job: {this.props.job} - default agrument</p>
                <p>this.props.name = "alex"</p> {/*Не сработает! props - только для чтения */}
            </div>
        )
    }
}   
App1.defaultProps = {job:"developer"};
ReactDOM.render(
    <App1 name="Tom" age="22"></App1>,
    document.getElementById('app1'),
    function(){
        console.log('Вызов опциональной функции после рендеринга элемента app1')
    }
);



//////////// 2_1, 2_2
function tick(){
    ReactDOM.render(
        <div>
            <h2>Текущее время: {new Date().toLocaleTimeString()}</h2>
        </div>,
        document.getElementById('app2')
    )
};
setInterval(tick, 1000); // Через 1 секунду перезаписывает поле app2 с приветствием
class App2 extends React.Component{
    render(){
        return(
            <h2>This component will be rewritten by Ticker after 1 second.</h2>
        )
    }
}
ReactDOM.render(
    <App2></App2>,
    document.getElementById('app2'),
);

class App3 extends React.Component{
    render(){
        return(
            <div id="items">
                <h2>Список телефонов</h2>
                <ul>
                    <li>iPhone 7</li>
                    <li>Samsung Galaxy A5</li>
                    <li>HTC U Ultra</li>
                    <li>Pixel XL</li>
                </ul>
            </div>
        )
    }
}
ReactDOM.render(
    <App3></App3>,
    document.getElementById('app3')
);



//////////// 2_4, 2_5, 2_6
class App4 extends React.Component{
    constructor(props){
        super(props);
        this.state = {welcome: 'Добро пожаловать на сайт!'}
    }
    render(){
        return <h1>{this.state.welcome}</h1>
    }
};
ReactDOM.render(
    <App4></App4>,
    document.getElementById('app4')
)
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
            <button onClick={this.press} className={this.state.class}>
                {this.state.label}({this.state.class})
            </button>
        )
    }
};
ReactDOM.render(
    <App5></App5>,
    document.getElementById('app5')
)




//////////// 2_7
class App6 extends React.Component{
    constructor(props){
        super(props);
        this.state = {date: new Date(), name:'Tom'};
    }
    componentDidMount(){
        this.timerId = setInterval(()=>this.tick(),1000 );
    }  
    componentWillUnmount(){
        clearInterval(this.timerId);
    }
    tick(){
        this.setState({
            date: new Date()
        });
    }
    render(){
        return (
            <div>
                <h1>Hello, {this.state.name}</h1>
                <h2>Current time {this.state.date.toLocaleString()}</h2>
            </div>
        )
    }
};
ReactDOM.render(
    <App6></App6>,
    document.getElementById('app6')
)



//////////// 2_8_1
class Item extends React.Component{
    render(){
        return <li>{this.props.name}</li>;
      }
};
class App7 extends React.Component{
    render(){
        return(
          <div>
            <h2>{this.props.title}</h2>
            <ul>
              <Item name="iPhone 7"></Item>
              <Item name="HTC U Ultra"></Item>
              <Item name="Google Pixel"></Item>
            </ul>
          </div>
        )
      }
};
ReactDOM.render(
    <App7 title="Items list:"></App7>,
    document.getElementById('app7')
)





//////////// 2_8_2
const propsValues = {
      title: "Список смартфонов",
      items:[
            "HTC U Ultra", 
            "iPhone 7", 
            "Google Pixel", 
            "Hawei P9", 
            "Meizu Pro 6", 
            "Asus Zenfone 3"
      ]
    };
class App8 extends React.Component{
    render(){
        return(
          <div>
            <h2>{this.props.data.title}</h2>
            <ul>
            {
              this.props.data.items.map(function(item){
                return <Item key={item} name={item}></Item>
              })
            }
            </ul>
          </div>
        )
      }
    }
ReactDOM.render(
    <App8 data={propsValues}></App8>,
    document.getElementById('app8')
)





//////////// 2_8_3
class App9 extends React.Component{
    constructor(props){
            super(props);
            this.state = { items: this.props.data.items};
                    
            this.filterList = this.filterList.bind(this);
        }
    // фильтрация списка
    filterList(e){
        var filteredList = this.props.data.items.filter(function(item){
            return item.toLowerCase().search(e.target.value.toLowerCase())!== -1;
        });
        // обновление состояния
        this.setState({items: filteredList});
    }
    
    render() {
        return(
            <div>         
                <h2>{this.props.data.title}</h2>
                <input placeholder="Поиск" onChange={this.filterList} />
                <ul>
                    {
                        this.state.items.map(function(item){
                            return <Item key={item} name={item} />
                        })
                    }
                </ul>
            </div>);
    }
}
ReactDOM.render(
    <App9 data={propsValues}></App9>,
    document.getElementById('app9')
)




//////////// 2_8_4
class SearchPlugin extends React.Component{
      constructor(props){
        super(props);
        this.onTextChanged = this.onTextChanged.bind(this);
      }
      onTextChanged(e){
        var text = e.target.value.trim();
        this.props.filter(text);
      }
      render(){
        return <input placeholder="Поиск" onChange={this.onTextChanged}></input>
        
      }
    }
    class App10 extends React.Component{
      constructor(props){
        super(props);
        this.state = {items: this.props.data.items};
        this.filterList = this.filterList.bind(this);
      }
      filterList(text){
        var filteredList = this.props.data.items.filter(function(item){
          return item.toLowerCase().search(text.toLowerCase()) !== -1;
        });
        this.setState({items:filteredList});
      }
      render(){
        return(
          <div>
            <h2>{this.props.data.title}</h2>
            <SearchPlugin filter={this.filterList}></SearchPlugin>
            <ul>
              {
                this.state.items.map(function(item){
                  return <Item key={item} name={item}></Item>
                })
              }
            </ul>
          </div>);
      }
    }
    ReactDOM.render(
      <App10 data={propsValues}></App10>,
      document.getElementById('app10')
    )









//////////// 3_1
class App11 extends React.Component{
        constructor(props) {
            super(props);
            this.state = {name: ""};

            this.onChange = this.onChange.bind(this);
            this.handleSubmit = this.handleSubmit.bind(this);
        }
        onChange(e){
            var val=e.target.value;
            this.setState({name:val});
        }
        handleSubmit(e){
            e.preventDefault();
            alert('Name:' + this.state.name);
        }
        render(){
            return(
                <form onSubmit={this.handleSubmit}>
                    <p>
                        <label>Name:</label><br/>
                        <input type="text" onChange={this.onChange} value={this.state.name}/>
                    </p>
                        <input type="submit" value="Send"/>
                </form>
            )
        }
    }
    ReactDOM.render(
        <App11></App11>,
        document.getElementById('app11'),
    )



//////////// 3_2
class App12 extends React.Component{
    constructor(props){
        super(props);
        var name = props.name;
        var nameIsValid = this.validateName(name);
        var age = props.age;
        var ageIsValid = this.validateAge(age)
        this.state = {name: name, age:age, nameValid:nameIsValid, ageValid:ageIsValid}
        
        this.onNameChange = this.onNameChange.bind(this);
        this.onAgeChange = this.onAgeChange.bind(this);
        this.handleSubmit =this.handleSubmit.bind(this);
    }
    validateAge(age){
        return age>=0;
    }
    validateName(name){
        return name.length>2;
    }
    onAgeChange(e){
        var val = e.target.value;
        console.log(val);
        var valid = this.validateAge(val);
        this.setState({age:val, ageValid:valid})
    }
    onNameChange(e){
        var val = e.target.value;
        console.log(val);
        var valid = this.validateName(val);
        this.setState({name:val, nameValid:valid});
    }
    handleSubmit(e){
        e.preventDefault()
        if(this.state.nameValid === true && this.state.ageValid === true){
            alert('Name: ' + this.state.name + ' Age: '+ this.state.age)
        }
    }
    render(){
        var nameColor = this.state.nameValid===true?"green":"red";
        var ageColor = this.state.ageValid===true?"green":"red";
        return(
            <form onSubmit={this.handleSubmit}>
                <p>
                    <label>Name: </label><br/>
                    <input type="text" value={this.state.name} 
                    onChange={this.onNameChange} style={{borderColor:nameColor}} />
                </p>
                <p>
                    <label>Age: </label><br/>
                    <input onChange={this.onAgeChange} style={{borderColor:ageColor}} type="number" value={this.state.age}/>
                </p>
                <input type="submit" value="Send"/>
            </form>
        )
    }
}
ReactDOM.render(
    <App12 name="" age=""></App12>,
    document.getElementById('app12')
)









//////////// 3_3
class NameField extends React.Component {
    constructor(props) {
        super(props);
        var isValid = this.validate(props.value);
        this.state = {value: props.value, valid: isValid};
        this.onChange = this.onChange.bind(this);
    }
    validate(val){
        return val.length>2;
    }
    onChange(e) {
        var val = e.target.value;
        var isValid = this.validate(val);
        this.setState({value: val, valid: isValid});
    }
    render() {
        var color = this.state.valid===true?"green":"red";
        return <p>
            <label>Имя:</label><br />
            <input type="text" value={this.state.value} onChange={this.onChange} style={{borderColor:color}} />
        </p>;
    }   
}
class AgeField extends React.Component {
    constructor(props) {
        super(props);
        var isValid = this.validate(props.value);
        this.state = {value: props.value, valid: isValid};
        this.onChange = this.onChange.bind(this);
    }
    validate(val){
        return val>=0;
    }
    onChange(e) {
        var val = e.target.value;
        var isValid = this.validate(val);
        this.setState({value: val, valid: isValid});
    }
    render() {
        var color = this.state.valid===true?"green":"red";
        return <p>
            <label>Возраст:</label><br />
            <input type="number" value={this.state.value} onChange={this.onChange} style={{borderColor:color}} />
        </p>;
    }   
}
class App13 extends React.Component {
    constructor(props) {
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    handleSubmit(e) {
        e.preventDefault();
        var name = this.refs.nameField.state.value;
        var age = this.refs.ageField.state.value;
        if(this.refs.nameField.state.valid && this.refs.ageField.state.valid){
            alert("Имя: " + name + " Возраст: " + age);
        }
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
            <NameField value="" ref="nameField" />
            <AgeField value="5" ref="ageField" />
            <input type="submit" value="Отправить" />
        </form>
    );
    }
}
ReactDOM.render(
    <App13 />,
    document.getElementById("app13")
)











