var React = require('react');
var ReactDOM = require('react-dom');
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';


var App1 = require('./components/App1.jsx');
var App2 = require('./components/App2.jsx');
var App3 = require('./components/App3.jsx');
var App4 = require('./components/App4.jsx');
var App5 = require('./components/App5.jsx');
var App6 = require('./components/App6.jsx');
var App7 = require('./components/App7.jsx');
var App8 = require('./components/App8.jsx');
var App9 = require('./components/App9.jsx');
var App10 = require('./components/App10.jsx');
var App11 = require('./components/App11.jsx');
var App12 = require('./components/App12.jsx');
var App13 = require('./components/App13.jsx');


ReactDOM.render(
    <App1 name="Tom" age="22"></App1>,
    document.getElementById('app1'),
    function(){
        console.log('Вызов опциональной функции после рендеринга элемента app1')
    }
);

ReactDOM.render(
    <App2></App2>,
    document.getElementById('app2'),
);
ReactDOM.render(
    <App3></App3>,
    document.getElementById('app3')
);
ReactDOM.render(
    <App4></App4>,
    document.getElementById('app4')
);
ReactDOM.render(
    <App5></App5>,
    document.getElementById('app5')
)
ReactDOM.render(
    <App6></App6>,
    document.getElementById('app6')
)
ReactDOM.render(
    <App7 title="Items list:"></App7>,
    document.getElementById('app7')
)

const propsValues = {
    title: "Список смартфонов",
    items:[
          "HTC U Ultra", 
          "iPhone 7", 
          "Google Pixel", 
          "Hawei P9", 
          "Meizu Pro 6", 
          "Asus Zenfone 3"
    ]
  };
ReactDOM.render(
    <App8 data={propsValues}></App8>,
    document.getElementById('app8')
)
ReactDOM.render(
    <App9 data={propsValues}></App9>,
    document.getElementById('app9')
)
ReactDOM.render(
    <App10 data={propsValues}></App10>,
    document.getElementById('app10')
)
//////////// 3_1
ReactDOM.render(
    <App11></App11>,
    document.getElementById('app11'),
)
//////////// 3_2
ReactDOM.render(
    <App12 name="" age=""></App12>,
    document.getElementById('app12')
)
//////////// 3_3
ReactDOM.render(
    <App13 />,
    document.getElementById("app13")
)






