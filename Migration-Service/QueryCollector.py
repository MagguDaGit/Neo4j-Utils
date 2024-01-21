import os


class QueryCollector:
    def __init__(self):
        self.script_folder = "scripts"  # Change this to your script folder name
        self.query_array = []

    def collect_queries(self):
        # Get the current directory
        current_directory = os.path.dirname(os.path.abspath(__file__))
        script_folder_path = os.path.join(current_directory, self.script_folder)
        print(f"Lookup in {script_folder_path} for potential CQL scripts")
        # Check if the script folder exists
        if not os.path.exists(script_folder_path):
            print(f"Error: Script folder '{self.script_folder}' not found.")
            return

        # Iterate through each file in the script folder
        for filename in os.listdir(script_folder_path):
            file_path = os.path.join(script_folder_path, filename)

            # Check if the file is a CQL file
            if filename.endswith(".cql") and os.path.isfile(file_path):
                # Read the entire content of the CQL file as a single query
                with open(file_path, "r") as file:
                    query = file.read().strip()

                    # Add the query to the array
                    self.query_array.append(query)
        print("---------------QUERIES FOUND IN Scripts---------------------------")
        for i, query in enumerate(self.query_array, start=1):
            print(f"\n {i} Query: ")
            print(query)
            print("\n")
        print("------------------------------------------")

    def get_queries(self):
        return self.query_array
# Example usage
# if __name__ == "__main__":
#    query_collector = QueryCollector()
#    query_collector.collect_queries()
#
#    queries = query_collector.get_queries()
#    for i, query in enumerate(queries, start=1):
#        print(f"Query {i}:\n{query}\n")
