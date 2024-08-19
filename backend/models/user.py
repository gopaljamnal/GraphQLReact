import graphene
from graphene import ObjectType, String, Int, List

class ActivityType(ObjectType):
    activity = String()
    timestamp = String()

class LogType(ObjectType):
    message = String()
    timestamp = String()

class ProfileType(ObjectType):
    id = Int()
    name = String()
    email = String()

class UserType(ObjectType):
    profile = graphene.Field(ProfileType)
    activities = List(ActivityType)
    logs = List(LogType)


# Explanation:
#
#     ActivityType: Represents a user's activity with fields for activity and timestamp.
#     LogType: Represents a log entry with fields for message and timestamp.
#     ProfileType: Represents a user's profile with fields for id, name, and email.
#     UserType: Combines all the above types. It has three fields:
#         profile: Uses the ProfileType.
#         activities: A list of ActivityType entries.
#         logs: A list of LogType entries.
#
# The UserType class models the aggregated data structure that will be returned when querying for user data.