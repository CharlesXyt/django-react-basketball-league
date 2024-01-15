import { createBrowserRouter, createRoutesFromElements, Route, RouterProvider } from "react-router-dom"
import Home from "./pages/Home"
import { ThemeProvider } from "@emotion/react"
import { createMuiTheme } from "./theme/theme"
import Login from "./pages/Login"
import { AuthServiceProvider } from "./context/AuthContext"
import ProtectedRoute from "./services/ProtectedRoute"


const router = createBrowserRouter(
  createRoutesFromElements(
    <Route>
      <Route path="/" element={<ProtectedRoute><Home /></ProtectedRoute>} />
      <Route path="/login" element={<Login />} />
    </Route>
  )
)

const App: React.FC = () => {
  const theme = createMuiTheme();
  return (
    <ThemeProvider theme={theme}>
      <AuthServiceProvider>
        <RouterProvider router={router} />
      </AuthServiceProvider>
    </ThemeProvider>
  );
};

export default App;
