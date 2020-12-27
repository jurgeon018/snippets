// 1_2_3_4_in-one-file
// package
{
    "name": "helloapp",
    "version": "1.0.0",
    "scripts": {
      "start": "lite-server"
    },
    "devDependencies": {
      "babel-cli": "^6.26.0",
      "babel-preset-env": "^1.6.0",
      "babel-preset-react": "^6.24.1",
      "babel-preset-stage-0": "^6.24.1",
      "lite-server": "^2.2.1"
    },
    "babel" : {
      "presets": ["env", "react", "stage-0"]
      }
  }
// html
<!DOCTYPE html>
<body>
<div class="app" id="app1"></div>
<script crossorigin src="https://unpkg.com/react@16/umd/react.production.min.js"></script>
<script crossorigin src="https://unpkg.com/react-dom@16/umd/react-dom.production.min.js"></script>
<!-- // модуль для работы с маршрутизацией -->
<script src="https://unpkg.com/react-router-dom/umd/react-router-dom.min.js"></script>
<!--  babel cdn подключается для компиляции JSX в JS. 
Если скомпилировать вручную то CDN не нужен. -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/6.25.0/babel.min.js"></script>
<script type="text/babel" src="index.jsx">
</script>
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
<!-- <script src="public/bundle.js">
</script> -->
</body>

