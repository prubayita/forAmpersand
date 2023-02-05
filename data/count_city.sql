select places.country, count(people.id) 
from places
join people on places.city = people.city_of_birth
group by places.country;