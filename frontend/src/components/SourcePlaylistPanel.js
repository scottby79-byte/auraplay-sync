import React, { useState } from 'react';
import { Paper, Typography, List, ListItem, ListItemText, Checkbox, IconButton, Collapse, Box } from '@mui/material';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import ExpandLessIcon from '@mui/icons-material/ExpandLess';
import TrackList from './TrackList'; // New component
import * as api from '../services/api'; // Assuming api service can fetch tracks

const SourcePlaylistPanel = ({ profileId, playlists, onSelectionChange }) => {
  const [expandedPlaylistId, setExpandedPlaylistId] = useState(null);
  const [tracksInExpandedPlaylist, setTracksInExpandedPlaylist] = useState([]);
  const [loadingTracks, setLoadingTracks] = useState(false);

  const handleToggleExpand = async (playlistId) => {
    if (expandedPlaylistId === playlistId) {
      setExpandedPlaylistId(null);
      setTracksInExpandedPlaylist([]);
    } else {
      setExpandedPlaylistId(playlistId);
      setLoadingTracks(true);
      try {
        // Assume API has an endpoint for fetching tracks of a playlist
        // This would be implemented in backend/src/api/playlists.py
        const fetchedTracks = await api.getPlaylistTracks(profileId, playlistId);
        setTracksInExpandedPlaylist(fetchedTracks);
      } catch (error) {
        console.error("Failed to fetch tracks:", error);
        setTracksInExpandedPlaylist([]);
      } finally {
        setLoadingTracks(false);
      }
    }
  };

  return (
    <Paper sx={{ p: 2, height: '100%' }}>
      <Typography variant="h6">Source Playlists</Typography>
      <List>
        {playlists.map(playlist => (
          <Box key={playlist.id}>
            <ListItem>
              <Checkbox
                edge="start"
                onChange={(e) => onSelectionChange({ id: playlist.id, type: 'playlist' }, e.target.checked)}
              />
              <ListItemText primary={playlist.name} secondary={`${playlist.track_count} tracks`} />
              <IconButton onClick={() => handleToggleExpand(playlist.id)}>
                {expandedPlaylistId === playlist.id ? <ExpandLessIcon /> : <ExpandMoreIcon />}
              </IconButton>
            </ListItem>
            <Collapse in={expandedPlaylistId === playlist.id} timeout="auto" unmountOnExit>
              <Box sx={{ pl: 4, maxHeight: 300, overflowY: 'auto' }}>
                {loadingTracks ? (
                  <Typography>Loading tracks...</Typography>
                ) : (
                  <TrackList tracks={tracksInExpandedPlaylist} onSelectionChange={onSelectionChange} />
                )}
              </Box>
            </Collapse>
          </Box>
        ))}
      </List>
    </Paper>
  );
};

export default SourcePlaylistPanel;
