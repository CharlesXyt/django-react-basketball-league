import { useEffect, useState } from 'react'
import useAxiosWithInterceptor from '../../helpers/jwtinterceptors'
import { API_BASE_URL } from '../../config'
import LoadingSpinner from '../../components/LoadingSpinner'
import GameBox from '../../components/Scoreboard/GameBox'
import { Box, Tabs, Tab } from '@mui/material'
import { Match, MatchRound } from '../../types/Match'

const ScoreBoard = () => {
    const [matches, setMatches] = useState<Match[] | null>(null)
    const [isLoading, setIsLoading] = useState(false)
    const [round, setRound] = useState<MatchRound[]>([])
    const [currentRound, setCurrentRound] = useState<number | null>(null)

    const jwtAxios = useAxiosWithInterceptor()

    const handleChange = (_event: React.SyntheticEvent, newRound: number) => {
        setCurrentRound(newRound)
    }

    useEffect(() => {
        const getRound = async () => {
            try {
                setIsLoading(true)
                const response = await jwtAxios.get(`${API_BASE_URL}/round`, {
                    withCredentials: true,
                })
                setRound(response.data)
                if (response.data.length > 0)
                    setCurrentRound(response.data[0].id)
            } catch (error) {
                console.log(error)
            } finally {
                setIsLoading(false)
            }
        }
        getRound()
    }, [])

    useEffect(() => {
        const getMatch = async () => {
            try {
                setIsLoading(true)
                const response = await jwtAxios.get(
                    `${API_BASE_URL}/scoreboard?round_id=${currentRound}`,
                    { withCredentials: true }
                )
                setMatches(response.data)
            } catch (error) {
                console.log(error)
            } finally {
                setIsLoading(false)
            }
        }
        if (currentRound !== null) {
            getMatch()
        }
    }, [currentRound])

    return (
        <Box sx={{ flexGrow: 1, margin: '40px 10%' }}>
            {round && (
                <Tabs
                    value={currentRound}
                    onChange={handleChange}
                    textColor="secondary"
                    indicatorColor="secondary"
                    aria-label="secondary tabs example"
                >
                    {round.map((r: any) => (
                        <Tab key={r.id} value={r.id} label={r.name} />
                    ))}
                </Tabs>
            )}
            {isLoading && <LoadingSpinner />}
            {matches &&
                matches
                    .filter((match: Match) => match.round === currentRound)
                    .map((game: any) => <GameBox key={game.id} game={game} />)}
        </Box>
    )
}

export default ScoreBoard
