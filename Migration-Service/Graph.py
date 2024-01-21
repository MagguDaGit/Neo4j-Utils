import time

from neo4j import GraphDatabase


class Graph:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def execute_write(self, query):
        with self.driver.session() as session:
            print("-----------------------TRANSACTION START-----------------------------------")
            session.write_transaction(self._write_and_return, query)
            print("-----------------------TRANSACTION END-----------------------------------")

    def execute_write_and_return(self, query):
        with self.driver.session() as session:
            print("-----------------------TRANSACTION START-----------------------------------")
            result = session.write_transaction(self._write_and_return, query)
            if result is not None:
                return result
            else:
                print("Query returned no data")
                print("-----------------------TRANSACTION END-----------------------------------")
                return None

    @staticmethod
    def _write_and_return(tx, query):
        transaction_start_time = time.time()
        result = tx.run(query)
        transaction_end_time = time.time()
        # Accessing statistics after fetching the record(s)
        records = list(result)
        metadata = result.consume().metadata

        print(f"Ran query: \n {metadata.get('query')}")

        print("Query run generated following statistics:")
        print(f"Nodes created: {metadata.get('nodes-created')}")
        print(f"Relationships created: {metadata.get('relationships-created')}")
        print(f"Transaction runtime: {round(transaction_end_time - transaction_start_time, 6)} ms")

        if records:
            print("The following data was returned from query:")
            for record in records:
                print(record)
        else:
            print("Query returned no data")

        return records
