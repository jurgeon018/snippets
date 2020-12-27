var React = require('react'); 
var SearchPlugin = require('./SearchPlugin.jsx');
var Item = require('./Item.jsx');
//////////// 2_8_4

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
        <h2>App10</h2>
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

module.exports = App10;