from neo4j import GraphDatabase


class MinimalGraph:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        if self.driver:
            self.driver.close()

    def get_all_nodes_count(self):
        query = "MATCH (n) RETURN n"
        with self.driver.session() as session:
            result = session.read_transaction(self._execute, query)
            record = result.single()  # Get a single record to consume the result

        return result.consume().counters.nodes_created

    def run_query(self, query):
        with self.driver.session() as session:
            result = session.execute_read(self._execute, query)
            return result

    @staticmethod
    def _execute(tx, query):
        result = tx.run(query)
        return list(result)
