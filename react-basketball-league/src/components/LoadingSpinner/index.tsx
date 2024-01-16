import { useTheme } from "@emotion/react";
import { Backdrop, CircularProgress } from "@mui/material"

const LoadingSpinner = () => {
    const theme = useTheme()
    return (
        <Backdrop
            sx={{ color: '#fff', zIndex: (theme) => theme.zIndex.appBar + 1 }}
            open={true}
        >
            <CircularProgress color="inherit" />
        </Backdrop>
    )

}

export default LoadingSpinner;