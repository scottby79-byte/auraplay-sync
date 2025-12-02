# Research & Decisions

This document outlines the key technical decisions made during the planning phase for the Playlist Transfer Feature.

## 1. Frontend Framework Selection

- **Decision**: React
- **Rationale**: The user provided a choice between `React.js`, `Vue.js`, and `Angular`. React is chosen for its large ecosystem, strong community support, and robust component-based architecture, which is well-suited for building a dynamic, single-page application like AuraPlay-Sync. Its performance and developer experience are excellent for this project's scale.
- **Alternatives considered**: `Vue.js`, `Angular`. While both are capable frameworks, React's ecosystem and talent pool are slightly larger, making it a safe and productive choice.

## 2. Frontend UI Component Library

- **Decision**: Material-UI (MUI)
- **Rationale**: To meet the requirement for a "très user friendly" interface that adheres to modern web standards, a component library is essential. MUI provides a comprehensive set of well-designed, pre-built React components that follow Material Design principles. This will accelerate UI development, ensure a consistent and high-quality user experience, and provide excellent cross-browser compatibility out-of-the-box.
- **Alternatives considered**: `Ant Design`, `Bootstrap for React`. MUI is chosen for its aesthetic appeal and tight integration with the React ecosystem.

## 3. Backend OAuth2 Library

- **Decision**: `Authlib` for Python
- **Rationale**: The application's core functionality relies on authenticating with multiple third-party streaming services (Spotify, Deezer, etc.), which use OAuth2. `Authlib` is a powerful and well-maintained Python library that provides a comprehensive OAuth2 client implementation. It has built-in support for many popular providers and is highly extensible, making it ideal for managing different authentication flows for each music service in a modular way.
- **Alternatives considered**: `requests-oauthlib`. Authlib is chosen for its broader scope and more modern API, which includes helpers for JWT, JWS, and other authentication-related standards.
