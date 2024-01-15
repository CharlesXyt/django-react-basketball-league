import axios, { AxiosInstance } from "axios";
import { useNavigate } from "react-router-dom";
import { API_BASE_URL } from "../config";


const useAxiosWithInterceptor = (): AxiosInstance => {
    const jwtAxios = axios.create({ baseURL: API_BASE_URL })
    const navigate = useNavigate()

    jwtAxios.interceptors.response.use(
        (response) => {
            return response
        },
        async (error) => {
            const originalRequest = error.config
            if (error.response?.status === 401 || 403) {
                const refreshToken = localStorage.getItem('refresh_token')
                if (refreshToken) {
                    try {
                        const refreshResponse = await axios.post(
                            API_BASE_URL + '/token/refresh/',
                            {
                                refresh: refreshToken
                            }
                        )
                        const { access: newAccessToken } = refreshResponse.data
                        originalRequest.headers['Authorization'] = `Bearer ${newAccessToken}`
                        localStorage.setItem('access_token', newAccessToken)
                        return jwtAxios(originalRequest)
                    } catch (refreshError) {
                        navigate('/login')
                        throw refreshError
                    }
                } else {
                    navigate('/login')
                }
            }
            throw error;
        }

    )
    return jwtAxios
}

export default useAxiosWithInterceptor;