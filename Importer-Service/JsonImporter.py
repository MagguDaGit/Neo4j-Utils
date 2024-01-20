import json
import os

from Models.City import City
from Models.Country import Country
from Models.Person import Person


def import_countries(version):
    # Get the current script's directory
    script_directory = os.path.dirname(os.path.realpath(__file__))

    # Construct the correct path to .json
    json_path = os.path.join(script_directory, 'json', 'countries', 'countries.json')

    # Read data json
    with open(json_path, 'r') as file:
        data = json.load(file)

    # Extract
    countries = data.get('countries', [])

    for countryObject in countries:
        country = Country.create_country(code=countryObject['code'], name=countryObject["name"])
        country.save()


def import_cities(version):
    # Get the current script's directory
    script_directory = os.path.dirname(os.path.realpath(__file__))

    # Construct the correct path to .json
    json_path = os.path.join(script_directory, 'json', 'cities', 'cities.json')

    # Read data from .json
    with open(json_path, 'r') as file:
        data = json.load(file)

    # Extract data
    cities = data.get('cities', [])

    for cityObject in cities:
        City.create_city(name=cityObject["name"])


def import_people(version):
    # Get the current script's directory
    script_directory = os.path.dirname(os.path.realpath(__file__))

    # Construct the correct path to .json
    json_path = os.path.join(script_directory, 'json', 'people', 'people.json')

    # Read data from .json
    with open(json_path, 'r') as file:
        data = json.load(file)

    # Extract data
    people = data.get('people', [])

    for personObject in people:
        Person.create_person(name=personObject['name'], age=personObject['age'],
                             country_code=personObject['country_code'],
                             city_name=personObject['city'])


import_countries("1")
import_cities("1")
import_people("1")
