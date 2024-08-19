from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select

# Create the engine, which connects to the SQLite database
engine = create_engine('sqlite:///users.db', echo=True)

# Initialize the MetaData without the `bind` argument
metadata = MetaData()

# Define the user table
users_table = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('email', String, nullable=False),
)

# If the table doesn't exist, create it
metadata.create_all(engine)

# Function to get user profile data
def get_user_profile(user_id):
    with engine.connect() as connection:
        stmt = select([users_table]).where(users_table.c.id == user_id)
        result = connection.execute(stmt).fetchone()

        if result:
            return {
                'id': result['id'],
                'name': result['name'],
                'email': result['email'],
            }
        else:
            return None
