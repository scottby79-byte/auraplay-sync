from flask import Blueprint, jsonify, request
from backend.src.services import transfer_service

transfer_bp = Blueprint('transfer', __name__)

@transfer_bp.route('/api/profiles/<int:profile_id>/transfer', methods=['POST'])
def transfer(profile_id):
    data = request.get_json()
    items_to_transfer = data.get('items', [])
    target_playlist_name = data.get('target_playlist_name')
    
    # In a real app, this would be a background job
    try:
        result = transfer_service.start_transfer(profile_id, items_to_transfer, target_playlist_name)
        return jsonify(result), 202 # Accepted
    except Exception as e:
        return jsonify({'message': str(e)}), 500
