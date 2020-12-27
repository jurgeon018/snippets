var React = require('react');


class App12 extends React.Component{
    constructor(props){
        super(props);
        var name = props.name;
        var nameIsValid = this.validateName(name);
        var age = props.age;
        var ageIsValid = this.validateAge(age)
        this.state = {name: name, age:age, nameValid:nameIsValid, ageValid:ageIsValid}
        
        this.onNameChange = this.onNameChange.bind(this);
        this.onAgeChange = this.onAgeChange.bind(this);
        this.handleSubmit =this.handleSubmit.bind(this);
    }
    validateAge(age){
        return age>=0;
    }
    validateName(name){
        return name.length>2;
    }
    onAgeChange(e){
        var val = e.target.value;
        console.log(val);
        var valid = this.validateAge(val);
        this.setState({age:val, ageValid:valid})
    }
    onNameChange(e){
        var val = e.target.value;
        console.log(val);
        var valid = this.validateName(val);
        this.setState({name:val, nameValid:valid});
    }
    handleSubmit(e){
        e.preventDefault()
        if(this.state.nameValid === true && this.state.ageValid === true){
            alert('Name: ' + this.state.name + ' Age: '+ this.state.age)
        }
    }
    render(){
        var nameColor = this.state.nameValid===true?"green":"red";
        var ageColor = this.state.ageValid===true?"green":"red";
        return(
            <form onSubmit={this.handleSubmit}>
                <h2>App12</h2>
                <p>
                    <label>Name: </label><br/>
                    <input type="text" value={this.state.name} 
                    onChange={this.onNameChange} style={{borderColor:nameColor}} />
                </p>
                <p>
                    <label>Age: </label><br/>
                    <input onChange={this.onAgeChange} style={{borderColor:ageColor}} type="number" value={this.state.age}/>
                </p>
                <input type="submit" value="Send"/>
            </form>
        )
    }
}

module.exports = App12;