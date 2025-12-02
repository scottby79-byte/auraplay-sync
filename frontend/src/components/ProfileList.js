import React from 'react';
import { List, ListItem, ListItemText, IconButton, Paper, Typography, Button } from '@mui/material';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
import { Link } from 'react-router-dom';

const ProfileList = ({ profiles, onEdit, onDelete }) => {
  if (!profiles.length) {
    return <Typography>No profiles found. Create one to get started!</Typography>;
  }

  return (
    <Paper elevation={2}>
      <List>
        {profiles.map((profile) => (
          <ListItem
            key={profile.id}
            secondaryAction={
              <>
                <IconButton edge="end" aria-label="edit" onClick={() => onEdit(profile)}>
                  <EditIcon />
                </IconButton>
                <IconButton edge="end" aria-label="delete" onClick={() => onDelete(profile.id)}>
                  <DeleteIcon />
                </IconButton>
                <Button component={Link} to={`/transfer/${profile.id}`} endIcon={<ArrowForwardIcon />} sx={{ ml: 1 }}>
                  Transfer
                </Button>
              </>
            }
          >
            <ListItemText
              primary={profile.name}
              secondary={`${profile.platform_configurations.find(p => p.platform_type === 'source')?.platform_name} → ${profile.platform_configurations.find(p => p.platform_type === 'target')?.platform_name}`}
            />
          </ListItem>
        ))}
      </List>
    </Paper>
  );
};

export default ProfileList;
