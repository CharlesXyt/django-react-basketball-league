import { Route, BrowserRouter, Routes, Navigate } from 'react-router-dom'
import Profile from './pages/Profile'
import { ThemeProvider } from '@emotion/react'
import { createMuiTheme } from './theme/theme'
import Login from './pages/Login'
import { AuthServiceProvider } from './context/AuthContext'
import ProtectedRoute from './services/ProtectedRoute'
import ScoreDashboard from './pages/Scoreboard'
import TeamDetail from './pages/TeamDetail'

const App: React.FC = () => {
    const theme = createMuiTheme()
    return (
        <BrowserRouter>
            <AuthServiceProvider>
                <ThemeProvider theme={theme}>
                    <Routes>
                        <Route
                            path="/"
                            element={
                                <ProtectedRoute>
                                    <ScoreDashboard />
                                </ProtectedRoute>
                            }
                        />
                        <Route path="/login" element={<Login />} />
                        <Route
                            path="/profile"
                            element={
                                <ProtectedRoute>
                                    <Profile />
                                </ProtectedRoute>
                            }
                        />
                        <Route
                            path="/team"
                            element={
                                <ProtectedRoute>
                                    <TeamDetail />
                                </ProtectedRoute>
                            }
                        />
                        <Route path="*" element={<Navigate to="/" replace />} />
                    </Routes>
                </ThemeProvider>
            </AuthServiceProvider>
        </BrowserRouter>
    )
}

export default App
