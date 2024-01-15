import { Box, CssBaseline } from "@mui/material";
import PrimaryAppBar from "./templates/PrimaryAppBar";
import Drawer from "./templates/Drawer";
import { useAuthServiceContext } from "../context/AuthContext";


const Home = () => {
    const { logout } = useAuthServiceContext()
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