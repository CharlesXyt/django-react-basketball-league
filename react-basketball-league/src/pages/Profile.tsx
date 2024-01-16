import AppWrapper from './templates/AppWrapper'
import LoadingSpinner from '../components/LoadingSpinner'
import { useAuthServiceContext } from '../context/AuthContext'
import { Avatar, Box, Card, Typography } from '@mui/material'
import { useLocation } from 'react-router-dom'

const Profile = () => {
    const { userProfile } = useAuthServiceContext()
    const location = useLocation()

    let userInfo = location.state?.userProfile ?? userProfile

    if (userInfo == null) return <LoadingSpinner />

    return (
        <AppWrapper>
            <Box
                sx={{
                    display: 'flex',
                    flexDirection: 'column',
                    mt: '30px',
                    width: '100%',
                }}
            >
                <Typography variant="h5" textAlign={'center'} gutterBottom>
                    Profile
                </Typography>
                <Card sx={{ margin: '20px', padding: '20px' }}>
                    <Avatar
                        sx={{
                            width: '100px',
                            height: '100px',
                            textAlign: 'center',
                            margin: 'auto',
                            mb: '40px',
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
        </AppWrapper>
    )
}

export default Profile
