var React = require('react');

const user = {
    id: 5,
    firstName:"Andrew",
    lastName:"Mendela",
    age:"21",
    getFullName:function(){
        {/* return `${this.firstName} ${this.lastName}` */}
        return this.firstName + ' ' + this.lastName
    }
}
const styleObj = {
    color:'red',
    fontFamily:'Verdana',
};
const userClassName = 'user-info'
class App1 extends React.Component{
    render(){ 
        return(
            <div>
            <h2>App1</h2>
            <div className={userClassName} style={styleObj}>
                <p>User.id: {user.id}</p>
                <p>user.firstName: {user.firstName}</p>
                <p>user.lastName{user.lastName}</p>
                <p>user.age{user.age}</p>
                <p>user.getFullName(): {user.getFullName()}</p>
                <p>this.props.name: {this.props.name} - argument</p>
                <p>this.props.age: {this.props.age} - argument</p>
                <p>this.props.job: {this.props.job} - default agrument</p>
                <p>this.props.name = "alex"</p> {/*Не сработает! props - только для чтения */}
            </div>
            </div>
        )
    }
}   
App1.defaultProps = {job:"developer"};
module.exports = App1;

