from flask import Blueprint, jsonify
from services import profile_service, platform_service

playlists_bp = Blueprint('playlists', __name__)

@playlists_bp.route('/api/profiles/<int:profile_id>/source/playlists', methods=['GET'], endpoint='get_source_playlists')
def get_source_playlists(profile_id):
    profile = profile_service.get_profile_by_id(profile_id)
    if not profile:
        return jsonify({'message': 'Profile not found'}), 404
    
    try:
        playlists = platform_service.get_playlists(profile)
        return jsonify(playlists)
    except Exception as e:
        # In a real app, log the error
        print(e)
        return jsonify({'message': 'Failed to connect to source platform'}), 500

@playlists_bp.route('/api/profiles/<int:profile_id>/source/playlists/<string:playlist_id>/tracks', methods=['GET'], endpoint='get_source_playlist_tracks')
def get_source_playlist_tracks(profile_id, playlist_id):
    profile = profile_service.get_profile_by_id(profile_id)
    if not profile:
        return jsonify({'message': 'Profile not found'}), 404
    
    try:
        tracks = platform_service.get_playlist_tracks(profile, playlist_id)
        return jsonify(tracks)
    except Exception as e:
        print(e)
        return jsonify({'message': 'Failed to fetch playlist tracks from source platform'}), 500