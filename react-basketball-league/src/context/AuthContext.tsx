import React, { createContext, useContext, useEffect, useState } from 'react'
import { API_BASE_URL } from '../config'
import { AuthServiceProps } from '../types/AuthService'
import axios from 'axios'
import { UserDetailData } from '../types/UserProfile'

const AuthServiceContext = createContext<AuthServiceProps | null>(null)
const AuthServiceProvider = (props: React.PropsWithChildren) => {
  const [isLoggedIn, setIsLoggedIn] = useState(() => {
    const loggedIn = localStorage.getItem('isLoggedIn')
    if (loggedIn !== null) {
      return Boolean(loggedIn)
    } else {
      return false
    }
  })
  const [userProfile, setUserProfile] = useState<UserDetailData | null>(null)

  const login = async (username: string, password: string) => {
    try {
      await axios.post(
        API_BASE_URL + '/token',
        { username, password },
        { withCredentials: true }
      )
      localStorage.setItem('isLoggedIn', 'true')
      setIsLoggedIn(true)
    } catch (error) {
      setIsLoggedIn(false)
      console.log(error)
    }
  }

  const logout = () => {
    localStorage.removeItem('isLoggedIn')
    setIsLoggedIn(false)
  }

  useEffect(() => {
    const getUserProfile = async () => {
      try {
        const response = await axios.get(API_BASE_URL + '/account', {
          withCredentials: true,
        })
        const userProfile = response.data
        setUserProfile({
          name: userProfile.name,
          email: userProfile.email,
          role: userProfile.role,
          playerMatchInfo: userProfile.playerMatchInfo,
          team: userProfile.team,
        })
      } catch (error) {
        console.log(error)
      }
    }
    if (isLoggedIn) {
      getUserProfile()
    }
  }, [isLoggedIn])

  return (
    <AuthServiceContext.Provider
      value={{
        isLoggedIn,
        login,
        logout,
        userProfile,
      }}
    >
      {props.children}
    </AuthServiceContext.Provider>
  )
}

const useAuthServiceContext = () => {
  const authContext = useContext(AuthServiceContext)
  if (authContext === null) {
    throw Error('AuthServiceProvider must be used')
  }
  return authContext
}

export { AuthServiceProvider, useAuthServiceContext }
