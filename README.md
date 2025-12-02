# AuraPlay-Sync

AuraPlay-Sync is a modular application designed to facilitate the transfer of playlists and albums between various music streaming platforms. This application aims to provide a user-friendly interface for managing user profiles, authenticating with different streaming services, and seamlessly transferring music content from a source platform to a target platform.

## Features

-   **User Profile Management**: Create, manage, and select user profiles, each configured with source and target streaming service credentials.
-   **Multi-Platform Support**: Initial support for Deezer, Spotify, YouTube Music, Tidal, and Qobuz.
-   **Secure Authentication**: Guides users through platform-specific authentication processes and securely stores credentials.
-   **Playlist & Album Transfer**: Transfer entire playlists or albums between configured streaming services.
-   **Granular Track Transfer**: Select and transfer individual tracks to new or existing playlists on the target platform.
-   **Transfer Reports**: Detailed reports for each transfer operation, indicating success/failure for each track, with download functionality.
-   **Dockerized Deployment**: Easily deployable using Docker and Docker Compose for a consistent development and production environment.

## Technologies Used

-   **Backend**: Python, Flask, SQLAlchemy (for SQLite), Authlib (for OAuth2)
-   **Frontend**: React, Material-UI (MUI)
-   **Database**: SQLite
-   **Containerization**: Docker, Docker Compose

## Quickstart

Follow the [Quickstart Guide](specs/001-playlist-transfer-feature/quickstart.md) to set up and run the application using Docker.

## Project Structure

```
.
├── backend/
│   ├── src/                 # Backend Python source code
│   │   ├── api/             # Flask blueprints for API endpoints
│   │   ├── core/            # Core utilities (database, security)
│   │   ├── models/          # SQLAlchemy data models
│   │   └── services/        # Business logic and platform clients
│   └── tests/               # Backend tests
├── frontend/
│   ├── public/              # Static assets for React app
│   ├── src/                 # Frontend React source code
│   │   ├── components/      # Reusable UI components
│   │   ├── pages/           # Top-level page components
│   │   ├── services/        # Frontend API client
│   │   └── contexts/        # React context for state management
│   └── tests/               # Frontend tests
├── specs/
│   └── 001-playlist-transfer-feature/ # Feature-specific documentation
│       ├── plan.md              # Implementation plan
│       ├── research.md          # Research and technical decisions
│       ├── data-model.md        # Data model definition
│       ├── contracts/           # API specifications (e.g., openapi.yaml)
│       ├── quickstart.md        # Quickstart guide for this feature
│       └── tasks.md             # Detailed task list
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile.backend       # Dockerfile for the Flask backend
├── Dockerfile.frontend      # Dockerfile for the React frontend
├── .env.example             # Example environment variables
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

## Setup & Configuration

1.  **Environment Variables**:
    Create a `.env` file in the project root based on `.env.example`. This file should contain sensitive information like the `ENCRYPTION_KEY` used by the backend.

    ```ini
    # .env
    ENCRYPTION_KEY=<your_secure_32_byte_base64_encoded_key>
    # Generate with: openssl rand -base64 32
    ```

2.  **Docker**:
    Ensure Docker and Docker Compose are installed on your system.
    Build and run the application using `docker-compose up --build`.

## Development

Refer to the [Quickstart Guide](specs/001-playlist-transfer-feature/quickstart.md) for detailed instructions on running the application locally, accessing the UI, and development workflow.

## Contributing

Contributions are welcome! Please follow the existing code conventions and submit pull requests for new features or bug fixes.

## License

[Specify your project's license here, e.g., MIT, Apache 2.0]
