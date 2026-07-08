import {useState, useEffect} from "react";
import {getProfile} from "../../services/authApi.js";
import {Link} from "react-router-dom";


function Profile(){
    const [user, setUser] = useState(null)

    useEffect(() => {
        async function fetchProfile(){
            try{
                const data = await getProfile()
                setUser(data)
            }catch (error){
                console.log(error)
            }
        }
        fetchProfile();
    }, []);
    console.log(user)
    if (!user) {
    return <p>Loading...</p>;
  }

   return (
     <>
         <img src={`${user.avatar}`}
              style={{width: "100px", height: "100px", borderRadius: "50px"}} alt={"profile"}/>
         <h2>{user.username}</h2>
         <p>{user.phone_number}</p>
         <p>{user.email}</p>
         <div>
             <Link to="/change-password">
                <button>تغییر رمز عبور</button>
            </Link>
         </div>
     </>
   );
}

export default Profile;