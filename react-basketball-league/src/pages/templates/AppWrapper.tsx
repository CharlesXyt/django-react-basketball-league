import { Box, CssBaseline } from "@mui/material";
import PrimaryAppBar from "./PrimaryAppBar";
import Drawer from "./Drawer";
import { useTheme } from "@mui/material/styles";
const AppWrapper = ({ children }: { children: React.ReactNode }) => {
    const theme = useTheme();
    return (
        <Box sx={{
            display: "flex"
        }}>
            <CssBaseline />
            <PrimaryAppBar />
            <Drawer />
            <Box sx={{ pt: `${theme.primaryAppBar.height}px}`, flexBasis: "100%" }}>
                {children}
            </Box>
        </Box>
    )
}

export default AppWrapper