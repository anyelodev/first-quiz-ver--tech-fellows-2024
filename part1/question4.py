import pets_db

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/   
#                                                                          
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is 
# created in the file `pets_db.py`. 
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each 
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

sql_pets_owned_by_nobody = 

SELECT pet_name, species, age
FROM pets
WHERE owner_id IS NULL;


# Part 4.B:
# Write SQL to select how the number of pets are older than their owners. 
# The output should be an integer.

sql_pets_older_than_owner = 

SELECT COUNT(*) AS pet_count
FROM pets
JOIN people ON pets.owner_id = people.id
WHERE pets.age > people.age;



# Part 4.C: BONUS CHALLENGE! 
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)
sql_only_owned_by_bessie = 

SELECT people.name AS owner_name, pets.pet_name, pets.species
FROM pets
JOIN people ON pets.owner_id = people.id
WHERE pets.owner_id IN (
    SELECT id
    FROM people
    WHERE name = 'Bessie'
)
GROUP BY pets.owner_id, pets.pet_name, pets.species
HAVING COUNT(DISTINCT pets.owner_id) = 1;



