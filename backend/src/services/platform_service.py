# This service will be a factory for platform clients
from .platforms.spotify_client import SpotifyClient
# Import other clients as they are created
from services import profile_service
from core.database import SessionLocal
from models.profile import UserProfile, PlatformConfiguration
from core.security import encrypt_data, decrypt_data
from datetime import datetime


def get_playlist_tracks(profile, playlist_id):
    source_config = next((p for p in profile.platform_configurations if p.platform_type == 'source'), None)
    if not source_config:
        raise ValueError("Profile does not have a source platform configured.")
    
    credentials = {"token": "dummy-token"} # Placeholder
    client = get_platform_client(source_config.platform_name, credentials)
    return client.get_playlist_tracks(playlist_id)

