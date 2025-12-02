from .base import BasePlatformClient

class SpotifyClient(BasePlatformClient):
    def get_playlists(self):
        # This is a mock implementation.
        # A real implementation would use the Spotify API.
        print(f"Fetching playlists from Spotify with token {self.credentials.get('token')}")
        return [
            {'id': 'spotify:playlist:1', 'name': 'My Spotify Rock Hits', 'track_count': 50},
            {'id': 'spotify:playlist:2', 'name': 'Discover Weekly', 'track_count': 30},
        ]
