import os

host = os.environ['POSTGRES_HOST']
port = os.environ['POSTGRES_PORT']
user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
database = os.environ['POSTGRES_DB']

# user = 'postgres'
# password = 'postgres'
# host = '192.168.1.121'
# database = 'books'
# port = 5432


DATABASE_CONNECTION_URI = f'postgresql://{user}:{password}@{host}:{port}/{database}'