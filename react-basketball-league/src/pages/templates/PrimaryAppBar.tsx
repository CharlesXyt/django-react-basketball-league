import { AppBar, Box, Button, Drawer, IconButton, Link, Toolbar, Typography, useMediaQuery } from "@mui/material";
import { useTheme } from "@mui/material/styles";
import MenuIcon from "@mui/icons-material/Menu";
import { useEffect, useState } from "react";
import { useAuthServiceContext } from "../../context/AuthContext";
import Menu from "../../components/Menu";

const PrimaryAppBar = () => {
    const theme = useTheme();
    const [sideMenu, setSideMenu] = useState(false);
    const { logout } = useAuthServiceContext();

    const isSmallScreen = useMediaQuery(theme.breakpoints.down("sm"))

    useEffect(() => {
        if (!isSmallScreen && sideMenu) {
            setSideMenu(false);
        }
    }, [isSmallScreen]);

    return (
        <AppBar
            sx={{
                backgroundColor: theme.palette.background.default,
                borderBottom: `1px solid ${theme.palette.divider}`
            }}
        >
            <Toolbar variant="dense" sx={{
                height: `${theme.primaryAppBar.height}px`,
                minHeight: `${theme.primaryAppBar.height}px`
            }}>
                <Box sx={{
                    display: {
                        xs: "block",
                        sm: "none"
                    }
                }}>
                    <IconButton
                        color="inherit"
                        edge="start"
                        sx={{ mr: 2 }}
                        onClick={() => setSideMenu(!sideMenu)}
                    >
                        <MenuIcon />
                    </IconButton>
                </Box>

                <Drawer
                    anchor="left"
                    open={sideMenu}
                    onClose={() => setSideMenu(false)}
                >
                    <Box sx={{
                        paddingTop: `${theme.primaryAppBar.height}px`,
                        minWidth: `${theme.draw.width}px`
                    }}>
                        <Menu />
                    </Box>
                </Drawer>

                <Link href="/" underline="none" color="inherit">
                    <Typography
                        variant="h6"
                        noWrap
                        component="div"
                        sx={{
                            display: {
                                fontWeight: 700,
                                letterSpacing: "-0.5px"
                            }
                        }}
                    >
                        Basketball League
                    </Typography>
                </Link>
                <Box sx={{ flexGrow: 1, display: "flex", justifyContent: "flex-end" }}>
                    <Button color="primary" onClick={() => logout()}>Logout</Button>
                </Box>

            </Toolbar>
        </AppBar>
    )
}

export default PrimaryAppBar;