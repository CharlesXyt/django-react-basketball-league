import { Box, Typography } from '@mui/material';
import TeamCard from './TeamCard';
import { useTheme } from '@mui/material/styles';

const GameBox = ({ game }: { game: any }) => {
    const theme = useTheme();
    return (
        <Box sx={{ width: '100%' }}>
            <Box
                sx={{
                    display: 'flex',
                    minWidth: '800px',
                    justifyContent: 'space-between',
                    alignItems: 'center',
                    padding: theme.spacing(2),
                }}
            >
                <Box>
                    <TeamCard teamScoreDetail={game.teamScoreInfo[0]} />
                </Box>
                <Typography variant="h2">vs</Typography>
                <Box>
                    <TeamCard teamScoreDetail={game.teamScoreInfo[1]} />
                </Box>
            </Box>
        </Box>
    );
};

export default GameBox;
