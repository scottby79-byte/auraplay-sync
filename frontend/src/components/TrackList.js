import React from 'react';
import { List, ListItem, ListItemText, Checkbox } from '@mui/material';

const TrackList = ({ tracks, onSelectionChange }) => {
  return (
    <List dense sx={{ width: '100%', bgcolor: 'background.paper' }}>
      {tracks.map((track) => (
        <ListItem key={track.id}>
          <Checkbox
            edge="start"
            onChange={(e) => onSelectionChange({ id: track.id, type: 'track', name: track.name, artist: track.artist, album: track.album }, e.target.checked)}
          />
          <ListItemText primary={track.name} secondary={`${track.artist} - ${track.album}`} />
        </ListItem>
      ))}
    </List>
  );
};

export default TrackList;
