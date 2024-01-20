from neomodel import (StructuredNode, StringProperty, IntegerProperty,
                      UniqueIdProperty, RelationshipTo, DoesNotExist)

from Models.City import City
from Models.Country import Country


class Person(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)

    # traverse outgoing IS_FROM relations, inflate to Country objects
    country = RelationshipTo(Country, 'IS_FROM')

    # traverse outgoing LIVES_IN relations, inflate to City objects
    city = RelationshipTo(City, 'LIVES_IN')

    @classmethod
    def create_person(cls, name, age, country_code, city_name):
        # Person is already in the database
        try:
            print("CREATING PERSON....")
            existing_person = cls.nodes.filter(name=name).first()
            return existing_person
        except DoesNotExist:
            # Not present in database, we save
            from_country = Country.nodes.get(code=country_code)
            from_city = City.nodes.get(name=city_name)
            new_person = cls(name=name, age=age)
            new_person.save()
            new_person.country.connect(from_country)
            new_person.city.connect(from_city)
            print(f"Person: '{name}' has been created/saved")
            return new_person
