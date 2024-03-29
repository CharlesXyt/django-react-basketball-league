import { Card, Typography } from '@mui/material';
import { useAuthServiceContext } from '../../context/AuthContext/AuthContext';
import { TeamScoreInfo } from '../../types/Match';
import { UserRoleEnum } from '../../Enums/enum';
import { useNavigate } from 'react-router-dom';
import Notification from '../Notification';
import { useState } from 'react';
import { useTheme } from '@mui/material/styles';

const TeamCard = ({ teamScoreDetail }: { teamScoreDetail: TeamScoreInfo }) => {
    const theme = useTheme();
    const { userProfile } = useAuthServiceContext();
    const [alert, setAlert] = useState(false);
    const navigate = useNavigate();

    const handleClick = () => {
        if (!userProfile) {
            setAlert(true);
            return;
        }

        const isCoachForTeam =
            userProfile.role?.name === UserRoleEnum.Coach &&
            teamScoreDetail.teamId === userProfile.team?.id;
        const isLeagueAdmin =
            userProfile.role?.name === UserRoleEnum.LeagueAdmin;
        if (isCoachForTeam || isLeagueAdmin) {
            navigate('/team', { state: { teamId: teamScoreDetail.teamId } });
        } else {
            setAlert(true);
        }
    };

    return (
        <>
            <Notification
                onClose={() => {
                    setAlert(false);
                }}
                showNotification={alert}
                message="Team Detail Access Denied"
            />
            <Card
                sx={{
                    textAlign: 'center',
                    padding: theme.spacing(2),
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'center',
                    width: '250px',
                    height: '150px',
                    bgcolor: teamScoreDetail['isWinner']
                        ? 'palegreen'
                        : 'lightsalmon',
                    cursor: 'pointer',
                    '&:hover': {
                        transform: 'scale(1.05)',
                    },
                }}
                onClick={handleClick}
            >
                <Typography variant="h6">{teamScoreDetail['name']}</Typography>
                <Typography variant="h4">
                    {teamScoreDetail['isWinner'] ? 'Win' : 'Lose'}
                </Typography>
                <Typography>{`Score : ${teamScoreDetail['score']}`}</Typography>
            </Card>
        </>
    );
};

export default TeamCard;
