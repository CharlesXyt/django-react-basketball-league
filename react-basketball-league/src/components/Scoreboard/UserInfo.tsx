import { Avatar, Card, Typography } from '@mui/material';
import { UserDetailData } from '../../types/UserProfile';
import { useNavigate } from 'react-router-dom';
import { UserRoleEnum } from '../../Enums/enum';
import { useAuthServiceContext } from '../../context/AuthContext';
import { useTheme } from '@mui/material/styles';

const UserInfo: React.FC<{ user: UserDetailData }> = ({ user }) => {
    const theme = useTheme();
    const { userProfile } = useAuthServiceContext();
    const navigate = useNavigate();

    const handleClick = () => {
        if (!userProfile) {
            return;
        }

        const isCoachForTeam =
            userProfile.role?.name === UserRoleEnum.Coach &&
            user.team?.id === userProfile.team?.id;
        const isLeagueAdmin =
            userProfile.role?.name === UserRoleEnum.LeagueAdmin;
        if (isCoachForTeam || isLeagueAdmin) {
            navigate('/profile', { state: { userProfile: user } });
        }
    };

    return (
        <Card
            sx={{
                padding: theme.spacing(2),
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'center',
                minWidth: '400px',
                cursor: 'pointer',
                '&:hover': {
                    transform: 'scale(1.05)',
                },
            }}
            onClick={handleClick}
        >
            <Avatar
                sx={{ width: 56, height: 56, textAlign: 'center', mb: '15px' }}
            >
                {user.name[0]}
            </Avatar>
            <Typography variant="subtitle1">
                Player Name: {user.name}
            </Typography>
            <Typography variant="subtitle1">
                Player Email: {user.email}
            </Typography>
        </Card>
    );
};

export default UserInfo;
