import { useEffect } from "react"
import { useAuthServiceContext } from "../context/AuthContext"
import { useNavigate } from "react-router-dom"

const ProtectedRoute = ({ children }: { children: React.ReactNode }) => {
    const { isLoggedIn } = useAuthServiceContext()
    const navigate = useNavigate()

    useEffect(() => {
        if (!isLoggedIn) {
            navigate('/login')
        }
    }, [isLoggedIn])

    return <>{children}</>
}

export default ProtectedRoute;