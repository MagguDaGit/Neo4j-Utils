from Graph import Graph
from QueryCollector import QueryCollector

graph = Graph("bolt://localhost:7687", "neo4j", "neo4jutil")


def run_migrations():
    print("Staring migrations....")
    query_collector = QueryCollector()
    query_collector.collect_queries()

    queries = query_collector.get_queries()
    for i, query in enumerate(queries, start=1):
        graph.execute_write(query)


run_migrations()
graph.close()
print("Migrations finished")
