import { Link } from "react-router-dom";
import { AuthContext } from "../App.js";
import { useContext } from "react";
import { useCookies } from 'react-cookie';
import GeneralConst from "../resource/General.js"
import "../style.css";

function Navbar() {
  const context = useContext(AuthContext);
  const [cookies, setCookie] = useCookies(['user']);

  return(
    <div className="container-navbar">
      <nav>
        <div>
          <Link to="/">
            <button 
              className="btn"
            >
              {GeneralConst.DASHBOARD}
            </button>
          </Link>
        </div>
        <div>
          <Link to="/Favorite">
            <button 
              className="btn"
            >
              {GeneralConst.FAVORITE}
            </button>
          </Link>
        </div>
        <div>
          <Link to="/profile">
            <button 
              className="btn"
            >
              {GeneralConst.PROFILE}
            </button>
          </Link>
        </div>
        {cookies['token'] !== undefined && (
          <div>
            <button
              className="btn"
              onClick={()=>context.handleLogout(cookies['token'])}
            >
              {GeneralConst.LOGOUT}
            </button>
          </div>
        )}
      </nav>
    </div>
  )
};

export default Navbar;