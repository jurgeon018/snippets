// Описание урока 3
// Аутентификация. На бекенде нужно будет достать токен для юзера, который логинится, сохранить этот токен в браузере. Если токена в браузере нет - то юзер не залогиненый. А если токен есть - то юзер залогиненый. Наворотили кучу говна с redux

// Описание урока 4
// Добавили возможность деплоить на хероку, и запускать фронтенд через джанго-сервер, привязав к списку шаблонов test/build/index.html, и к списку статических файлов test/build/static/

import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import {createStore, compose, applyMiddleware} from 'redux';
import reducer from './store/reducers/auth';
import thunk from 'redux-thunk';
import {Provider} from 'react-redux'

const composeEnhances = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE || compose
const store = createStore(reducer, composeEnhances(
  applyMiddleware(thunk)
  ));

// ReactDOM.render(<App/>, document.getElementById('root'));

const app = (
  <Provider store={store}>
    <App/>
  </Provider>
)
ReactDOM.render(app, document.getElementById('root'));


  
// НЕ ДОДЕЛАНО
// https://www.youtube.com/watch?v=BxzO2M7QcZw&list=PLLRM7ROnmA9FxCtnLoIHAs6hIkJyd1dEx&index=3
// 34:00