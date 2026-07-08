import {Link} from "react-router-dom";
import api from "../../services/api.js";
import {useEffect, useState} from "react";

function Navbar(){
    const [isLoggedIn, setIsLoggedIn] = useState(false);

useEffect(() => {
    async function checkLogin() {
        try {
            await api.get("accounts/me/");
            setIsLoggedIn(true);
        } catch {
            setIsLoggedIn(false);
        }
    }

    checkLogin();
}, []);
    return(
        <nav>
            <Link to={"/"}> Home </Link>
            <Link to={"/dashboard"}> Dashboard </Link>
            <Link to={"/register"}> Register </Link>
            {isLoggedIn ?
                (<Link to="/profile">Profile</Link>) :
                (<Link to="/login">Login</Link>)
            }
        </nav>
    );
}
export default Navbar