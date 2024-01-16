import { Card, Typography } from "@mui/material"


const TeamCard = ({ teamScoreDetail }: { teamScoreDetail: any }) => {
    return (
        <Card sx={{ textAlign: "center", padding: '20px', display: "flex", flexDirection: "column", justifyContent: "center", width: "250px", height: "150px" }}>
            <Typography variant="h6">{teamScoreDetail["name"]}</Typography>
            <Typography variant="h4">{teamScoreDetail["isWinner"] ? 'Win' : 'Lose'}</Typography>
            <Typography>{`Score : ${teamScoreDetail["score"]}`}</Typography>
        </Card >
    )
}

export default TeamCard;