import { Route, BrowserRouter, Routes } from "react-router-dom";
import Profile from "./pages/Profile"
import { ThemeProvider } from "@emotion/react"
import { createMuiTheme } from "./theme/theme"
import Login from "./pages/Login"
import { AuthServiceProvider } from "./context/AuthContext"
import ProtectedRoute from "./services/ProtectedRoute"
import ScoreDashboard from "./pages/Scoreboard";



const App: React.FC = () => {
  const theme = createMuiTheme();
  return (
    <BrowserRouter>
      <AuthServiceProvider>
        <ThemeProvider theme={theme}>
          <Routes>
            <Route path="/" element={
              <ProtectedRoute>
                <ScoreDashboard />
              </ProtectedRoute>
            } />
            <Route path="/login" element={<Login />} />
            <Route path="/profile" element={
              <ProtectedRoute>
                <Profile />
              </ProtectedRoute>
            } />
          </Routes>
        </ThemeProvider>
      </AuthServiceProvider>
    </BrowserRouter>

  );
};

export default App;
