# Quickstart Guide: AuraPlay-Sync

This guide explains how to build and run the AuraPlay-Sync application using Docker and Docker Compose.

## Prerequisites

-   Docker (version 20.10.0 or later)
-   Docker Compose (version 2.0.0 or later)

## Project Structure

The application is divided into two main services:

-   `backend`: A Python/Flask REST API that handles all business logic, database interactions, and communication with external streaming services.
-   `frontend`: A React/MUI single-page application that provides the user interface.

These services are defined in the `docker-compose.yml` file at the root of the project.

## Setup

1.  **Environment Variables**:
    The backend requires an encryption key to securely store user credentials. Create a file named `.env` in the project root:

    ```sh
    # .env
    # Generate a secure random key. You can use: openssl rand -hex 32
    ENCRYPTION_KEY=your-super-secret-32-byte-encryption-key
    ```

2.  **Persistent Data**:
    A Docker volume named `auraplay_data` will be created automatically by Docker Compose. This volume will store the SQLite database (`auraplay.db`), ensuring that user profiles and configurations persist even if the backend container is removed or recreated.

## Running the Application

1.  **Build and Start Services**:
    From the root directory of the project, run the following command:

    ```bash
    docker-compose up --build
    ```

    -   `--build`: This flag forces Docker to rebuild the images for the `backend` and `frontend` services using their respective `Dockerfile`. You should use this the first time you run the application or whenever you make changes to the source code or dependencies.
    -   Docker Compose will start both containers and connect them to a shared network.

2.  **Accessing the Application**:
    -   **Frontend (Web UI)**: Once the containers are running, you can access the AuraPlay-Sync web interface by navigating to `http://localhost:3000` in your web browser.
    -   **Backend (API)**: The Flask API will be running and accessible at `http://localhost:5000`. The frontend application is pre-configured to communicate with the API on this address.

## Development Workflow

-   **Live Reloading (Frontend)**: The `frontend` service is configured with a volume that maps your local `frontend/src` directory to the container. Any changes you make to the frontend source code will trigger an automatic reload in your browser.
-   **Live Reloading (Backend)**: The `backend` service uses Flask's development server in debug mode. Any changes to the backend Python files will cause the server to automatically restart within the container.
-   **Viewing Logs**: You can view the logs for both services in the terminal where you ran `docker-compose up`. To view logs for a specific service in a separate terminal, use `docker-compose logs -f <service_name>`, where `<service_name>` is either `backend` or `frontend`.

## Stopping the Application

-   To stop the running services, press `Ctrl+C` in the terminal where `docker-compose` is running.
-   To stop the services and remove the containers, run:
    ```bash
    docker-compose down
    ```
-   To remove the persistent data volume as well (this will delete all user profiles!), run:
    ```bash
    docker-compose down -v
    ```
