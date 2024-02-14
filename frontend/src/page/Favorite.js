import { useState, useEffect } from "react";
import { useCookies } from 'react-cookie';
import Card from "../component/Card.js";
import UrlConst from "../resource/Url.js"
import axios from "axios";

const Favorite = () => {
  const [cookies, setCookie] = useCookies(['user']);

  const [favoriteData, setFavoriteData] = useState(null)

  useEffect(() =>{
    getFavorite()
  }, [])

  const getFavorite = async () => {
    axios({
      method: 'get',
      url: UrlConst.GETFAVORITE,
      headers: {'Authorization': "Token " + cookies['token']}
    }).then((res) => {
      setFavoriteData(res.data)
    })
  }

  return(
    <>
      <h1>Favorite</h1>
      {favoriteData !== null && (favoriteData.map((item, idx) => {
        return (
          <Card 
            title={item.title}
            imageUrl={item.imageURL}
            id={item.id}
            isShowBtnFavorite={false}
          />
        )
      }))}
    </>
  )
}

export default Favorite