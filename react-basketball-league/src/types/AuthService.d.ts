import { UserDetailData } from './UserProfile';

export interface AuthServiceProps {
    isLoggedIn: boolean;
    login: (username: string, password: string) => any;
    logout: () => void;
    userProfile: UserDetailData | null;
}