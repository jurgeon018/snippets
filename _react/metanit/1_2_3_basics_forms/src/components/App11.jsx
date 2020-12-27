var React = require('react');


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
                <h2>App11</h2>
                <p>
                    <label>Name:</label><br/>
                    <input type="text" onChange={this.onChange} value={this.state.name}/>
                </p>
                    <input type="submit" value="Send"/>
            </form>
        )
    }
}

module.exports = App11;
