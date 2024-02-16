import GeneralConst from "../resource/General.js"

const Card = ({
    title, 
    imageUrl, 
    isShowBtnFavorite, 
    id,
    setIsShowModal = () =>{},
    setRecipeIdModal = () => {},
    setTitleModal = () => {}
  }) => {

  return(
    <>
      <div className="card-food">
        <img
          src={imageUrl}
          className="card-img"
        />
        <span>{title}</span>
        <br />
        {isShowBtnFavorite === true && (
          <>
            <button
              className="btn btn-card-favorite"
            >
              {GeneralConst.FAVORITE}
            </button>
            <br />
          </>
        )}
        <button
          className="btn btn-card-detail"
          onClick={(e) => {
            setIsShowModal(true)
            setRecipeIdModal(id)
            setTitleModal(title)
          }}
        >
          {GeneralConst.DETAIL}
        </button>
      </div>
    </>
  )
}

export default Card