var React = require('react');
var Item = require('./Item.jsx')
//////////// 2_8_2

class App8 extends React.Component{
    render(){
        return(
          <div>
            <h2>App8</h2>
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




module.exports = App8;
