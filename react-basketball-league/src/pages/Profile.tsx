import UserProfile from "./templates/UserProfile";
import AppWrapper from './templates/AppWrapper';
import LoadingSpinner from "../components/LoadingSpinner";
import { useAuthServiceContext } from "../context/AuthContext";


const Profile = () => {
    const { userProfile } = useAuthServiceContext()

    const renderProfile = () => {
        if (userProfile === null)
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