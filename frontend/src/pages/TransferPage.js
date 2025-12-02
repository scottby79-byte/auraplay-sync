import React, { useState, useEffect } from 'react';
import { Container, Typography, Grid, CircularProgress, Alert, Button, Dialog, DialogTitle, DialogContent, DialogActions, TextField } from '@mui/material';
import { useParams } from 'react-router-dom';
import * as api from '../services/api';
import SourcePlaylistPanel from '../components/SourcePlaylistPanel';
import TargetPlaylistPanel from '../components/TargetPlaylistPanel';

const TransferPage = () => {
  const { profileId } = useParams();
  const [sourcePlaylists, setSourcePlaylists] = useState([]);
  const [selectedItems, setSelectedItems] = useState([]); // Can contain playlists or tracks
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [transferMessage, setTransferMessage] = useState('');
  const [newPlaylistName, setNewPlaylistName] = useState('');
  const [isCreatingNewPlaylist, setIsCreatingNewPlaylist] = useState(false);

  useEffect(() => {
    const fetchPlaylists = async () => {
      try {
        setLoading(true);
        const playlists = await api.getSourcePlaylists(profileId);
        setSourcePlaylists(playlists);
      } catch (err) {
        setError('Failed to fetch source playlists.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    fetchPlaylists();
  }, [profileId]);

  const handleSelectionChange = (item, isSelected) => {
    setSelectedItems(prev => 
      isSelected ? [...prev, item] : prev.filter(i => i.id !== item.id)
    );
  };

  const handleCreateNewPlaylist = () => {
    setIsCreatingNewPlaylist(true);
  };

  const handleCloseNewPlaylistDialog = () => {
    setIsCreatingNewPlaylist(false);
    setNewPlaylistName('');
  };

  const handleConfirmCreateNewPlaylist = () => {
    // For now, just close the dialog. The actual playlist creation happens on transfer.
    setIsCreatingNewPlaylist(false);
  };

  const handleTransfer = async () => {
    if (selectedItems.length === 0) {
      setError('Please select at least one item to transfer.');
      return;
    }
    try {
      setTransferMessage('Starting transfer...');
      const result = await api.transferItems(profileId, selectedItems, newPlaylistName || undefined);
      setTransferMessage(result.message);
      // Optionally reset selections after successful transfer
      setSelectedItems([]); 
      setNewPlaylistName('');
    } catch (err) {
      setError('Transfer failed.');
      console.error(err);
    }
  };

  return (
    <Container sx={{ py: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom>
        Transfer Music
      </Typography>

      {loading && <CircularProgress />}
      {error && <Alert severity="error" onClose={() => setError('')}>{error}</Alert>}
      {transferMessage && <Alert severity="info">{transferMessage}</Alert>}

      <Grid container spacing={2} sx={{ mt: 2 }}>
        <Grid item xs={12} md={6}>
          <SourcePlaylistPanel 
            playlists={sourcePlaylists}
            onSelectionChange={handleSelectionChange}
          />
        </Grid>
        <Grid item xs={12} md={6}>
          <TargetPlaylistPanel onCreateNewPlaylist={handleCreateNewPlaylist} />
        </Grid>
      </Grid>
      
      <Button
        variant="contained"
        color="primary"
        onClick={handleTransfer}
        disabled={selectedItems.length === 0 || loading}
        sx={{ mt: 4 }}
      >
        Transfer {selectedItems.length} items {newPlaylistName && `to "${newPlaylistName}"`}
      </Button>

      <Dialog open={isCreatingNewPlaylist} onClose={handleCloseNewPlaylistDialog}>
        <DialogTitle>Create New Target Playlist</DialogTitle>
        <DialogContent>
          <TextField
            autoFocus
            margin="dense"
            label="Playlist Name"
            type="text"
            fullWidth
            variant="standard"
            value={newPlaylistName}
            onChange={(e) => setNewPlaylistName(e.target.value)}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCloseNewPlaylistDialog}>Cancel</Button>
          <Button onClick={handleConfirmCreateNewPlaylist} disabled={!newPlaylistName}>Create</Button>
        </DialogActions>
      </Dialog>
    </Container>
  );
};

export default TransferPage;
