from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base
from models.review import Review

# Define the association table for the many-to-many relationship
place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True)
)

class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    # Define the many-to-many relationship with amenities
    amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)

    # Define the one-to-many relationship with reviews
    reviews = relationship("Review", backref="place", cascade="all, delete-orphan")

    @property
    def reviews(self):
        """Getter attribute for reviews"""
        return [review for review in self.reviews if review.place_id == self.id]

    @property
    def amenities(self):
        """Getter attribute for amenities"""
        return self.amenities

    @amenities.setter
    def amenities(self, obj):
        """Setter attribute for amenities"""
        if isinstance(obj, Amenity):
            self.amenities.append(obj.id)
