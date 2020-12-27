var React = require("react");
var Reflux = require("reflux");
var Actions = require("./actions.jsx");
var PhonesStore = require("./phonestore.jsx");
 
class PhonesList extends Reflux.Component{
 
    constructor(props){
        super(props);
        this.state = {newItem: ""};
        this.store = PhonesStore;
         
        this.onInputChange = this.onInputChange.bind(this);
        this.onClick = this.onClick.bind(this);
    }
    onInputChange(e){
        this.setState({newItem:e.target.value});
    }
    onClick(e){
        if(this.state.newItem){
            Actions.addItem(this.state.newItem);
            this.setState({newItem:" "});
        }
    }
    onRemove(item){
        if(item){
            Actions.removeItem(item);
        }
    }
    render(){
         
        var remove = this.onRemove;
        return <div> 
                <input type="text" value={this.state.newItem} onChange={this.onInputChange} />    
                <button onClick={this.onClick}>Добавить</button>                
                <h2>Список смартфонов</h2>
                <div>
                    {
                        this.state.phones.map(function(item){
                             
                            return <Phone key={item} text={item} onRemove={remove} />
                        })
                    }
                </div>
            </div>;
    }
}
 
class Phone extends React.Component{
 
    constructor(props){
        super(props);
        this.state = {text: props.text};
        this.onClick = this.onClick.bind(this);
    }
    onClick(e){
        this.props.onRemove(this.state.text);
    }
    render(){
        return <div> 
                <p>
                    <b>{this.state.text}</b><br />
                    <button onClick={this.onClick}>Удалить</button> 
                </p>
            </div>;
    }
}
 
module.exports = PhonesList;