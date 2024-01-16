import { useTheme } from "@mui/material/styles";
import UserProfile from "./templates/UserProfile";
import { UserDetailData } from "../types/UserProfile";
import { useEffect, useState } from "react";
import useAxiosWithInterceptor from "../helpers/jwtinterceptors";
import { API_BASE_URL } from "../config";
import AppWrapper from './templates/AppWrapper';
import LoadingSpinner from "../components/LoadingSpinner";


const Profile = () => {
    const theme = useTheme()
    const [userProfile, setUserProfile] = useState<UserDetailData | null>(null)
    const [isLoading, setIsLoading] = useState(false);

    const jtwAxios = useAxiosWithInterceptor()

    useEffect(() => {
        const getUserProfile = async () => {
            setIsLoading(true);
            try {
                const response = await jtwAxios.get(API_BASE_URL + '/account', { withCredentials: true })
                const userProfile = response.data
                setUserProfile(
                    {
                        username: userProfile.username,
                        email: userProfile.email,
                        role: userProfile.role_name,
                        averageScore: userProfile.average_score,
                        team: userProfile.team
                    }
                )
            } catch (error) {
                console.log(error)
            } finally {
                setIsLoading(false);
            }


        }
        getUserProfile()
    }, [])

    const renderProfile = () => {
        if (isLoading || userProfile === null)
            return <LoadingSpinner />
        return <UserProfile profile={userProfile} />
    }

    return (
        <AppWrapper>
            {renderProfile()}
        </AppWrapper>
    );
};

export default Profile;