import React, {Component} from 'react'
import {BrowserRouter as Router} from 'react-router-dom';
import BaseRouter from './routers';
import 'antd/dist/antd.css';
import CustomLayout from './containers/Layout';
import {connect} from 'react-redux';
import * as actions from './store/actions/auth'




class App extends Component{
  componentDidMount(){
    this.props.onTryAutoSignup();
  }
  render(){
    return(
      <div>
        {/* <Router></Router> - нужен для того, чтобы внутрь него можно было поместить BaseRouter, внутри которого находятся:
          <Route exact path="/" component={ArticleList} />{" "}
          <Route exact path="/articles/:articleID/" component={ArticleDetail} />{" "}
        */}
        <Router>
          {/* it passes isAuthenticated from mapStateToProps into the CustomLayout component, and allows to access isAuthenticated from CustomLayout. */}
          <CustomLayout {...this.props}>
            <BaseRouter />
          </CustomLayout>
        </Router>
      </div>
    )
  }
}

// export default App;
// connect will grab the store that we created, and it will allow us to access some of the state from the store.

// mapStateToProps: converts state from react-redux store into properties which can be passed into application. It means that instead of having state = { something={...} } in App, and accessing it with {this.state.something}, we can just write:
const mapStateToProps = state => {
  return {
    isAuthenticated: state.token !== null
  }
}
// mapDispatchToProps: automatic authentication check. Everytime the app is rendered, the app will check whether or not we authenticated. 
const mapDispatchToProps = dispatch => {
  return{
    onTryAutoSignup: () => dispatch(actions.authCheckState())
  }
}
export default connect(mapStateToProps, mapDispatchToProps)(App);
