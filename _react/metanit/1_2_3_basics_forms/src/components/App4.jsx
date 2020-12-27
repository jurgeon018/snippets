var React = require('react');

//////////// 2_4, 2_5, 2_6
class App4 extends React.Component{
    constructor(props){
        super(props);
        this.state = {welcome: 'Добро пожаловать на сайт!'}
    }
    render(){
        return(
            <div>
                <h2>App4</h2>
                <h1>{this.state.welcome}</h1>
            </div>
        )
    }
};

module.exports = App4;