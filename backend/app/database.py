from databases import Database

DATABASE_URL = "mysql+pymysql://myuser:mypassword@db:3306/travel_dev"
database = Database(DATABASE_URL)
