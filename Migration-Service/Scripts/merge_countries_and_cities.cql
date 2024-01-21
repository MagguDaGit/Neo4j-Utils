MATCH(p:Person)
MATCH(country:Country)<-[:IS_FROM]-(p)
MATCH(city:City)<-[:LIVES_IN]-(p)
MERGE (city)-[:IN_COUNTRY]->(country)
RETURN city, country