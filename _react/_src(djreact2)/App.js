import React, {Component} from 'react'
import {BrowserRouter as Router} from 'react-router-dom';
import BaseRouter from './routers';
import 'antd/dist/antd.css';
import CustomLayout from './containers/Layout';


class App extends Component{
  render(){
    return(
      <div>
        {/* <Router></Router> - нужен для того, чтобы внутрь него можно было поместить BaseRouter, внутри которого находятся:
          <Route exact path="/" component={ArticleList} />{" "}
          <Route exact path="/articles/:articleID/" component={ArticleDetail} />{" "}
        */}
        <Router>
          <CustomLayout>
            <BaseRouter>
            </BaseRouter>
          </CustomLayout>
        </Router>
      </div>
    )
  }
}

export default App;