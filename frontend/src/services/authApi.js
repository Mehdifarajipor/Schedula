import api from './api.js';


export async function login(data){
    const response = await api.post("accounts/login/", data);
    return response.data
}


export async function register(data){
    const response = await api.post("accounts/register/", data);
    return response.data;
}


export async function getProfile(){
    const response = await api.get("accounts/me/")
    return response.data
}