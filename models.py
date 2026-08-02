from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    favorites = relationship(
        "FavoriteCity",
        back_populates="owner"
    )

class FavoriteCity(Base):
    
    __tablename__ = "favorite_cities"
    id = Column(Integer, primary_key=True, index=True)
    city_name = Column(String, index=True)
    latitude = Column(String)
    longitude = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship(
        "User", 
        back_populates="favorites"
    )