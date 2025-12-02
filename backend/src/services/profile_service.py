from core.database import SessionLocal
from models.profile import UserProfile, PlatformConfiguration
from core.security import encrypt_data, decrypt_data

def get_all_profiles():
    db = SessionLocal()
    profiles = db.query(UserProfile).all()
    # Force load platform_configurations for each profile before closing session
    for profile in profiles:
        _ = profile.platform_configurations 
    db.close()
    return profiles

def get_profile_by_id(profile_id: int):
    db = SessionLocal()
    profile = db.query(UserProfile).filter(UserProfile.id == profile_id).first()
    if profile:
        # Force load platform_configurations before closing session
        _ = profile.platform_configurations
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
    # Force load platform_configurations before closing session
    _ = new_profile.platform_configurations
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
    # Force load platform_configurations before closing session
    _ = profile.platform_configurations
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
