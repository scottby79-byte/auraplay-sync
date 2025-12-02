// Placeholder for TargetPlaylistPanel
import React from 'react';
import { Paper, Typography, Button, Box } from '@mui/material';
import AddIcon from '@mui/icons-material/Add';

const TargetPlaylistPanel = ({ onCreateNewPlaylist }) => {
  return (
    <Paper sx={{ p: 2, height: '100%', display: 'flex', flexDirection: 'column' }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
        <Typography variant="h6">Target Playlists</Typography>
        <Button 
          variant="contained" 
          startIcon={<AddIcon />} 
          size="small"
          onClick={onCreateNewPlaylist}
        >
          New Playlist
        </Button>
      </Box>
      {/* Existing playlist list or dropped items will go here */}
      <Typography sx={{ mt: 2, color: 'text.secondary' }}>
        Drop items here or create a new playlist.
      </Typography>
    </Paper>
  );
};

export default TargetPlaylistPanel;
