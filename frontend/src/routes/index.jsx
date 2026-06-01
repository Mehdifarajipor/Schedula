import {createBrowserRouter} from "react-router-dom";
import Home from "../pages/Home/home.jsx";
import Login from "../pages/Login/login.jsx";
import Register from "../pages/Register/register.jsx";
import Dashboard from "../pages/Dashboard/dashboard.jsx";

const router = createBrowserRouter([
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
    }
]);
export default router