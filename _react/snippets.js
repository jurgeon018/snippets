
<div id="app"></div>
<script crossorigin src="https://unpkg.com/react@16/umd/react.production.min.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@16/umd/react-dom.production.min.js"></script>
<!-- // babel cdn подключается для компиляции JSX в JS -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/6.25.0/babel.min.js"></script>
<!-- // модуль для работы с маршрутизацией -->
<script src="https://unpkg.com/react-router-dom/umd/react-router-dom.min.js"></script>
<script type="text/babel" src="index.jsx">
</script>
         





package.json - файл, в котором нужно описать конфигурации проекта
npm install - команда, которая устанавливает необходимые зависимости в папку node_modules. Запускать после того,как был создан package.json
node_modules/.bin/babel index.jsx --out-file app.js - команда, которая компилирует jsx в js при помощи компилятора Babel. После компиляции можно запускать файл напрямую в браузере, без веб-сервера.


npm run start - запускает сервер
npm run build - создает билд
npm run dev - запускает dev-сервер



<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/6.25.0/babel.min.js"></script>
<!-- // babel cdn подключается для компиляции JSX в JS. 
     // не нужен, если скомпилировать вручную 
     // node_modules/.bin/babel index.jsx --out-file app.js
-->
<script src="app.js">
</script>



Через функции
function Hello(props){
    return <div>
        <p>Name: {props.name}</p>
        <p>Age: {props.age}</p>
    </div>
}
Через стрелочные функции
    const Hello = (props) => {
        const {name, age} = props;
    return(<div>
        <p>Name: {name}</p>
        <p>Age: {age}</p>
    </div>)
}
Через классы
class Hello extends React.Component {
    render() {
        return <div>
                    <p>Имя: {this.props.name}</p>
                    <p>Возраст: {this.props.age}</p>
                </div>;
        }
    }

this.props.someArg - агрументы, передаваемые в функцию извне
return(
  this.props.todos.map(todo => <p>{todo.title}</p>)
  // переменную нужно оборачивать в {} только если она находится внутри html-тегов
  this.props.todos.map(todo => todo.title)
)





import { connect } from 'react-redux';
or
var connect = require("react-redux").connect;
одно и то же







Почему стрелочные функции лучше обычных?

export class TodoItem extends Component {
  markComplete(e) {
    console.log(this.props)
  }

  render() {
    return (<div>
      <input type="checkbox" onChange={this.markComplete} /> 
      // Сработает со стрелочной фунцией без использование .bind(this)
      <input type="checkbox" onChange={this.markComplete.bind(this)} /> 
      // С обычной функцией сработает только это
    </div>)
  }
}


echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p