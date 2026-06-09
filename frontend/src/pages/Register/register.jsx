import {useState} from "react";
import {register} from "../../services/authApi.js";
import {useNavigate} from "react-router-dom";


function Register() {
    const [email, setEmail] = useState("")
    const [phone_number, setPhone_number] = useState("")
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    let navigate = useNavigate()
    async function handleSubmit(event){
        event.preventDefault()
        localStorage.clear()
        try{
            const response = await register({email, phone_number, username, password})
            console.log(response)
            navigate("/login")
        }catch(err){
            console.log(err.response?.data)
            console.log(err.response?.status)
        }
    }
    return (
        <>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>Email</label>
                    <input
                        type={"text"}
                        value={email}
                        onChange={(element) => {
                            setEmail(element.target.value)
                        }}
                    />
                </div>

                <div>
                    <label>Phone number</label>
                    <input
                        type={"text"}
                        value={phone_number}
                        onChange={(element) => {
                            setPhone_number(element.target.value)
                        }}
                    />
                </div>

                <div>
                    <label>Username</label>
                    <input
                        type={"text"}
                        value={username}
                        onChange={(element) =>{
                            setUsername(element.target.value)
                        }}
                    />
                </div>

                <div>
                    <label>Password</label>
                    <input
                        type={"text"}
                        value={password}
                        onChange={(element) =>{
                            setPassword(element.target.value)
                        }}
                    />
                </div>

                <button type={"submit"}>Register</button>
            </form>
        </>
    );
}

export default Register