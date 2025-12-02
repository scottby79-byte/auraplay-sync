from flask import Blueprint, request, jsonify
from backend.src.services import profile_service

profiles_bp = Blueprint('profiles', __name__)

@profiles_bp.route('/api/profiles', methods=['GET'])
def get_profiles():
    profiles = profile_service.get_all_profiles()
    return jsonify([profile.to_dict() for profile in profiles])

@profiles_bp.route('/api/profiles', methods=['POST'])
def create_profile():
    data = request.get_json()
    profile = profile_service.create_profile(data)
    return jsonify(profile.to_dict()), 201

@profiles_bp.route('/api/profiles/<int:profile_id>', methods=['GET'])
def get_profile(profile_id):
    profile = profile_service.get_profile_by_id(profile_id)
    if profile:
        return jsonify(profile.to_dict())
    return jsonify({'message': 'Profile not found'}), 404

@profiles_bp.route('/api/profiles/<int:profile_id>', methods=['PUT'])
def update_profile(profile_id):
    data = request.get_json()
    profile = profile_service.update_profile(profile_id, data)
    if profile:
        return jsonify(profile.to_dict())
    return jsonify({'message': 'Profile not found'}), 404

@profiles_bp.route('/api/profiles/<int:profile_id>', methods=['DELETE'])
def delete_profile(profile_id):
    success = profile_service.delete_profile(profile_id)
    if success:
        return '', 204
    return jsonify({'message': 'Profile not found'}), 404

# Add a to_dict method to the models to make them serializable
def _patch_models_for_serialization():
    from backend.src.models.profile import UserProfile, PlatformConfiguration

    def user_profile_to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'platform_configurations': [pc.to_dict() for pc in self.platform_configurations]
        }

    def platform_config_to_dict(self):
        return {
            'id': self.id,
            'profile_id': self.profile_id,
            'platform_type': self.platform_type,
            'platform_name': self.platform_name
            # Do not expose encrypted_credentials
        }
    
    UserProfile.to_dict = user_profile_to_dict
    PlatformConfiguration.to_dict = platform_config_to_dict

_patch_models_for_serialization()
