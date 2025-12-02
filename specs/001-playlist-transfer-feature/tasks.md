# Tasks: Playlist Transfer Feature

**Input**: Design documents from `/specs/001-playlist-transfer-feature/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Project Setup

**Purpose**: Initialize the backend and frontend projects with basic boilerplate.

- [x] T001 [P] Initialize the main Flask application structure in `backend/src/app.py`.
- [x] T002 [P] Initialize the main React application in `frontend/src/index.js` and `frontend/src/App.js`.
- [x] T003 [P] Configure linting and formatting tools for both Python (e.g., Black, Flake8) and JavaScript (e.g., ESLint, Prettier).
- [x] T004 Review and confirm Docker configurations in `docker-compose.yml`, `Dockerfile.backend`, and `Dockerfile.frontend`.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented.

- [x] T005 [P] Implement the database setup logic in `backend/src/core/database.py` using SQLAlchemy.
- [x] T006 [P] Implement the credential encryption/decryption service in `backend/src/core/security.py` using the `ENCRYPTION_KEY`.
- [x] T007 Implement the `UserProfile` and `PlatformConfiguration` SQLAlchemy models in `backend/src/models/profile.py` based on the data model.
- [x] T008 [P] Set up the basic MUI theme and a global layout component in `frontend/src/theme.js` and `frontend/src/components/Layout.js`.
- [x] T009 [P] Set up basic frontend routing using a library like React Router in `frontend/src/App.js`.
- [x] T010 [P] Create a generic API service client in `frontend/src/services/api.js` to communicate with the backend.

---

## Phase 3: User Story 1 - Profile Creation and Management (Priority: P1) 🎯 MVP

**Goal**: Allow users to create, view, update, and delete connection profiles.
**Independent Test**: A user can create a profile with a source and target platform, see it on a list, edit it, and delete it.

### Implementation for User Story 1

- [x] T011 [P] [US1] Implement the `/api/platforms` endpoint in `backend/src/api/platforms.py` to return the list of supported platforms.
- [x] T012 [P] [US1] Implement the CRUD endpoints for `/api/profiles` in `backend/src/api/profiles.py`.
- [x] T013 [US1] Implement the business logic for profile management in `backend/src/services/profile_service.py`, using the security service for credentials.
- [x] T014 [P] [US1] Create the main profiles dashboard page in `frontend/src/pages/DashboardPage.js`.
- [x] T015 [P] [US1] Create a `ProfileList` component in `frontend/src/components/ProfileList.js` to display all user profiles.
- [x] T016 [P] [US1] Create a `ProfileForm` component in `frontend/src/components/ProfileForm.js` for creating and editing profiles.
- [x] T017 [US1] Integrate the frontend components to allow full CRUD management of profiles, calling the backend API via the `api.js` service.

---

## Phase 4: User Story 2 - Playlist/Album Transfer (Priority: P1)

**Goal**: Allow users to select a profile and transfer entire playlists or albums from the source to the target platform.
**Independent Test**: A user can select a profile, view their source playlists, and successfully trigger a transfer for a selected playlist.

### Implementation for User Story 2

- [x] T018 [P] [US2] Create a modular structure for platform clients in `backend/src/services/platforms/`.
- [x] T019 [P] [US2] Implement a base platform client class in `backend/src/services/platforms/base.py`.
- [x] T020 [US2] Implement the client for the first platform (e.g., Spotify) in `backend/src/services/platforms/spotify_client.py`, including authentication and playlist fetching.
- [x] T021 [US2] Implement the `/api/profiles/{profileId}/source/playlists` endpoint in `backend/src/api/playlists.py`.
- [x] T022 [US2] Implement the `/api/profiles/{profileId}/transfer` endpoint, creating a background job for the transfer logic.
- [x] T023 [US2] Implement the transfer logic in `backend/src/services/transfer_service.py` to handle playlist replication.
- [x] T024 [P] [US2] Create the main transfer UI page in `frontend/src/pages/TransferPage.js`.
- [x] T025 [P] [US2] Create a `SourcePlaylistPanel` component in `frontend/src/components/SourcePlaylistPanel.js` to display source playlists.
- [x] T026 [P] [US2] Create a `TargetPlaylistPanel` component in `frontend/src/components/TargetPlaylistPanel.js` to display target playlists.
- [x] T027 [US2] Implement the UI logic to select items and trigger the `/api/transfer` endpoint.

---

## Phase 5: User Story 3 - Granular Track Transfer (Priority: P2)

**Goal**: Allow users to select individual tracks for transfer into new or existing target playlists.
**Independent Test**: A user can expand a source playlist, select specific tracks, and transfer them to a target playlist.

### Implementation for User Story 3

- [x] T028 [US3] Update the platform client logic in `backend/src/services/platforms/` to include fetching tracks for a playlist.
- [x] T029 [US3] Update the `transfer_service.py` and the `/api/transfer` endpoint to accept and process individual track transfer requests.
- [x] T030 [US3] Add a "Create Playlist" button to the `TargetPlaylistPanel` component in the frontend.
- [x] T031 [US3] Implement a `TrackList` component in `frontend/src/components/TrackList.js` that appears when a source playlist is expanded.
- [x] T032 [US3] Update the frontend transfer logic to allow track-level selection and transfer.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and finalize the application.

- [x] T033 Implement the generation and download of the transfer report in `backend/src/services/transfer_service.py`.
- [x] T034 Implement a notification system in the frontend to show transfer progress and completion/error status.
- [x] T035 Add comprehensive error handling and user-friendly feedback across the entire application.
- [x] T036 Write a final, detailed `README.md` for the project root.
- [x] T037 Perform a security review of the backend, especially around credential handling.
- [x] T038 [P] Write unit tests for critical business logic in the backend services.
- [x] T039 [P] Write component tests for the main React components in the frontend.

---

## Dependencies & Execution Order

- **Setup (Phase 1)** can start immediately.
- **Foundational (Phase 2)** depends on Setup completion and blocks all user stories.
- **User Stories (Phase 3+)**: All depend on Foundational phase completion. The recommended order is **US1 -> US2 -> US3**.
- **Polish (Phase 6)** depends on all desired user stories being complete.

---

## Implementation Strategy

### MVP First (User Story 1)

The suggested Minimum Viable Product (MVP) is the completion of **Phases 1, 2, and 3**. This will deliver a functional application that allows users to securely set up and manage their connection profiles, which is the core prerequisite for all other features.

### Incremental Delivery

After the MVP, **Phase 4 (US2)** can be completed to add the primary feature of whole-playlist transfers. **Phase 5 (US3)** can follow as a feature enhancement. **Phase 6** should be an ongoing effort, with critical parts (like error handling) integrated during each phase.
