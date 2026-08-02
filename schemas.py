from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    username: str = Field(min_length = 3, max_length=50)
    password: str = Field(min_length=6, max_length=100)

class UserResponse(BaseModel):
    id: int
    username: str
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class FavoriteCityCreate(BaseModel):
    city_name: str
    latitude: str
    longitude: str

class FavoriteCityResponse(BaseModel):
    id: int
    city_name: str
    latitude: str
    longitude: str
    class Config:
        from_attributes = True

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    windspeed: float
    weathercode: int
    fetched_at: str
