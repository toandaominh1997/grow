import loginUser from "./../actions/user";
import { useSelector, useDispatch } from "react-redux";
const initialState = {
    token:  null
  }


export const userReducer = (state = initialState, action) =>{
    
    switch (action.type) {
    case 'LOGIN_USER':
        return {...state, token: action.payload.token}
    default:
        console.log("default ha")
        return state;
    }
}
export default userReducer;