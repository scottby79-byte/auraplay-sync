from flask import Blueprint, jsonify

platforms_bp = Blueprint('platforms', __name__)

SUPPORTED_PLATFORMS = ["Spotify", "Deezer", "YouTube Music", "Tidal", "Qobuz"]

@platforms_bp.route('/api/platforms', methods=['GET'])
def get_supported_platforms():
    """
    Returns the list of supported streaming platforms.
    """
    return jsonify({"platforms": SUPPORTED_PLATFORMS})
