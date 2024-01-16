import { Box, Typography } from '@mui/material'
import TeamCard from './TeamCard'

const GameBox = ({ game }: { game: any }) => {
  return (
    <Box sx={{ width: '100%' }}>
      <Box
        sx={{
          display: 'flex',
          minWidth: '800px',
          justifyContent: 'space-between',
          alignItems: 'center',
          padding: '20px',
        }}
      >
        <Box sx={{}}>
          <TeamCard teamScoreDetail={game.teamScoreInfo[0]} />
        </Box>
        <Typography variant="h2">vs</Typography>
        <Box>
          <TeamCard teamScoreDetail={game.teamScoreInfo[1]} />
        </Box>
      </Box>
    </Box>
  )
}

export default GameBox
