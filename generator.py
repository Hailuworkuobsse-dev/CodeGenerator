import sqlalchemy as sa
from jinja2 import Environment, FileSystemLoader

# Parse the database schema
engine = sa.create_engine('your_database_uri')
metadata = sa.MetaData(bind=engine)
metadata.reflect()

# Define Jinja2 templates
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('sql_query_template.jinja2')

# Generate code for each table
for table in metadata.tables.values():
    columns = [column.name for column in table.columns]
    generated_code = template.render(table_name=table.name, columns=columns)
    print(generated_code)
