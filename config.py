# Database
db_user = 'testuser'
db_password = 'test'
db_addr = 'localhost'
db_name = 'zalando'

db_uri_temp =  "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}"
SQLALCHEMY_DATABASE_URI =db_uri_temp.format(
        DB_USER=db_user,
        DB_PASS=db_password,
        DB_ADDR=db_addr,
        DB_NAME=db_name)

SQLALCHEMY_TRACK_MODIFICATIONS = True
