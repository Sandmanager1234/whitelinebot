import os

from classes.db_manager import ManagerBD

DBNAME = os.getenv('DB_NAME')
USERNAME = os.getenv('DB_USERNAME')
USER_PASSWORD = os.getenv('DB_USERNAME_PASSWORD')

db_manager = ManagerBD(dbname=DBNAME, dbuser=USERNAME, user_password=USER_PASSWORD)

# a = [(519959965,), (5315238849,)]
a = db_manager.get_stuff()
print((519959965,) in a)