import { Box, CssBaseline } from "@mui/material";
import PrimaryAppBar from "./templates/PrimaryAppBar";
import Drawer from "./templates/Drawer";


const Home = () => {

    return (
        <Box sx={{
            display: "flex"
        }}>
            <CssBaseline />
            <PrimaryAppBar />
            <Drawer />
        </Box>
    );
};

export default Home;