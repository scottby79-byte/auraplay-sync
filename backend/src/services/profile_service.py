from backend.src.core.database import SessionLocal
from backend.src.models.profile import UserProfile, PlatformConfiguration
from backend.src.core.security import encrypt_data, decrypt_data

def get_all_profiles():
    db = SessionLocal()
    profiles = db.query(UserProfile).all()
    db.close()
    return profiles

def get_profile_by_id(profile_id: int):
    db = SessionLocal()
    profile = db.query(UserProfile).filter(UserProfile.id == profile_id).first()
    db.close()
    return profile

def create_profile(profile_data: dict):
    db = SessionLocal()
    # In a real app, credentials would be passed in and encrypted
    # For now, using placeholder credentials
    source_creds = encrypt_data("dummy_source_token")
    target_creds = encrypt_data("dummy_target_token")

    new_profile = UserProfile(name=profile_data['name'])
    
    source_config = PlatformConfiguration(
        platform_type='source',
        platform_name=profile_data['source_platform']['platform_name'],
        encrypted_credentials=source_creds
    )
    target_config = PlatformConfiguration(
        platform_type='target',
        platform_name=profile_data['target_platform']['platform_name'],
        encrypted_credentials=target_creds
    )

    new_profile.platform_configurations.append(source_config)
    new_profile.platform_configurations.append(target_config)
    
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
    db.close()
    return new_profile

def update_profile(profile_id: int, profile_data: dict):
    db = SessionLocal()
    profile = db.query(UserProfile).filter(UserProfile.id == profile_id).first()
    if not profile:
        db.close()
        return None

    profile.name = profile_data.get('name', profile.name)
    
    # Simplified update logic: remove old configs and add new ones
    for config in profile.platform_configurations:
        db.delete(config)
    
    source_creds = encrypt_data("dummy_source_token_updated")
    target_creds = encrypt_data("dummy_target_token_updated")

    source_config = PlatformConfiguration(
        platform_type='source',
        platform_name=profile_data['source_platform']['platform_name'],
        encrypted_credentials=source_creds
    )
    target_config = PlatformConfiguration(
        platform_type='target',
        platform_name=profile_data['target_platform']['platform_name'],
        encrypted_credentials=target_creds
    )

    profile.platform_configurations.append(source_config)
    profile.platform_configurations.append(target_config)

    db.commit()
    db.refresh(profile)
    db.close()
    return profile

def delete_profile(profile_id: int):
    db = SessionLocal()
    profile = db.query(UserProfile).filter(UserProfile.id == profile_id).first()
    if profile:
        db.delete(profile)
        db.commit()
        db.close()
        return True
    db.close()
    return False
