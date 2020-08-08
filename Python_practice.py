counties = ['Arapahoe','Denver','Jefferson']
if counties[1] == 'Denver':
    print(counties[1])

temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")    

#What is the score?
score = int(input('What is your test score?'))

#Determine the grade.
if score >= 90:
    print('Your grade is an A')
else:
    if score >= 80:
        print('Your grade is a B')
    else:
        if score >= 70:
            print('Your grade is a C')
        else:
            if score >= 60:
                print('Your grade is a D')
            else:
                print('Your grade is an F')

#What is the score?
score = int(input('What is your test score?'))

# Determine the grade
if score >= 90:
    print('Your grade is an A')
elif score >= 80:
    print('Ypur grade is a B')
elif score >= 70:
    print('Your grade is a C')
elif score >= 60:
    print('Your grade is a D')
else:
    print('Your score is an F')        

x = 0
while x <= 5:
    print (x)
    x = x + 1

for county in counties:
    print(county)

numbers = [0,1,2,3,4]
for num in numbers:
    print(num)

for num in range(9):
    print(num)


for i in range(len(counties)):    
    print(counties[i])


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for county in counties_dict:
    print(counties_dict.get(county))


for county, voters in counties_dict.items():
    print(county,voters) 


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])        

print ("Arapahoe and Denver are not in the list of counties")

interest = str
print("Your interest for the year is $" + str(2))


my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes")


my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")


counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jeferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")


for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total votes in the election?"))
message_to_candidate = (f"You received {candidate_votes:,} number of votes."
                        f"The total number of votes in the election was {total_votes:,} "
                        f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes")

print(message_to_candidate)                        


# Import the datetime class from the datetime modole
import datetime
# Use the now() attribute on the datetime class to get the present time
now = datetime.datetime.now()
# Print the present time
print("The time right now is ", now)


dir({'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438})

dir(int)
dir(float)

dir(csv)


import csv
dir(csv)

dir(csv)

#The data we need to retrieve.
# 1. The total number of votes cast
# 2. A comlplete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular votes


dir(csv)

# Assign a variable for the file to load and the path.
file_to_load = 'Resources\election_results.csv'

# Open the election results and read the file. 
election_data = open(file_to_load, 'r')

# To do: perfomr analysis.

# Close the file.
election_data.close()


# Open the election resuts and read the file
with open(file_to_load) as election_data:

    # To do: perfimr analysis.
    print(election_data)


import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election  results and read the file
with open(file_to_load) as election_data:

    #Print the file object
    print(election_data)


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")   


# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Using the with statment open the file as a text file
outfile = open(file_to_save, "w")
# Write some data to the file 
outfile.write("Hello World")

#Close the file
outfile.close()

#------------
# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file 
with open(file_to_save, "w") as txt_file:

    ## Write some data to the file
    
    # Write three counties to the file.
    txt_file.write("Counties in the election\n--------------------------\nArapahoe\nDenver\nJefferson")
    