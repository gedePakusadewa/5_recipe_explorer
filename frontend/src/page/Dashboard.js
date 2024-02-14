import { useState, useEffect } from "react";
import { useCookies } from 'react-cookie';
import Card from "../component/Card.js";
import GeneralConst from "../resource/General.js"
import UrlConst from "../resource/Url.js"
import axios from "axios";

const Dashboard = () => {
  const [cookies, setCookie] = useCookies(['user']);
  
  const [searchInput, setSearchInput] = useState("")
  const [searchResult, setSearchResult] = useState(null)
  const [totalSearchResult, setTotalSearchResult] = useState(0)

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
              id={item.id}
            />
            )

          })}
          
        </>
      )}
    </div>
  )
}

export default Dashboard