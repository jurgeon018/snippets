  НИХУЯ НЕ РАБОТАЕТ БЛЯДЬ


// terminal
npm init    
  // (заполнить вручную)
npm init -y 
  // (заполнить дефолтными значениями)
npm install react react-dom 
  // (установить без добавления зависимостей в packages.json)
npm install react react-dom --save 
  // (установить с добавлением зависимостей в packages.json)
npm install webpack webpack-dev-server webpack-cli --save
npm install babel-core babel-loader babel-preset-env babel-preset-react html-webpack-plugin --save-dev

npm install @babel/core babel-preset-es2015 --save


//  package.json
{
  "name": "test",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    // вписать самому
    "start": "webpack-dev-server --mode development --open --hot",
    "build": "webpack --mode production"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "react": "^16.8.6",
    "react-dom": "^16.8.6",
    "webpack": "^4.35.0",
    "webpack-cli": "^3.3.5",
    "webpack-dev": "^1.1.1"
  },
  "devDependencies": {
    "babel-core": "^6.26.3",
    "babel-loader": "^8.0.6",
    "babel-preset-env": "^1.7.0",
    "babel-preset-react": "^6.24.1",
    "html-webpack-plugin": "^3.2.0"
  }
}

// index.js
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>
  <div id="app"></div>
  <script src="index_bundle.js"></script>
</body>
</html>
{/* App.js */}
import React, {Component} from 'react';
class App extends Component{
  render(){
    return(
      <div>
        <h1>Helloworld!</h1>
      </div>
    )
  }
}
{/* main.js */}
import App from 'App.js';
import React from 'react';
import ReactDOM from 'react-dom';
ReactDOM.render(App, document.getElementById('app'))

{/* webpack.config.js */}
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
module.exports = {
  entry: './main.js',
  output: {
    path: path.join(__dirname, '/bundle'),
    filename: 'index_bundle.js'
  },
  devServer: {
    inline: true,
    port: 8080
  },
  module:{
    rules:[
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
        query:{
          presets:['es2015','react']
        }
      }
    ]
  },
  plugins:[
    new HtmlWebpackPlugin({
      template: './index.html'
    })
  ]
}
{/* .babelrc */}
{
  "preset":["env", "react"]
}


{/* terminal */}
npm run build
