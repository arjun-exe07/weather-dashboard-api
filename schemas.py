from pydantic import BaseModel, Field

#Request Schema
class UserCreate(BaseModel):
    username: str = Field(min_length = 3, max_length=50)
    password: str = Field(min_length=6, max_length=100)

#Response Schema
class UserResponse(BaseModel):
    id: int
    username: str
    class Config:
        from_attributes = True

#Response Schema
class Token(BaseModel):
    access_token: str
    token_type: str

#Request Schema
class FavoriteCityCreate(BaseModel):
    city_name: str
    latitude: str
    longitude: str

#Response Schema
class FavoriteCityResponse(BaseModel):
    id: int
    city_name: str
    latitude: str
    longitude: str
    class Config:
        from_attributes = True

#Response Schema
class WeatherResponse(BaseModel):
    city: str
    temperature: float
    windspeed: float
    weathercode: int
    fetched_at: str
