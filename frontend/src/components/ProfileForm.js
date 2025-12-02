import React, { useState, useEffect } from 'react';
import { Button, TextField, Box, Typography, Grid, FormControl, InputLabel, Select, MenuItem } from '@mui/material';

const ProfileForm = ({ profile, platforms, onSave, onCancel }) => {
  const [name, setName] = useState('');
  const [sourcePlatform, setSourcePlatform] = useState('');
  const [targetPlatform, setTargetPlatform] = useState('');

  useEffect(() => {
    if (profile) {
      setName(profile.name);
      setSourcePlatform(profile.platform_configurations.find(p => p.platform_type === 'source')?.platform_name || '');
      setTargetPlatform(profile.platform_configurations.find(p => p.platform_type === 'target')?.platform_name || '');
    } else {
      setName('');
      setSourcePlatform('');
      setTargetPlatform('');
    }
  }, [profile]);

  const handleSubmit = (e) => {
    e.preventDefault();
    // In a real app, this would also handle credentials
    const profileData = {
        name,
        source_platform: { platform_type: 'source', platform_name: sourcePlatform },
        target_platform: { platform_type: 'target', platform_name: targetPlatform },
    };
    onSave(profileData);
  };

  const availableTargetPlatforms = platforms.filter(p => p !== sourcePlatform);

  return (
    <Box component="form" onSubmit={handleSubmit} sx={{ mt: 4, p: 2, border: '1px solid grey', borderRadius: 1 }}>
      <Typography variant="h6" gutterBottom>{profile ? 'Edit Profile' : 'Create New Profile'}</Typography>
      <Grid container spacing={2}>
        <Grid item xs={12}>
          <TextField
            fullWidth
            label="Profile Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </Grid>
        <Grid item xs={12} sm={6}>
          <FormControl fullWidth required>
            <InputLabel>Source Platform</InputLabel>
            <Select
              value={sourcePlatform}
              label="Source Platform"
              onChange={(e) => setSourcePlatform(e.target.value)}
            >
              {platforms.map(p => <MenuItem key={p} value={p}>{p}</MenuItem>)}
            </Select>
          </FormControl>
        </Grid>
        <Grid item xs={12} sm={6}>
          <FormControl fullWidth required disabled={!sourcePlatform}>
            <InputLabel>Target Platform</InputLabel>
            <Select
              value={targetPlatform}
              label="Target Platform"
              onChange={(e) => setTargetPlatform(e.target.value)}
            >
              {availableTargetPlatforms.map(p => <MenuItem key={p} value={p}>{p}</MenuItem>)}
            </Select>
          </FormControl>
        </Grid>
        <Grid item xs={12} sx={{ display: 'flex', justifyContent: 'flex-end', gap: 1 }}>
          <Button onClick={onCancel}>Cancel</Button>
          <Button type="submit" variant="contained">Save Profile</Button>
        </Grid>
      </Grid>
    </Box>
  );
};

export default ProfileForm;
