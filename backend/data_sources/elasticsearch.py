from elasticsearch import Elasticsearch

# Initialize the Elasticsearch client
es = Elasticsearch(['http://localhost:9200'])

def get_user_logs(user_id):
    """Fetches user logs from an Elasticsearch index."""
    query_body = {
        "query": {
            "match": {
                "user_id": user_id
            }
        }
    }
    # Perform the search query on the "user_logs" index
    response = es.search(index="user_logs", body=query_body)
    # Extract and return the source data from the hits
    return [hit['_source'] for hit in response['hits']['hits']]


# Explanation:
#
#     Elasticsearch: The Elasticsearch client is imported from the elasticsearch Python package.
#     es: This variable initializes the Elasticsearch client, connecting to a local Elasticsearch instance running at http://localhost:9200.
#     get_user_logs(user_id): This function searches the user_logs index for logs associated with the provided user_id. The search query uses a match query on the user_id field. The function returns the logs as a list of dictionaries extracted from the search results.
#
# This script handles the retrieval of unstructured data from an Elasticsearch index, making it available for inclusion in your GraphQL API responses.