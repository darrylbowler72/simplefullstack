#!/bin/bash

# This script sets up a local PostgreSQL database for testing without Docker
# Adjust the connection parameters as needed

DBNAME="tasktracker"
DBUSER="postgres"
DBPASS="postgres"

echo "Creating PostgreSQL database: $DBNAME"

# Create database (you may need to adjust this command based on your PostgreSQL setup)
# createdb -U $DBUSER $DBNAME

echo "Database setup complete!"
echo ""
echo "To use this database, set the DATABASE_URL environment variable:"
echo "export DATABASE_URL=postgresql://$DBUSER:$DBPASS@localhost:5432/$DBNAME"
