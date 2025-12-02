from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from backend.src.core.database import Base

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False, index=True)

    platform_configurations = relationship("PlatformConfiguration", back_populates="user_profile", cascade="all, delete-orphan")

class PlatformConfiguration(Base):
    __tablename__ = "platform_configurations"

    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("user_profiles.id"), nullable=False)
    platform_type = Column(String(10), nullable=False)  # 'source' or 'target'
    platform_name = Column(String(50), nullable=False)
    encrypted_credentials = Column(Text, nullable=False)

    user_profile = relationship("UserProfile", back_populates="platform_configurations")
