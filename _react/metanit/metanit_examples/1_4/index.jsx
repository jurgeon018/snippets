const user = {
        id: 5,
        age: 33,
        firstName: 'Tom', 
        lastName: 'Smith', 
        getFullName: function(){
            return `${this.firstName} ${this.lastName}`;
        },
    };

    const userClassName = 'user-info';

    const styleObj = {
        color:'red',
        fontFamily:'Verdana'
    };
    
class Hello extends React.Component {
    render() {
        return <div class={userClassName} style={styleObj}>
            Hello react   
            <p>id: {user.id}</p>   
            <p>Полное имя: {user.getFullName()}</p>
            <p>Возраст: {user.age}</p>
            <p>Время генерации данных: {new Date().toLocaleTimeString()}</p>
        </div>
    }
}

ReactDOM.render(
        <Hello></Hello>,
        document.getElementById('app')
    )