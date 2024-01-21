from neomodel import config

print("Initializing database connection...")
config.DATABASE_URL = 'bolt://neo4j:neo4jutil@localhost:7687'  # default
