import { AppLayout } from '../components/AppLayout';
import { useEffect, useState } from 'react';
import useAxiosWithInterceptor from '../helpers/jwtinterceptors';
import { API_BASE_URL } from '../config';
import LoadingSpinner from '../components/LoadingSpinner';
import GameBox from '../components/Scoreboard/GameBox';
import { Box, Tabs, Tab } from '@mui/material';
import { Match, MatchRound } from '../types/Match';
import { useTheme } from '@mui/material/styles';

const ScoreDashboardContainer = () => {
    const [matches, setMatches] = useState<Match[] | null>(null);
    const [isLoading, setIsLoading] = useState(false);
    const [round, setRound] = useState<MatchRound[]>([]);
    const [currentRound, setCurrentRound] = useState<number | null>(null);
    const theme = useTheme();

    const jwtAxios = useAxiosWithInterceptor();

    const handleChange = (_event: React.SyntheticEvent, newRound: number) => {
        setCurrentRound(newRound);
    };

    useEffect(() => {
        const getRound = async () => {
            try {
                setIsLoading(true);
                const response = await jwtAxios.get(`${API_BASE_URL}/round`, {
                    withCredentials: true,
                });
                setRound(response.data);
                if (response.data.length > 0)
                    setCurrentRound(response.data[0].id);
            } catch (error) {
                console.log(error);
            } finally {
                setIsLoading(false);
            }
        };
        getRound();
    }, []);

    useEffect(() => {
        const getMatch = async () => {
            try {
                setIsLoading(true);
                const response = await jwtAxios.get(
                    `${API_BASE_URL}/scoreboard?round_id=${currentRound}`,
                    { withCredentials: true }
                );
                setMatches(response.data);
            } catch (error) {
                console.log(error);
            } finally {
                setIsLoading(false);
            }
        };
        if (currentRound !== null) {
            getMatch();
        }
    }, [currentRound]);

    return (
        <AppLayout>
            <Box sx={{ flexGrow: 1, margin: `${theme.spacing(4)} 10%` }}>
                {round && (
                    <Tabs
                        value={currentRound}
                        onChange={handleChange}
                        textColor="secondary"
                        indicatorColor="secondary"
                        aria-label="secondary tabs example"
                    >
                        {round.map(r => (
                            <Tab key={r.id} value={r.id} label={r.name} />
                        ))}
                    </Tabs>
                )}
                {isLoading && <LoadingSpinner />}
                {matches &&
                    matches
                        .filter(match => match.round === currentRound)
                        .map((game) => (
                            <GameBox key={game.id} game={game} />
                        ))}
            </Box>
        </AppLayout>
    );
};

export default ScoreDashboardContainer;
