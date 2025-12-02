import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#1DB954', // Spotify Green
    },
    background: {
      default: '#121212',
      paper: '#242424',
    },
  },
});

export default theme;
