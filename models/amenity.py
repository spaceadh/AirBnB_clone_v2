from sqlalchemy import Column, String
from models.base_model import BaseModel, Base

class Amenity(BaseModel, Base):
    """The Amenity class, contains the amenity name"""

    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
