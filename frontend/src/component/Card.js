const Card = ({title, imageUrl, id, isShowBtnFavorite}) => {
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
              Favorite
            </button>
            <br />
          </>
        )}
        <button
          className="btn btn-card-detail"
        >
          Detail
        </button>
      </div>
    </>

  )
}

export default Card