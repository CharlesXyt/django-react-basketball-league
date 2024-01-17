import React, { useEffect, useState } from 'react';
import Alert from '@mui/material/Alert';

interface NotificationProps {
    message: string;
    duration?: number;
}
const Notification: React.FC<NotificationProps> = ({
    message,
    duration = 2000,
}) => {
    const [open, setOpen] = useState(true);

    useEffect(() => {
        const timerId = setTimeout(() => {
            setOpen(false);
        }, duration);

        return () => {
            clearTimeout(timerId);
        };
    }, [duration]);

    return open ? (
        <Alert
            severity="warning"
            sx={{ position: 'fixed', bottom: '20px', right: '40px' }}
        >
            {message}
        </Alert>
    ) : null;
};

export default Notification;
