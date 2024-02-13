import Card from "../component/Card.js";
import GeneralConst from "../resource/General.js"

const Dashboard = () => {
  
  
  return(
    <div className="container-home">
      <div className="container-header-home">
        <p className="title-home">{GeneralConst.EXPLORERECIPE_TITLE}</p>
        <div className="container-search-input">
          <input
            className="search-input-home"
            placeholder="Search Recipe"
          />
        </div>
      </div>
      <hr />
      <p>Result from XX total</p>
      <Card />
    </div>
  )
}

export default Dashboard