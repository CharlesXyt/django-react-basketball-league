import { Card, Typography } from '@mui/material'
import { useAuthServiceContext } from '../../context/AuthContext'
import { TeamScoreInfo } from '../../types/Match'
import { UserRoleEnum } from '../../Enums/enum'
import { useNavigate } from 'react-router-dom'

const TeamCard = ({ teamScoreDetail }: { teamScoreDetail: TeamScoreInfo }) => {
    const { userProfile } = useAuthServiceContext()
    const navigate = useNavigate()

    const handleClick = () => {
        if (!userProfile) {
            return
        }

        const isCoachForTeam =
            userProfile.role?.name === UserRoleEnum.Coach &&
            teamScoreDetail.teamId === userProfile.team?.id
        const isLeagueAdmin =
            userProfile.role?.name === UserRoleEnum.LeagueAdmin
        console.log(userProfile)
        if (isCoachForTeam || isLeagueAdmin) {
            navigate('/team', { state: { teamId: teamScoreDetail.teamId } })
        }
    }
    return (
        <Card
            sx={{
                textAlign: 'center',
                padding: '20px',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'center',
                width: '250px',
                height: '150px',
            }}
            onClick={handleClick}
        >
            <Typography variant="h6">{teamScoreDetail['name']}</Typography>
            <Typography variant="h4">
                {teamScoreDetail['isWinner'] ? 'Win' : 'Lose'}
            </Typography>
            <Typography>{`Score : ${teamScoreDetail['score']}`}</Typography>
        </Card>
    )
}

export default TeamCard
