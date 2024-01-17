import {
    List,
    ListItem,
    ListItemButton,
    ListItemText,
    Typography,
} from '@mui/material';
import { Link } from 'react-router-dom';

export const Menu = () => {
    const menu = [
        {
            name: 'ScoreBoard',
            link: '',
        },
        {
            name: 'Profile',
            link: 'profile',
        },
    ];
    return (
        <List sx={{ py: 0 }}>
            {menu.map((item) => (
                <ListItem
                    disablePadding
                    key={item.name}
                    sx={{ display: 'block' }}
                    dense={true}
                >
                    <Link
                        to={`/${item.link}`}
                        style={{ textDecoration: 'none', color: 'inherit' }}
                    >
                        <ListItemButton sx={{ minHeight: 48 }}>
                            <ListItemText
                                primary={
                                    <Typography
                                        variant="body1"
                                        textAlign="start"
                                        paddingLeft={1}
                                    >
                                        {item.name}
                                    </Typography>
                                }
                            />
                        </ListItemButton>
                    </Link>
                </ListItem>
            ))}
        </List>
    );
};
