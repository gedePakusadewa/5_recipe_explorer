const Card = ({title, imageUrl, id}) => {
  return(
    <>
      <div className="card-food">
        <img
          src={imageUrl}
          className="card-img"
        />
        <span>{title}</span>
        <br />
        <button
          className="btn btn-card-favorite"
        >
          Favorite
        </button>
        <br />
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