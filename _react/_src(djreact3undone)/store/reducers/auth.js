import * as actionTypes from '../actions/actionTypes';
import { updateObject } from '../utility';

// in the reducer we define the initial state of entire application. 
// We define the actions. Actions are executed with the dispatch, they return an object, which contains the type and extra field.
// When that action is dispatched, then it is received in the reducer as one of the parameters. 
// Reducer is taking in all the actions. Its determining what the type of the action, and then looks which method it needs to execute, depending on the type of action, that is being received.

const InitialState = {
  token: null,
  error: null,
  loading: false
}

// creating the method that goes hand-in-hand with actions.
// The reducers job is to take the initial state. 
const authStart = (state, action) => {
  // it returns state that is updated
  return updateObject(state, {
    error: null,
    loading: true
  })
}

const authSuccess = (state, action) => {
  return updateObject(state, {
    token: action.token,
    error: null,
    loading: false
  })
}

const authFail = (state, action) => {
  return updateObject(state, {
    error: action.error,
    loading: false
  })
}

const authLogout = (state, action) => {
  return updateObject(state, {
    token: null
  })
}

// Define when these reducers take place.
const reducer = (state=InitialState, action) => {
  switch (action.type){
    case actionTypes.AUTH_START: return authStart(state, action)
    case actionTypes.AUTH_SUCCESS: return authSuccess(state, action)
    case actionTypes.AUTH_FAIL: return authFail(state, action)
    case actionTypes.AUTH_LOGOUT: return authLogout(state, action)
    default: 
      return state;
  }
} 

export default reducer;