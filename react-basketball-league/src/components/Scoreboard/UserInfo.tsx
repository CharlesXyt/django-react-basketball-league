import { Avatar, Card, Typography } from '@mui/material'
import { UserDetailData } from '../../types/UserProfile'
import { useNavigate } from 'react-router-dom'
import { UserRoleEnum } from '../../Enums/enum'
import { useAuthServiceContext } from '../../context/AuthContext'

const UserInfo: React.FC<{ user: UserDetailData }> = ({ user }) => {
    const { userProfile } = useAuthServiceContext()
    const navigate = useNavigate()

    const handleClick = () => {
        if (!userProfile) {
            return
        }

        const isCoachForTeam =
            userProfile.role?.name === UserRoleEnum.Coach &&
            user.team?.id === userProfile.team?.id
        const isLeagueAdmin =
            userProfile.role?.name === UserRoleEnum.LeagueAdmin
        if (isCoachForTeam || isLeagueAdmin) {
            navigate('/profile', { state: { userProfile: user } })
        }
    }

    return (
        <Card
            sx={{
                padding: '30px',
                display: 'flex',
                flexDirection: 'column',
                justifyContent: 'center',
                minWidth: '400px',
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
    )
}

export default UserInfo
