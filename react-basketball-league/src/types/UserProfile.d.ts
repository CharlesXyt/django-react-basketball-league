export enum UserRole {
    Player = 'Player',
    LeagueAdmin = 'League Admin',
    Coach = 'Coach',
}

export interface UserDetailData {
    username: string,
    email: string,
    role: UserRole,
    averageScore?: number,
    team?: string
}