class BasePlatformClient:
    """
    Base class for all platform clients.
    Defines the interface that all platform-specific clients must implement.
    """
    def __init__(self, credentials):
        self.credentials = credentials

    def get_playlists(self):
        """
        Returns a list of the user's playlists.
        Each playlist should be a dict with 'id', 'name', and 'track_count'.
        """
        raise NotImplementedError

    def get_playlist_tracks(self, playlist_id):
        """
        Returns a list of tracks for a given playlist.
        Each track should be a dict with 'id', 'name', 'artist', 'album'.
        """
        raise NotImplementedError

    def create_playlist(self, name, tracks, public=False):
        """
        Creates a new playlist with the given tracks.
        Returns the new playlist's ID.
        """
        raise NotImplementedError
