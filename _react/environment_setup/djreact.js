// package.json

{
  "name": "django-react-tutorial",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "antd": "^3.19.8",
    "axios": "^0.18.0",
    "lodash": "^4.17.11",
    "react": "^16.4.1",
    "react-dom": "^16.8.6",
    "react-redux": "^5.0.7",
    "react-router-dom": "^4.3.1",
    "react-scripts": "1.1.4",
    "redux": "^4.0.0",
    "redux-thunk": "^2.3.0",
    "webpack-dev-server": "^3.3.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test --env=jsdom",
    "eject": "react-scripts eject",
    "postinstall": "npm run build"
  },
  "engines": {
    "node": "9.5.0",
    "npm": "6.4.1"
  },
  "devDependencies": {
    "react-cookies": "^0.1.0"
  }
}
