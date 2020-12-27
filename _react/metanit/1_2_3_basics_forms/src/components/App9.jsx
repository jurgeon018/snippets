var React = require('react');
var Item = require('./Item.jsx');

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
                <h2>App9</h2>   
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

module.exports = App9;


