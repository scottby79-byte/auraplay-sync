import React, { useState, useEffect, useCallback } from 'react';
import { Container, Typography, CircularProgress, Alert, Button, Box } from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import * as api from '../services/api';
import ProfileList from '../components/ProfileList';
import ProfileForm from '../components/ProfileForm';

const DashboardPage = () => {
  const [profiles, setProfiles] = useState([]);
  const [platforms, setPlatforms] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [editingProfile, setEditingProfile] = useState(null);
  const [isFormOpen, setIsFormOpen] = useState(false);

  const fetchData = useCallback(async () => {
    try {
      setLoading(true);
      const [profilesData, platformsData] = await Promise.all([
        api.getProfiles(),
        api.getPlatforms(),
      ]);
      setProfiles(profilesData);
      setPlatforms(platformsData.platforms);
    } catch (err) {
      setError('Failed to load data. Please try again later.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

  const handleEdit = (profile) => {
    setEditingProfile(profile);
    setIsFormOpen(true);
  };

  const handleDelete = async (profileId) => {
    if (window.confirm('Are you sure you want to delete this profile?')) {
      try {
        await api.deleteProfile(profileId);
        fetchData(); // Refresh list
      } catch (err) {
        setError('Failed to delete profile.');
        console.error(err);
      }
    }
  };

  const handleSave = async (profileData) => {
    try {
      if (editingProfile) {
        await api.updateProfile(editingProfile.id, profileData);
      } else {
        await api.createProfile(profileData);
      }
      setIsFormOpen(false);
      setEditingProfile(null);
      fetchData(); // Refresh list
    } catch (err) {
      setError('Failed to save profile.');
      console.error(err);
    }
  };

  const handleAddNew = () => {
    setEditingProfile(null);
    setIsFormOpen(true);
  };
  
  const handleCancel = () => {
    setIsFormOpen(false);
    setEditingProfile(null);
  };

  return (
    <Container sx={{ py: 4 }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
        <Typography variant="h4" component="h1">
          AuraPlay-Sync Dashboard
        </Typography>
        <Button
          variant="contained"
          startIcon={<AddIcon />}
          onClick={handleAddNew}
          disabled={isFormOpen}
        >
          New Profile
        </Button>
      </Box>
      
      {loading && <CircularProgress />}
      {error && <Alert severity="error" onClose={() => setError('')}>{error}</Alert>}
      
      {isFormOpen ? (
        <ProfileForm 
          profile={editingProfile}
          platforms={platforms}
          onSave={handleSave}
          onCancel={handleCancel}
        />
      ) : (
        <ProfileList 
          profiles={profiles}
          onEdit={handleEdit}
          onDelete={handleDelete}
        />
      )}
    </Container>
  );
};

export default DashboardPage;
