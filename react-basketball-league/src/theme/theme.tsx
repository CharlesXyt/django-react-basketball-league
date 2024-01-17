import { createTheme } from '@mui/material';

declare module '@mui/material/styles' {
    interface Theme {
        primaryAppBar: {
            height: number;
        };
        draw: {
            width: number;
        };
    }
    interface ThemeOptions {
        primaryAppBar: {
            height: number;
        };
        draw: {
            width: number;
        };
    }
}

export const createMuiTheme = () => {
    const theme = createTheme({
        spacing: 10,
        primaryAppBar: {
            height: 50,
        },
        draw: {
            width: 200,
        },
        components: {
            MuiAppBar: {
                defaultProps: {
                    color: 'default',
                    elevation: 0,
                },
            },
        },
    });
    return theme;
};
