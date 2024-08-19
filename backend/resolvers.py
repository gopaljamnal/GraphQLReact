import strawberry
from data_sources.database import get_user_profile
from data_sources.graphql_api import get_recent_activities
from data_sources.elasticsearch import get_user_logs

@strawberry.type
class ProfileType:
    id: int
    name: str
    email: str

@strawberry.type
class ActivityType:
    activity: str
    timestamp: str

@strawberry.type
class LogType:
    message: str
    timestamp: str

@strawberry.type
class UserType:
    profile: ProfileType
    activities: list[ActivityType]
    logs: list[LogType]

@strawberry.type
class Query:
    @strawberry.field
    def user_data(self, user_id: int) -> UserType:
        profile = get_user_profile(user_id)
        activities = get_recent_activities(user_id)
        logs = get_user_logs(user_id)

        return UserType(
            profile=profile,
            activities=activities,
            logs=logs
        )
