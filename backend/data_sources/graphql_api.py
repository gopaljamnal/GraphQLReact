from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# Configure the transport with the external GraphQL API URL
transport = RequestsHTTPTransport(
    url="https://api.example.com/graphql",
    verify=True,
    retries=3,
)
# Create a GraphQL client
client = Client(transport=transport, fetch_schema_from_transport=True)

def get_recent_activities(user_id):
    """Fetches recent activities for a user from an external GraphQL API."""
    query = gql("""
    query($userId: ID!) {
        recentActivities(userId: $userId) {
            activity
            timestamp
        }
    }
    """)
    variables = {"userId": user_id}
    response = client.execute(query, variable_values=variables)
    return response['recentActivities']


# Explanation:
#
#     gql and Client: These are imported from the gql library to construct and send GraphQL queries.
#     RequestsHTTPTransport: This transport layer is configured to communicate with an external GraphQL API.
#     client: The GraphQL client is instantiated with the specified transport.
#     get_recent_activities(user_id): This function sends a GraphQL query to the external API to fetch recent activities for a user based on their user_id. The query is constructed using gql, and the response is returned as a list of activities.
#
# This script handles fetching semi-structured data from an external GraphQL API, integrating it with your GraphQL server.