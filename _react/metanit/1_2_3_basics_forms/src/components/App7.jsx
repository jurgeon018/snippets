var React = require('react');
var Item = require('./Item.jsx')
//////////// 2_8_1

class App7 extends React.Component{
    render(){
        return(
          <div>
            <h2>App7</h2>
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

module.exports = App7;



