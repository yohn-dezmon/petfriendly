from sqlalchemy_declarative import Person, Base, Address
from sqlalchemy import create_engine
engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()
# Make a query to find all Persons in the database
session.query(Person).all()
[<sqlalchemy_declarative.Person object at 0x2ee3a10>]
# Return the first Person from all Persons in the database
person = session.query(Person).first()
print(person.name)


# Find all Address whose person field is pointing to the person object
session.query(Address).filter(Address.person == person).all()
[<sqlalchemy_declarative.Address object at 0x2ee3cd0>]
# Retrieve one Address whose person field is point to the person object
session.query(Address).filter(Address.person == person).one()
<sqlalchemy_declarative.Address object at 0x2ee3cd0>
address = session.query(Address).filter(Address.person == person).one()
address.post_code
