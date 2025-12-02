from backend.src.services import profile_service, platform_service

def start_transfer(profile_id, items, target_playlist_name=None):
    """
    Mock implementation of the transfer service.
    Handles both playlists and individual tracks.
    """
    profile = profile_service.get_profile_by_id(profile_id)
    if not profile:
        raise ValueError("Profile not found.")

    source_config = next((p for p in profile.platform_configurations if p.platform_type == 'source'), None)
    target_config = next((p for p in profile.platform_configurations if p.platform_type == 'target'), None)

    if not source_config or not target_config:
        raise ValueError("Profile is not fully configured for transfer.")

    source_client = platform_service.get_platform_client(source_config.platform_name, {"token": "dummy-token"})
    target_client = platform_service.get_platform_client(target_config.platform_name, {"token": "dummy-token"})

    all_tracks_to_transfer = []
    
    for item in items:
        if item['type'] == 'playlist':
            print(f"Fetching tracks for playlist: {item['id']}")
            playlist_tracks = source_client.get_playlist_tracks(item['id'])
            all_tracks_to_transfer.extend(playlist_tracks)
        elif item['type'] == 'track':
            # For simplicity, assume item['id'] for track is already a full track object or can be fetched
            # In a real scenario, you'd fetch track details if only an ID is given
            all_tracks_to_transfer.append(item)
    
    print(f"Total tracks to transfer: {len(all_tracks_to_transfer)}")

    if not all_tracks_to_transfer:
        return {'message': 'No tracks found to transfer.', 'report': {'total_items': 0, 'transferred': 0, 'failed': 0, 'failures': []}}

    # Create playlist on target
    final_target_playlist_name = target_playlist_name if target_playlist_name else f"Transferred from {source_config.platform_name}"
    try:
        new_playlist_id = target_client.create_playlist(final_target_playlist_name, all_tracks_to_transfer)
        print(f"Created new playlist on target: {new_playlist_id}")
        report = {
            'total_items': len(items),
            'total_tracks_attempted': len(all_tracks_to_transfer),
            'transferred_tracks': len(all_tracks_to_transfer),
            'failed_tracks': 0,
            'failures': [],
            'target_playlist_id': new_playlist_id
        }
        return {'message': 'Transfer process completed successfully.', 'report': report}
    except Exception as e:
        print(f"Failed to create playlist on target: {e}")
        report = {
            'total_items': len(items),
            'total_tracks_attempted': len(all_tracks_to_transfer),
            'transferred_tracks': 0,
            'failed_tracks': len(all_tracks_to_transfer),
            'failures': [{'item': track, 'reason': str(e)} for track in all_tracks_to_transfer],
            'target_playlist_id': None
        }
        return {'message': 'Transfer process failed.', 'report': report}
