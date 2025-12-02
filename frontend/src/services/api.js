const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

const fetchApi = async (endpoint, options = {}) => {
  const response = await fetch(`${API_URL}${endpoint}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
  });
  if (!response.ok) {
    throw new Error(`API call failed: ${response.statusText}`);
  }
  return response.json();
};

export const getPlatforms = () => fetchApi('/platforms');

export const getProfiles = () => fetchApi('/profiles');

export const createProfile = (profile) => fetchApi('/profiles', {
  method: 'POST',
  body: JSON.stringify(profile),
});

export const updateProfile = (profileId, profile) => fetchApi(`/profiles/${profileId}`, {
  method: 'PUT',
  body: JSON.stringify(profile),
});

export const deleteProfile = (profileId) => fetchApi(`/profiles/${profileId}`, {
  method: 'DELETE',
});

export const getSourcePlaylists = (profileId) => fetchApi(`/profiles/${profileId}/source/playlists`);

export const transferItems = (profileId, items, targetPlaylistName) => fetchApi(`/profiles/${profileId}/transfer`, {
  method: 'POST',
  body: JSON.stringify({ items, target_playlist_name: targetPlaylistName }),
});

export const getPlaylistTracks = (profileId, playlistId) => fetchApi(`/profiles/${profileId}/source/playlists/${playlistId}/tracks`);

