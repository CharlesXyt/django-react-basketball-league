import React, { createContext, useContext, useState } from 'react';
import { API_BASE_URL } from '../config';
import { AuthServiceProps } from '../types/AuthService';
import axios from 'axios';



const AuthServiceContext = createContext<AuthServiceProps | null>(null);
const AuthServiceProvider = (props: React.PropsWithChildren) => {
    const [isLoggedIn, setIsLoggedIn] = useState(() => {
        const loggedIn = localStorage.getItem("isLoggedIn")
        if (loggedIn !== null) {
            return Boolean(loggedIn)
        } else {
            return false
        }
    });

    const login = async (username: string, password: string) => {
        try {
            await axios.post(API_BASE_URL + '/token', { username, password }, { withCredentials: true })
            localStorage.setItem("isLoggedIn", "true")
            setIsLoggedIn(true)
        } catch (error) {
            setIsLoggedIn(false)
            console.log(error)
        };
    }

    const logout = () => {
        localStorage.removeItem("isLoggedIn")
        setIsLoggedIn(false)
    }

    return (
        <AuthServiceContext.Provider value={{
            isLoggedIn,
            login,
            logout
        }}>
            {props.children}
        </AuthServiceContext.Provider>
    )
};

const useAuthServiceContext = () => {
    const authContext = useContext(AuthServiceContext);
    if (authContext === null) {
        throw Error('AuthServiceProvider must be used')
    }
    return authContext;
};

export {
    AuthServiceProvider,
    useAuthServiceContext
}

