import 'antd/dist/antd.css';
import React, {Component} from 'react'
import {BrowserRouter as Router,Route} from 'react-router-dom';
import ArticleList from "./containers/ArticleListView";
import ArticleDetail from "./containers/ArticleDetailView";
import CustomLayout from './containers/Layout';

const BaseRouter = () => (
  <div>
    {/* Для обработки тэга Route нужно поместить его внутрь Router */}
    <Route 
      exact path="/" 
      component={ArticleList} />{" "}
    <Route 
      exact path="/articles/:articleID/" 
      component={ArticleDetail} />{" "}
  </div>
);

class App extends Component{
  render(){
    return(
      <div>
        {/* <Router></Router> - нужен для того, чтобы внутрь него можно было поместить BaseRouter*/}
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