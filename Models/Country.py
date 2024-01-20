from neomodel import StructuredNode, StringProperty, DoesNotExist


class Country(StructuredNode):
    code = StringProperty(unique_index=True, required=True)
    name = StringProperty(unique_index=True)

    @classmethod
    def create_country(cls, code, name):
        try:
            # Try to get the existing country with the given code
            existing_country = cls.nodes.filter(code=code).first()

            # If it exists, return the existing country
            return existing_country
        except DoesNotExist:
            # If it does not exist, create and save the new country
            new_country = cls(code=code, name=name).save()
            print(f"Country '{name}' with code '{code}' created.")
            return new_country

# Example usage:
# new_country_1 = Country.create_country(code="US", name="United States")
# new_country_2 = Country.create_country(code="US", name="United States")
