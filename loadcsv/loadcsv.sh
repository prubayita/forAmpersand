#!/bin/bash

# Load the places.csv file into the places table
psql -U postgres -d mydatabase -c "\copy places(city, county, country) FROM '/data/places.csv' DELIMITER ',' CSV HEADER;"

# Load the people.csv file into the people table
psql -U postgres -d mydatabase -c "\copy people(first_name, last_name, date_of_birth, city_of_birth) FROM '/data/people.csv' DELIMITER ',' CSV HEADER;"
