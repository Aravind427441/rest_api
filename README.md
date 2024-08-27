ABSTRACT:
This project aims to build a mock Youtube API by building a RESTful API using Flask and Python to create, retrieve, update, and delete video records in a SQLite database. It uses SQLAlchemy for database interactions and Flask-RESTful for creating the API endpoints.

BRIEF CODE DESCRIPTION:
main.py:
• Imported all the necessary modules.
• Defined a class for the Database Model.
• Defined two request parsers to specify the arguments for PUT and PATCH requests.
• Defined a dictionary (resource_fields) which specfies that the instances should be serialized.
• Defined a class which contains all the functions for the resources i.e. GET, PUT, PATCH, DELETE
test.py:
• Used for testing the API
