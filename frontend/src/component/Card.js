const Card = () => {
  return(
    <>
      <div className="card-food">
        <img
          src="https://spoonacular.com/recipeImages/654959-312x231.jpg"
          className="card-img"
        />
        <span>Tralla asdasd asdas</span>
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