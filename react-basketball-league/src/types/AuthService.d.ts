export interface AuthServiceProps {
    isLoggedIn: boolean,
    login: (username: string, password: string) => any,
    logout: () => void
}