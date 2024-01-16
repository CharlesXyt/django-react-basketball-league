import { useLocation } from 'react-router-dom'
import { useAuthServiceContext } from '../context/AuthContext'
import { Box, Paper, Typography } from '@mui/material'
import { TeamDetail } from '../types/UserProfile'
import { useEffect, useState } from 'react'
import useAxiosWithInterceptor from '../helpers/jwtinterceptors'
import { API_BASE_URL } from '../config'
import LoadingSpinner from '../components/LoadingSpinner'
import UserInfo from './templates/UserInfo'
import AppWrapper from './templates/AppWrapper'
import { UserRoleEnum } from '../Enums/enum'

const TeamDetailPage = () => {
  const location = useLocation()
  const jwtAxios = useAxiosWithInterceptor()
  const [isLoading, setIsLoading] = useState(false)
  const [teamDetail, setTeamDetail] = useState<TeamDetail | null>(null)
  const { userProfile } = useAuthServiceContext()

  let teamId = location.state.teamId ?? userProfile?.team?.id

  useEffect(() => {
    const getTeamDetail = async () => {
      try {
        setIsLoading(true)
        const response = await jwtAxios.get(
          API_BASE_URL + `/team?team_id=${teamId}`,
          { withCredentials: true }
        )
        setTeamDetail(response.data)
      } catch (error) {
        console.log(error)
      } finally {
        setIsLoading(false)
      }
    }
    if (teamId) getTeamDetail()
  }, [teamId])

  if (isLoading || teamId == null || teamDetail == null) {
    return <LoadingSpinner />
  }
  console.log(teamDetail)
  return (
    <AppWrapper>
      <Box sx={{ display: 'flex', flexDirection: 'column', mt: '30px' }}>
        <Typography variant="h5" textAlign={'center'} gutterBottom>
          Team Detail
        </Typography>
        <Paper
          sx={{
            width: '100%',
            margin: '20px',
            padding: '20px',
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
            margin: '20px',
            display: 'flex',
            flexWrap: 'wrap',
            rowGap: '30px',
            justifyContent: 'space-between',
          }}
        >
          {teamDetail.members
            ?.filter((member) => member.role.name !== UserRoleEnum.Coach)
            .map((memberData) => (
              <UserInfo key={memberData.name} user={memberData} />
            ))}
        </Box>
      </Box>
    </AppWrapper>
  )
}

export default TeamDetailPage
