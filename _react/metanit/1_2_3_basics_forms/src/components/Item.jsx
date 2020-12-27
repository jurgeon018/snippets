var React = require('react');

class Item extends React.Component{
    render(){
        return <li>{this.props.name}</li>;
      }
};
module.exports = Item;