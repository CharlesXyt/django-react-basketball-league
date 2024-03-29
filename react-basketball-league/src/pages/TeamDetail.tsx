import { useLocation } from 'react-router-dom';
import { useAuthServiceContext } from '../context/AuthContext/AuthContext';
import { Box, Paper, Typography } from '@mui/material';
import { TeamDetail } from '../types/UserProfile';
import { useEffect, useState } from 'react';
import useAxiosWithInterceptor from '../helpers/jwtinterceptors';
import { API_BASE_URL } from '../config';
import LoadingSpinner from '../components/LoadingSpinner';
import UserInfo from '../components/Scoreboard/UserInfo';
import { UserRoleEnum } from '../Enums/enum';
import { useTheme } from '@mui/material/styles';
import { AppLayout } from '../components/AppLayout';

const TeamDetailPage = () => {
    const theme = useTheme();
    const location = useLocation();
    const jwtAxios = useAxiosWithInterceptor();
    const [isLoading, setIsLoading] = useState(false);
    const [teamDetail, setTeamDetail] = useState<TeamDetail | null>(null);
    const { userProfile } = useAuthServiceContext();

    const teamId = location.state.teamId ?? userProfile?.team?.id;

    useEffect(() => {
        const getTeamDetail = async () => {
            try {
                setIsLoading(true);
                const response = await jwtAxios.get(
                    API_BASE_URL + `/team?team_id=${teamId}`,
                    { withCredentials: true }
                );
                setTeamDetail(response.data);
            } catch (error) {
                console.log(error);
            } finally {
                setIsLoading(false);
            }
        };
        if (teamId) getTeamDetail();
    }, [teamId]);

    if (isLoading || teamId == null || teamDetail == null) {
        return <LoadingSpinner />;
    }
    return (
        <AppLayout>
            <Box sx={{ display: 'flex', flexDirection: 'column', mt: '30px' }}>
                <Typography variant="h5" textAlign={'center'} gutterBottom>
                    Team Detail
                </Typography>
                <Paper
                    sx={{
                        margin: theme.spacing(2),
                        padding: theme.spacing(2),
                        height: '200px',
                    }}
                >
                    <Typography variant="subtitle1" gutterBottom>
                        Team ID: {teamDetail.id}
                    </Typography>
                    <Typography variant="subtitle1" gutterBottom>
                        Team Name: {teamDetail.name}
                    </Typography>
                    <Typography variant="subtitle1" gutterBottom>
                        Coach Name: {teamDetail.coach.name}
                    </Typography>
                </Paper>
                <Typography variant="h5" textAlign={'center'} gutterBottom>
                    Team Members
                </Typography>
                <Box
                    sx={{
                        margin: theme.spacing(2),
                        display: 'flex',
                        flexWrap: 'wrap',
                        rowGap: theme.spacing(3),
                        justifyContent: 'space-between',
                    }}
                >
                    {teamDetail.members
                        ?.filter(
                            (member) => member.role.name !== UserRoleEnum.Coach
                        )
                        .map((memberData) => (
                            <UserInfo key={memberData.name} user={memberData} />
                        ))}
                </Box>
            </Box>
        </AppLayout>
    );
};

export default TeamDetailPage;
