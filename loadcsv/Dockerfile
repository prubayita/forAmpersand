FROM postgres:14

#copy csv files to the container
COPY places.csv /data/places.csv
COPY people.csv /data/people.csv


#set the working directory ro /data
WORKDIR /data

# set environement variables for the postgresql username and password
ENV POSTGRES_USER=postgres
ENV POSTGRES_USER=postgres

#run the script to load the csv files into the database
COPY load_csv.sh /docker-entrypoint-initdv.d/



#docker run -d --name loadcsv-container -p 5432:5432 loadcsv
