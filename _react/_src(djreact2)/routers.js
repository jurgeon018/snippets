import React from "react";
import { Route } from "react-router-dom";

import ArticleList from "./containers/ArticleListView";
import ArticleDetail from "./containers/ArticleDetailView";

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

export default BaseRouter;
