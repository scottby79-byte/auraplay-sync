# AuraPlay-Sync Data Model

This document defines the data structures for the AuraPlay-Sync application, based on the entities identified in the feature specification. The model will be implemented using SQLAlchemy with a SQLite database.

## Entity Relationship Diagram (Conceptual)

```
+----------------+      +-------------------------+
|   User Profile |------| Platform Configuration  |
| (One-to-Many)  |      | (Belongs to one Profile)|
+----------------+      +-------------------------+
| id             |      | id                      |
| name           |      | profile_id (FK)         |
+----------------+      | platform_name           |
                        | encrypted_credentials   |
                        +-------------------------+
```

## Entity Definitions

### 1. UserProfile

Represents a user's named configuration for a specific transfer setup (e.g., "My Spotify to Deezer"). A user can have multiple profiles.

-   **Table Name**: `user_profiles`

| Field | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `Integer` | Primary Key, Autoincrement | Unique identifier for the profile. |
| `name` | `String(100)` | Not Null, Unique | A user-defined name for the profile. |

-   **Relationships**:
    -   Has a one-to-many relationship with `PlatformConfiguration`. Deleting a `UserProfile` will cascade and delete all its associated `PlatformConfiguration` records.

### 2. PlatformConfiguration

Represents the settings for a single streaming platform (either source or target) within a `UserProfile`.

-   **Table Name**: `platform_configurations`

| Field | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | `Integer` | Primary Key, Autoincrement | Unique identifier for the platform setting. |
| `profile_id` | `Integer` | Foreign Key (`user_profiles.id`), Not Null | Links this configuration to a `UserProfile`. |
| `platform_type`| `String(10)`| Not Null | The type of platform, either 'source' or 'target'. |
| `platform_name`| `String(50)`| Not Null | The name of the streaming service (e.g., 'Spotify', 'Deezer'). |
| `encrypted_credentials` | `Text` | Not Null | The user's authentication credentials (e.g., OAuth2 refresh token), stored in an encrypted format. |

-   **Relationships**:
    -   Belongs to one `UserProfile`.

## Security Note

The `encrypted_credentials` field is critical. The application backend will use a symmetric encryption key (configured via an environment variable, not stored in the repository) to encrypt and decrypt these credentials before use and before storing them in the database. This prevents direct exposure of user tokens should the database file be compromised.
