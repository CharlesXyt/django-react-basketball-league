import axios, { AxiosInstance } from 'axios'
import { useNavigate } from 'react-router-dom'
import { API_BASE_URL } from '../config'
import { useAuthServiceContext } from '../context/AuthContext'
import camelcaseKeys from 'camelcase-keys'

const useAxiosWithInterceptor = (): AxiosInstance => {
    const jwtAxios = axios.create({})
    const navigate = useNavigate()
    const { logout } = useAuthServiceContext()

    jwtAxios.interceptors.response.use(
        (response) => {
            response.data = camelcaseKeys(response.data, { deep: true })
            return response
        },
        async (error) => {
            const originalRequest = error.config
            if (
                error.response?.status === 401 ||
                error.response?.status === 403
            ) {
                axios.defaults.withCredentials = true
                try {
                    const response = await axios.post(
                        API_BASE_URL + '/token/refresh'
                    )
                    if (response['status'] == 200) {
                        return jwtAxios(originalRequest)
                    }
                } catch (refreshError) {
                    logout()
                    navigate('/login')
                    return Promise.reject(refreshError)
                }
            }
            return Promise.reject(error)
        }
    )
    return jwtAxios
}

export default useAxiosWithInterceptor
