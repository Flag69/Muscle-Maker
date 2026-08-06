from app.database.db import drop_tables, create_tables

drop_tables()
create_tables()

print("Database reset !")