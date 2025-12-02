from flask import Flask
from flask_cors import CORS
from backend.src.api.profiles import profiles_bp
from backend.src.api.platforms import platforms_bp
from backend.src.api.playlists import playlists_bp
from backend.src.api.transfer import transfer_bp
from backend.src.core.database import init_db

app = Flask(__name__)
CORS(app) # Allow frontend to call the API

# Register blueprints
app.register_blueprint(profiles_bp)
app.register_blueprint(platforms_bp)
app.register_blueprint(playlists_bp)
app.register_blueprint(transfer_bp)

@app.route('/api/health')
def health_check():
    return {'status': 'ok'}

# Initialize the database
with app.app_context():
    init_db()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
