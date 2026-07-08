import {createBrowserRouter} from "react-router-dom";

import MainLayout from "../components/layout/MainLayout.jsx";

import Home from "../pages/Home/home.jsx";
import Login from "../pages/Login/login.jsx";
import Register from "../pages/Register/register.jsx";
import Dashboard from "../pages/Dashboard/dashboard.jsx";
import Profile from "../pages/Profile/profile.jsx";
import ChangePassword from "../pages/ChangePassword/ChangePassword.jsx"

const router = createBrowserRouter([
    {
        path: '/',
        element: <MainLayout/>,
        children: [
            {
        path: "/",
        element: <Home/>
    },
    {
        path: '/register',
        element: <Register/>
    },
    {
        path: '/login',
        element: <Login/>
    },
    {
        path: '/dashboard',
        element: <Dashboard/>
    },
    {
        path: "/profile",
        element: <Profile/>
    },
    {
        path: '/change-password',
        element: <ChangePassword/>
    },
        ]
    }
]);
export default router