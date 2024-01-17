import { UserRoleEnum } from '../Enums/enum';
export interface Team {
    id: number;
    name: string;
}

export interface UserRole {
    id: number;
    name: UserRoleEnum;
}

export interface UserDetailData {
    name: string;
    email: string;
    role: UserRole;
    playerMatchInfo?: { averageScore: number; gameCount: number };
    team?: Team;
}

export interface TeamDetail {
    id: number;
    name: string;
    coach: UserDetailData;
    members: UserDetailData[];
}
