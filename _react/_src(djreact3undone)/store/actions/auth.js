// Methods that will take place on receiving actions from actionTypes.js

import axios from 'axios';
import * as actionTypes from './actionTypes';

export const authStart = () => {
  return {
    // when working with the actions, object that we need to return always need to include a type
    // actionTypes.AUTH_START - message that is received when we execute the authStart() method.
    type: actionTypes.AUTH_START
  }
}

// in order to have a successfull login we are going to receive a token.
export const authSuccess = (token) => {
  return {
    // when working with the actions, object that we need to return always need to include a type
    // actionTypes.AUTH_SUCCESS - message that is received when we execute the authSuccess() method.
    type: actionTypes.AUTH_SUCCESS,
    token: token
  }
}


export const authFail = (error) => {
  return{
    // when working with the actions, object that we need to return always need to include a type
    // actionTypes.AUTH_FAIL - message that is received when we execute the authFail() method.
    type: actionTypes.AUTH_FAIL,
    error: error
  }
}


export const logout = () => {
  // to logout the user we need to remove his credentials
  localStorage.removeItem('user');
  localStorage.removeItem('expirationDate');
  return {
    type: actionTypes.AUTH_LOGOUT
  }
}

// method that checks if the expiration date has expired. The timer for logout to take place has been set for 1 hour
export const checkAuthTimeout = (expirationTame) => {
  return dispatch => {
    setTimeout( () => {
      dispatch(logout());
    }, expirationTame * 1000)
  }
}

// In order to login we need 2 parameters. Once you've set up the backend, you'll know what parameters you need. 
export const authLogin = (username, password) => {
  // When we login, we want to return a dispatch. Dispatch is a method, call to action. It returns a dispatch of the authStart method. It tells, or it alerts us, that the authStart has taken place. 
  return dispatch => {
    // Once the authLogin is called, we say that out authentication proccess has started. That will be an alert, that we can look at.
    dispatch(authStart());
    // And then we want to login user into the django-rest-framework. We want to post parameters username and password into the backend api.
    axios.post('http://127.0.0.1:8000/rest-auth/login/', {
      username: username, 
      password: password
    })
    // Once we have posted username and password, we are going to get a response(res) using promise(.then). In the response we are going to get back the key. Key is what is returned from DRF once you've successfully logged in. DRF is going to generate the key, or give the key that is already assigned to the user.
    .then(res => {
      const token = res.data.key;
      // gives the expiration date of 1 hour
      const expirationDate = new Date(new Date().getTime + 3600 * 1000)
      // We want to store token and expiration date in the local storage of the browser
      // This is the logic that you need, to persist the user's session in the application. We can't jsut store in the state of application, because once the application reloads - then that data has gone, its refreshed. So we need to store it in something that persists, and an example of that in localStorage.
      localStorage.setItem('token', token);
      localStorage.setItem('expirationDate', expirationDate);
      // once you've stored those variables, you need to dispatch the authSuccess and pass in the token.
      dispatch(authSuccess(token))
      // once the user has successfully logged in with the token then we are executing the checkAuthTimeout method to take place, setting the timer.
      dispatch(checkAuthTimeout(3600))
    })
    // in case we've posted incorrect set of username and password
    .catch( (err) => {
      dispatch(authFalid(err))
    })
  }
}


// The same as authLogin, but needs and email, password1 and password2. Those are the parameters that are required by DRF
export const authSignup = (username, email, password1, password2) => {
  return dispatch => {
    dispatch(authStart());
    axios.post('http://127.0.0.1:8000/rest-auth/registration/', {
      username: username, 
      password1: password1,
      password2: password2,
      email: email
    })
    .then(res => {
      const token = res.data.key;      const expirationDate = new Date(new Date().getTime + 3600 * 1000)
      localStorage.setItem('token', token);
      localStorage.setItem('expirationDate', expirationDate);
      dispatch(authSuccess(token))
      dispatch(checkAuthTimeout(3600))
    })
    .catch( (err) => {
     dispatch(authFalid(err))
    })
  }
}


export const authCheckState = () => {
  return dispatch => {

  }
}

https://www.youtube.com/watch?v=BxzO2M7QcZw&list=PLLRM7ROnmA9FxCtnLoIHAs6hIkJyd1dEx&index=3
45:00