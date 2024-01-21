from MinimalGraph import MinimalGraph

graph = MinimalGraph("bolt://localhost:7687", "neo4j", "neo4jutil")


# TEST UTILS
def get_all_nodes_count():
    return len(graph.run_query("MATCH(n) RETURN n"))


def get_orphaned_persons():
    query = """
            MATCH (n:Person)
            WHERE NOT EXISTS((n)-[:IS_FROM]->()) 
            RETURN n
            """
    return len(graph.run_query(query))


def get_city_not_in_country():
    query = """
            MATCH (n:City)
            WHERE NOT EXISTS((n)-[:IN_COUNTRY]->()) 
            RETURN n
            """
    return len(graph.run_query(query))


# TESTS SUITES
def test_right_amount_of_nodes():
    assert get_all_nodes_count() == 30


def test_no_orphaned_people():
    assert test_right_amount_of_nodes() is None


def test_no_city_not_in_country():
    assert get_city_not_in_country() == 0


graph.close()
