import { Box } from '@mui/material'
import { useFormik } from 'formik'
import { useNavigate } from 'react-router-dom'
import { useAuthServiceContext } from '../context/AuthContext'

const Login = () => {
  const navigate = useNavigate()
  const { login } = useAuthServiceContext()
  const formik = useFormik({
    initialValues: {
      username: '',
      password: '',
    },
    onSubmit: async (values) => {
      const { username, password } = values
      await login(username, password)
      navigate('/')
    },
  })
  return (
    <Box>
      <form onSubmit={formik.handleSubmit}>
        <label>username:</label>
        <input
          id="username"
          name="username"
          type="text"
          value={formik.values.username}
          onChange={formik.handleChange}
        />
        <label>password:</label>
        <input
          id="password"
          name="password"
          type="password"
          value={formik.values.password}
          onChange={formik.handleChange}
        />
        <button type="submit">Submit</button>
      </form>
    </Box>
  )
}

export default Login
