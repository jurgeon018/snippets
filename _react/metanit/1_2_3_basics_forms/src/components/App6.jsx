var React = require('react');

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
                <h2>App6</h2>
                <h1>Hello, {this.state.name}</h1>
                <h2>Current time {this.state.date.toLocaleString()}</h2>
            </div>
        )
    }
};


module.exports = App6;