import { Box, CssBaseline } from "@mui/material";
import PrimaryAppBar from "./templates/PrimaryAppBar";
import Drawer from "./templates/Drawer";
import { useAuthServiceContext } from "../context/AuthContext";
import { useEffect } from "react";
import axios from "axios";
import { API_BASE_URL } from "../config";


const Home = () => {
    const { logout } = useAuthServiceContext()

    useEffect(() => {
        const getUserProfile = async () => {
            const response = await axios.get(API_BASE_URL + '/user', { withCredentials: true })
            console.log(response)
        }
        getUserProfile()

    }, [])
    return (
        <Box sx={{
            display: "flex"
        }}>
            <CssBaseline />
            <PrimaryAppBar />
            <Drawer />
            <Box sx={{ mt: '100px' }}>
                <button onClick={() => logout()}>logout</button>
            </Box>
        </Box>
    );
};

export default Home;