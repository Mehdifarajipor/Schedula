import {useState, useEffect} from "react";
import {changePassword} from "../../services/authApi.js";


function ChangePassword(){
    const [old_password, setOld_password] = useState("")
    const [new_password, setNew_password] = useState("")
    const [confirm_password, setConfirm_password] = useState("")
    const [message, setMessage] = useState("")

    async function handleSubmit(event){
        event.preventDefault()
        const data = changePassword({old_password, new_password, confirm_password})
        setMessage("your password was changed successfully")
    }

    return(
        <div>
            <form onSubmit={handleSubmit}>
                <div>
                    <label>old password</label>
                    <input type={"password"}
                    value={old_password}
                    onChange={(e)=> {
                        setOld_password(e.target.value)
                    }} />
                </div>

                <div>
                    <label>new password</label>
                    <input type={"password"}
                    value={new_password}
                    onChange={(e)=> {
                        setNew_password(e.target.value)
                    }}/>
                </div>

                <div>
                    <label>confirm password</label>
                    <input type={"password"}
                    value={confirm_password}
                    onChange={(e)=> {
                        setConfirm_password(e.target.value)
                    }}/>
                </div>


                <div>{message}</div>

                <input type={"submit"} value={"Change Password"}/>
            </form>

        </div>
    )
}

export default ChangePassword