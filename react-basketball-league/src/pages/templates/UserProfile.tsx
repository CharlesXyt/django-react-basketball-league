import { UserDetailData } from "../../types/UserProfile";

interface UserProfileProps {
    profile: UserDetailData;
}


const UserProfile: React.FC<UserProfileProps> = ({ profile }) => {
    return <>{profile.username}, {profile.averageScore}</>;
}

export default UserProfile;