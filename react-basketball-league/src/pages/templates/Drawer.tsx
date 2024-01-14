import { useTheme } from "@mui/material/styles";
import { Box } from "@mui/material";

const Drawer = () => {
    const theme = useTheme();
    return (
        <Box sx={{
            minWidth: `${theme.draw.width}px`,
            height: `calc(100vh - ${theme.primaryAppBar.height}px)`,
            mt: `${theme.primaryAppBar.height}px`,
            borderRight: `1px solid ${theme.palette.divider}`,
            display: {
                xs: "none",
                sm: "block"
            }
        }}>
            asdasdasd
        </Box>
    )
}

export default Drawer;