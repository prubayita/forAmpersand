import json
from sqlalchemy import create_engine, Column, Integer, String, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Place(Base):
    __tablename__ = 'places'
    city = Column(String, primary_key=True)
    county = Column(String)
    country = Column(String)

class Person(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(String)
    city_of_birth = Column(String)

# Connect to the database
engine = create_engine('postgresql://postgres:postgres@localhost:5432/ampersand')
Session = sessionmaker(bind=engine)
session = Session()

# Query the summary data
result = session.query(Place.country, func.count(Person.id)).join(Person, Place.city == Person.city_of_birth).group_by(Place.country).all()

# Convert the result to a dictionary
result_dict = {row[0]: row[1] for row in result}

# Write the result to a file in JSON format
with open('summary_output.json', 'w') as f:
    f.write(json.dumps(result_dict))
