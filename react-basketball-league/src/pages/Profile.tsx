import LoadingSpinner from '../components/LoadingSpinner';
import { useAuthServiceContext } from '../context/AuthContext/AuthContext';
import { Avatar, Box, Card, Typography } from '@mui/material';
import { useLocation } from 'react-router-dom';
import { useTheme } from '@mui/material/styles';
import { AppLayout } from '../components/AppLayout';

const Profile = () => {
    const theme = useTheme();
    const { userProfile } = useAuthServiceContext();
    const location = useLocation();

    const userInfo = location.state?.userProfile ?? userProfile;

    if (userInfo == null) return <LoadingSpinner />;

    return (
        <AppLayout>
            <Box
                sx={{
                    display: 'flex',
                    flexDirection: 'column',
                    mt: theme.spacing(3),
                    width: '100%',
                }}
            >
                <Typography variant="h5" textAlign={'center'} gutterBottom>
                    Profile
                </Typography>
                <Card sx={{ margin: theme.spacing(2), padding: theme.spacing(2) }}>
                    <Avatar
                        sx={{
                            width: '100px',
                            height: '100px',
                            textAlign: 'center',
                            margin: 'auto',
                            mb: theme.spacing(4),
                            fontSize: '50px',
                        }}
                    >
                        {userInfo.name[0]}
                    </Avatar>
                    <Typography variant="subtitle1" gutterBottom>
                        Name: {userInfo.name}
                    </Typography>
                    <Typography variant="subtitle1" gutterBottom>
                        Email: {userInfo.email}
                    </Typography>
                    <Typography variant="subtitle1" gutterBottom>
                        Role: {userInfo.role.name}
                    </Typography>
                    {userInfo.playerMatchInfo && (
                        <>
                            <Typography variant="subtitle1" gutterBottom>
                                Average Score:{' '}
                                {userInfo.playerMatchInfo.averageScore}
                            </Typography>
                            <Typography variant="subtitle1" gutterBottom>
                                Partipant Game Count:{' '}
                                {userInfo.playerMatchInfo.gameCount}
                            </Typography>
                        </>
                    )}
                    {userInfo.team && (
                        <Typography variant="subtitle1" gutterBottom>
                            Team: {userInfo.team.name}
                        </Typography>
                    )}
                </Card>
            </Box>
        </AppLayout>

    );
};

export default Profile;
