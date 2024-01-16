export interface MatchRound {
    id: number,
    name: string
}

export interface TeamScoreInfo {
    score: number,
    team_id: number,
    name: string,
    is_winner: boolean
}

export interface Match {
    id: number,
    name: number,
    round: number,
    teamScoreInfo: TeamScoreInfo[]
}