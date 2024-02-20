import { useState, useEffect } from "react";
import { useCookies } from 'react-cookie';
import Card from "../component/Card.js";
import ModalDetailRecipe from "../component/ModalDetailRecipe.js";
import ModalFavorite from "../component/ModalFavorite.js";
import GeneralConst from "../resource/General.js"
import UrlConst from "../resource/Url.js"
import axios from "axios";

const Dashboard = () => {
  const [cookies, setCookie] = useCookies(['user']);
  
  const [searchInput, setSearchInput] = useState("")
  const [searchResult, setSearchResult] = useState(null)
  const [totalSearchResult, setTotalSearchResult] = useState(0)
  const [isShowModal, setIsShowModal] = useState(false)
  const [isShowModalFavorite, setIsShowModalFavorite] = useState(false)
  const [recipeIdModal, setRecipeIdModal] = useState(0)
  const [titleModal, setTitleModal] = useState('')

  const searchHandler = async () => {
    if(searchInput !== null || searchInput.length > 0){
      axios({
        method: 'get',
        url: UrlConst.SEARCH,
        headers: {'Authorization': "Token " + cookies['token']},
        params: { keyword : searchInput }
      }).then((res) => {
        setSearchResult(res.data.results)
        setTotalSearchResult(res.data.totalResults)
      })
    }
  }

  const favoriteHandler = async (idRecipe, title, imageURL) => {
    // console.log(title)
    axios({
      method: 'post',
      url: UrlConst.GETFAVORITE,
      headers: {'Authorization': "Token " + cookies['token']},
      data: { 
        recipe_id : idRecipe,
        title: title,
        imageURL: imageURL
      }
    }).then((res) => {
      console.log(res)
      setIsShowModalFavorite(true)
    })
  }

  return(
    <div className="container-home">
      <div className="container-header-home">
        <p className="title-home">{GeneralConst.EXPLORERECIPE_TITLE}</p>
        <div className="container-search-input">
          <input
            className="search-input-home"
            placeholder="Example: pasta"
            onChange={
              (e) => {setSearchInput(e.target.value)}
            }
          />
          <button
            onClick={searchHandler}
          >
            Search
          </button>
        </div>
      </div>
      <hr />
      {searchResult !== null && (
        <>
          <p>Result "{searchInput}" 10 from total {totalSearchResult}</p>
          {searchResult.map((item, idx) => {
            return (
              <Card 
                title={item.title}
                imageUrl={item.image}
                isShowBtnFavorite={true}
                id={item.id}
                setIsShowModal={setIsShowModal}
                setRecipeIdModal={setRecipeIdModal}
                setTitleModal={setTitleModal}
                favoriteHandler={favoriteHandler}
              />
            )
          })}          
        </>
      )}
      {isShowModal && (
        <ModalDetailRecipe
          recipeIdModal={recipeIdModal}
          titleModal={titleModal}
          setIsShowModal={setIsShowModal}
        />
      )}

      {isShowModalFavorite && (
        <ModalFavorite
          setIsShowModalFavorite={setIsShowModalFavorite}
          titleRecipe={titleModal}
        />
      )}
    </div>
  )
}

export default Dashboard