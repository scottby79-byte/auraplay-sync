# This service will be a factory for platform clients
from backend.src.services.platforms.spotify_client import SpotifyClient
# Import other clients as they are created

def get_platform_client(platform_name, credentials):
    if platform_name.lower() == 'spotify':
        return SpotifyClient(credentials)
    # Add other platforms here
    else:
        raise ValueError(f"Unsupported platform: {platform_name}")

def get_playlists(profile):
    source_config = next((p for p in profile.platform_configurations if p.platform_type == 'source'), None)
    if not source_config:
        raise ValueError("Profile does not have a source platform configured.")

    # In a real app, you would decrypt credentials here
    # from backend.src.core.security import decrypt_data
    # credentials = decrypt_data(source_config.encrypted_credentials)
    credentials = {"token": "dummy-token"} # Placeholder

    client = get_platform_client(source_config.platform_name, credentials)
    return client.get_playlists()

def get_playlist_tracks(profile, playlist_id):
    source_config = next((p for p in profile.platform_configurations if p.platform_type == 'source'), None)
    if not source_config:
        raise ValueError("Profile does not have a source platform configured.")
    
    credentials = {"token": "dummy-token"} # Placeholder
    client = get_platform_client(source_config.platform_name, credentials)
    return client.get_playlist_tracks(playlist_id)


def get_playlist_tracks(profile, playlist_id):
    source_config = next((p for p in profile.platform_configurations if p.platform_type == 'source'), None)
    if not source_config:
        raise ValueError("Profile does not have a source platform configured.")
    
    credentials = {"token": "dummy-token"} # Placeholder
    client = get_platform_client(source_config.platform_name, credentials)
    return client.get_playlist_tracks(playlist_id)

