import {useNavigate} from "react-router-dom";
import {useState} from "react";
import {login} from "../../services/authApi.js";

function Login() {
    const navigate = useNavigate()
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")

    async function handleLogin(event){
        event.preventDefault()
        try{
            const data = await login({email, password})
            localStorage.setItem('access', data.access)
            localStorage.setItem('refresh', data.refresh)
            console.log("login Successful")
            navigate("/profile")
        }catch(error){
            console.log(error)
        }
    }

    return(
        <form onSubmit={handleLogin}>
            <div>
                <label>Email</label>
                <input type={'text'}
                       value={email}
                       onChange={(e) => {
                           setEmail(e.target.value)
                       }}
                />
            </div>
            <div>
                <label>Password</label>
                <input
                    type={'text'}
                    value={password}
                    onChange={(e) => {
                        setPassword(e.target.value)
                    }}
                />
            </div>
            <button type={'submit'}>Login</button>
        </form>
    );
}

export default Login