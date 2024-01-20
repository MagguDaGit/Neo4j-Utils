from neomodel import StructuredNode, StringProperty, DoesNotExist, RelationshipTo

from Models import Country


class City(StructuredNode):
    name = StringProperty(required=True)
    country = RelationshipTo(Country, 'FROM_COUNTRY')

    @classmethod
    def create_city(cls, name):
        try:
            existing_city = cls.nodes.filter(name=name).first()
            # If it exists, return the existing city
            return existing_city
        except DoesNotExist:
            # If it does not exist, create and save the new city
            new_city = cls(name=name).save()
            print(f"City '{name}' created.")
            return new_city
