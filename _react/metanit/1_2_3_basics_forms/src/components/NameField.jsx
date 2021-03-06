var React = require('react');


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


module.exports = NameField;