import { Box, CssBaseline } from '@mui/material';
import { useTheme } from '@mui/material/styles';
import { AppHeader } from './AppHeader';
import { Drawer } from './Drawer';
import { Menu } from './Menu';

export const AppLayout = ({ children }: { children: React.ReactNode }) => {
    const theme = useTheme();
    return (
        <Box
            sx={{
                display: 'flex',
            }}
        >
            <CssBaseline />
            <AppHeader />
            <Drawer>
                <Menu />
            </Drawer>
            <Box
                sx={{
                    display: 'flex',
                    pt: `${theme.primaryAppBar.height}px`,
                    width: '100%',
                    maxHeight: '100vh',
                    overflow: 'auto',
                }}
            >
                {children}
            </Box>
        </Box>
    );
};
