import { useEffect, useState } from "react";
import { useCookies } from 'react-cookie';
import Navbar from "../component/NavBar.js";
import GeneralConst from "../resource/General.js"
import UrlConst from "../resource/Url.js"
import axios from "axios";
import "../style.css";

const Profile = () => {
  const [cookies, setCookie] = useCookies(['user']);
  
  const [form, setForm] = useState({
    username:"",
    email:""
  });

  useEffect(() => {
    getProfile()
  }, [])

  const getProfile = async () => {    
    axios({
      method: 'get',
      url: UrlConst.GETPROFILE,
      headers: {'Authorization': "Token " + cookies['token']},
    }).then((res) => {
      setForm({
        username: res.data.user.username,
        email: res.data.user.email
      })
    })
  };

  const onSubmit = () => {    
    axios({
      method: 'post',
      url: UrlConst.GETPROFILE,
      data: {
        username:form.username,
        email:form.email
      },
      headers: {'Authorization': "Token " + cookies['token']},
    })
  };

  const updateForm = (e) =>{
    setForm(previousState =>{
      return { 
        ...previousState,
        [e.target.name]:e.target.value
      }
    });
  }

  return(
    <div className="container-profile">
      <div className="wrapper-profile">
        <div className="title-profile">{GeneralConst.PROFILE}</div>
        <label htmlFor="title">{GeneralConst.USERNAME}</label><br />
        <input 
          type="input"
          defaultValue={form.username}
          name="username"
          onChange={
            (e) => {updateForm(e)}
          }
        />
        <label htmlFor="title">{GeneralConst.EMAIL}</label><br />
        <input
          type="email"
          name="email"
          defaultValue={form.email}
          onChange={
            (e) => {updateForm(e)}
          }
        />
        <button
          className="btn-cust"
          onClick={onSubmit}
        >
          Update
        </button>
      </div>
    </div>
  )
}

export default Profile