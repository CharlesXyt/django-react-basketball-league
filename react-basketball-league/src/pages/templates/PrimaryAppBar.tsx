import { AppBar, Box, Drawer, IconButton, Link, Toolbar, Typography, useMediaQuery } from "@mui/material";
import { useTheme } from "@mui/material/styles";
import MenuIcon from "@mui/icons-material/Menu";
import { useEffect, useState } from "react";

const PrimaryAppBar = () => {
    const theme = useTheme();
    const [sideMenu, setSideMenu] = useState(false);

    const isSmallScreen = useMediaQuery(theme.breakpoints.down("sm"))

    useEffect(() => {
        if (!isSmallScreen && sideMenu) {
            setSideMenu(false);
        }
    }, [isSmallScreen]);

    return (
        <AppBar
            sx={{
                zIndex: (theme) => theme.zIndex.drawer + 1,
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
                        asdasda
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
            </Toolbar>
        </AppBar>
    )
}

export default PrimaryAppBar;