// 4_routing
// package.json
{
  "name": "webpackapp",
  "description": "A React.js project using Webpack",
  "version": "1.0.0",
  "author": "metanit.com",
  "scripts": {
    "dev": "webpack-dev-server --hot --open",
    "build": "webpack",
    "start": "lite-server"
  },
  "dependencies": {
    "react": "^16.5.0",
    "react-dom": "^16.5.0",
    "react-router-dom": "^4.3.1"
  },
  "devDependencies": {
    "@babel/core": "^7.1.2",
    "@babel/preset-env": "^7.1.0",
    "@babel/preset-react": "^7.0.0",
    "babel-cli": "^6.26.0",
    "babel-loader": "^8.0.0",
    "lite-server": "^2.2.1",
    "webpack": "^4.35.0",
    "webpack-cli": "^3.3.5",
    "webpack-dev-server": "^3.1.9"
  }
}
// webpack
var path = require('path');
 
module.exports = {
    entry: "./app/app.jsx", // входная точка - исходный файл
    output:{
        path: path.resolve(__dirname, './public'),     // путь к каталогу выходных файлов - папка public
        publicPath: '/public/',
        filename: "bundle.js"       // название создаваемого файла
    },
    module:{
        rules:[   //загрузчик для jsx
            {
                test: /\.jsx?$/, // определяем тип файлов
                exclude: /(node_modules)/,  // исключаем из обработки папку node_modules
                loader: "babel-loader",   // определяем загрузчик
                options:{
                    presets:["@babel/preset-env", "@babel/preset-react"]    // используемые плагины
                }
            }
        ]
    },
    devServer: {
        historyApiFallback: true,
    }
}
  
//   hmtml
<body>
<div class="app" id="app14"></div>
<div class="app" id="app15"></div>
<div class="app" id="app16"></div>
<div class="app" id="app17"></div>
<div class="app" id="app18"></div>
<div class="app" id="app19"></div>
<div class="app" id="app20"></div>
<div class="app" id="app21"></div>
<div class="app" id="app22"></div>
<div class="app" id="app23"></div>
<div class="app" id="app24"></div>

<script crossorigin src="https://unpkg.com/react@16/umd/react.production.min.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@16/umd/react-dom.production.min.js"></script>
<!-- // модуль для работы с маршрутизацией -->
<script src="https://unpkg.com/react-router-dom/umd/react-router-dom.min.js"></script>


<!--  babel cdn подключается для компиляции JSX в JS. 
Если скомпилировать вручную то CDN не нужен. -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/6.25.0/babel.min.js"></script>
<!-- <script type="text/babel" src="index.jsx">
</script> -->


<!-- описать конфиги в package.json -->
<!-- npm install -->
<!-- node_modules/.bin/babel index.jsx --out-file app.js -->
<!-- npm start (опционально) -->
<!-- <script src="app.js">
</script> -->


<!-- описать конфиги в package.json -->
<!-- npm install -->
<!-- описать конфиги в webpack.config.js -->
<!-- npm build -->
<!-- npm run dev -->
<script src="public/bundle.js">
</script>


</body>

//  lite server
{
    "name": "routeapp",
    "version": "1.0.0",
    "scripts": {
        "start": "lite-server"
    },
    "devDependencies": {
        "lite-server": "^2.2.1"
    }
  }