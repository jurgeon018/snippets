var NameField = require('./NameField.jsx');
var AgeField = require('./AgeField.jsx');
var React = require('react');


class App13 extends React.Component {
    constructor(props) {
        super(props);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    handleSubmit(e) {
        e.preventDefault();
        var name = this.refs.nameField.state.value;
        var age = this.refs.ageField.state.value;
        if(this.refs.nameField.state.valid && this.refs.ageField.state.valid){
            alert("Имя: " + name + " Возраст: " + age);
        }
    }

    render() {
        return (
        <form onSubmit={this.handleSubmit}>
            <h2>App13</h2>
            <NameField value="" ref="nameField" />
            <AgeField value="10" ref="ageField" />
            <input type="submit" value="Отправить" />
        </form>
    );
    }
}
module.exports = App13;