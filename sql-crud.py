from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create a class-based model for the "Programmer" table
# class Programmer(base):
#     __tablename__ = "Programmer"
#     id = Column(Integer, primary_key=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     gender = Column(String)
#     nationality = Column(String)
#     famous_for = Column(String)

# create a class-based model for the "Favourite Place" table
class FavouritePlace(base):
    __tablename__ = "FavouritePlace"
    id = Column(Integer, primary_key = True)
    city = Column(String)
    country = Column(String)
    capital = Column(String)
    population = Column(String)
    famous_for = Column(String)

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on our Progammer table
# ada_lovelace = Programmer(
#     first_name="Ada",
#     last_name="Lovelace",
#     gender="F",
#     nationality="British",
#     famous_for="First Programmer"
# )

# alan_turing = Programmer(
#     first_name="Alan",
#     last_name="Turing",
#     gender="M",
#     nationality="British",
#     famous_for="Modern Computing"
# )

# grace_hopper = Programmer(
#     first_name="Grace",
#     last_name="Hopper",
#     gender="F",
#     nationality="American",
#     famous_for="COBOL language"
# )

# margaret_hamilton = Programmer(
#     first_name="Margaret",
#     last_name="Hamilton",
#     gender="F",
#     nationality="American",
#     famous_for="Apollo 11"
# )

# bill_gates = Programmer(
#     first_name="Bill",
#     last_name="Gates",
#     gender="M",
#     nationality="American",
#     famous_for="Microsoft"
# )

# tim_berners_lee = Programmer(
#     first_name="Tim",
#     last_name="Berners-Lee",
#     gender="M",
#     nationality="British",
#     famous_for="World Wide Web"
# )

# gary_broderick = Programmer(
#     first_name="Gary",
#     last_name="Broderick",
#     gender="M",
#     nationality="Irish",
#     famous_for="Learning Something New"
# )

# creating records on our Favourite Place table
limerick = FavouritePlace(
    city="Limerick",
    country="Ireland",
    capital="Dublin",
    population="5 Million",
    famous_for="Guinness"
)

swansea = FavouritePlace(
    city="Swansea",
    country="Wales",
    capital="Cardiff",
    population="3 Million",
    famous_for="Rugby"
)

glasgow = FavouritePlace(
    city="Glasgow",
    country="Scotland",
    capital="Edinburgh",
    population="5.5 Million",
    famous_for="Whiskey"
)

birmingham = FavouritePlace(
    city="Birmingham",
    country="England",
    capital="London",
    population="56 Million",
    famous_for="Football"
)

bordeaux = FavouritePlace(
    city="Bordeaux",
    country="France",
    capital="Paris",
    population="66.5 Million",
    famous_for="Football"
)

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(gary_broderick)
# session.add(limerick)
# session.add(swansea)
# session.add(glasgow)
# session.add(birmingham)
# session.add(bordeaux)

# commit our session to the database
# session.commit()

# updating a single record
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "World President"

# updating a single record
# favouritePlace = session.query(FavouritePlace).filter_by(id=5).first()
# favouritePlace.famous_for = "Romance"

# commit our session to the database
# session.commit()

# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# updating multiple records
# places = session.query(FavouritePlace)
# for place in places:
#     if place.capital == "Cardiff":
#         place.country = "United Kingdom of Britain"
#     elif place.capital == "Paris":
#         place.country = "European Union"
#     else:
#         print("Capital not defined")
#     session.commit()

# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()

# deleting a single record
cityName = input("Enter a city: ")
favouritePlace = session.query(FavouritePlace).filter_by(city=cityName).first()

# defensive programming
if favouritePlace is not None:
    print("Favourite Place Found: ", favouritePlace.city)
    confirmation = input("Are you sure you want to delete this record? (y/n) ")
    if confirmation.lower() == "y":
        session.delete(favouritePlace)
        session.commit()
        print("Favourite Place has been deleted")
    else:
        print("Favourite Place not deleted")
else:
    print("No records found")

# query the database to find all Programmers
# programmers = session.query(Programmer)
# for programmer in programmers:
#     print(
#         programmer.id,
#         programmer.first_name + " " + programmer.last_name,
#         programmer.gender,
#         programmer.nationality,
#         programmer.famous_for,
#         sep=" | "
#     )

# query the database to find all Favourite Places
favouritePlaces = session.query(FavouritePlace)
for favouritePlace in favouritePlaces:
    print(
        favouritePlace.id,
        favouritePlace.city,
        favouritePlace.country + " , " + favouritePlace.capital,
        favouritePlace.population,
        favouritePlace.famous_for,
        sep = " | "
    )