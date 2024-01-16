export interface MatchRound {
    id: number
    name: string
}

export interface TeamScoreInfo {
    score: number
    teamId: number
    name: string
    isWinner: boolean
}

export interface Match {
    id: number
    name: number
    round: number
    teamScoreInfo: TeamScoreInfo[]
}
