from flask import Flask
from strawberry.flask.views import GraphQLView
from resolvers import Query  # Import your query resolvers
import strawberry

schema = strawberry.Schema(query=Query)

app = Flask(__name__)

app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql_view", schema=schema),
)

if __name__ == "__main__":
    app.run(debug=True)


#
# Explanation:
#
#     Flask is used to create the web server.
#     The /graphql endpoint is configured to serve GraphQL queries using GraphQLView.
#     The GraphiQL interface is enabled for easier query testing.
#     The schema is imported from the schema.py file, which defines the structure of the GraphQL API.
#
# This app.py file sets up the server and exposes the GraphQL API at the /graphql endpoint