import graphene
from resolvers import Query

schema = graphene.Schema(query=Query)

# Explanation:
#
#     graphene is a Python library used to create GraphQL schemas.
#     The Query class is imported from the resolvers.py file, which defines the queryable fields and their resolvers.
#     The schema variable is created by passing the Query class to graphene.Schema, establishing the structure of
#     the GraphQL schema.
#
# This schema.py file ties together the resolvers (which define how data is fetched) with the GraphQL schema,
# making it possible to serve this schema via the Flask app.