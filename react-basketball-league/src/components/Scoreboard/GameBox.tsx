import { Box, Typography } from '@mui/material';
import TeamCard from './TeamCard';
import { useTheme } from '@mui/material/styles';
import { Match } from '../../types/Match';

const GameBox = ({ game }: { game: Match }) => {
    const theme = useTheme();
    return (
        <Box
            sx={{
                display: 'flex',
                minWidth: '800px',
                justifyContent: 'space-between',
                alignItems: 'center',
                padding: theme.spacing(2),
            }}
        >
            <TeamCard teamScoreDetail={game.teamScoreInfo[0]} />
            <Typography variant="h2">vs</Typography>
            <TeamCard teamScoreDetail={game.teamScoreInfo[1]} />
        </Box>
    );
};

export default GameBox;
