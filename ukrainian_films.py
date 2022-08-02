import csv
from csv import writer

filename = "ukrainian_movie.csv"

# Read CSV file
film_notes = []
with open(filename, mode ='r')as file:
    f = csv.reader(file)
    for lines in f:
        film_notes.append(lines)

# Write new note to the file
# note = ['Fruit','Wealthy couple tries to buy new apricots',1]
# with open(filename, 'a') as filek:
#     writer_object = writer(filek)
#     writer_object.writerow(note)
#     filek.close()

# Print all notes
print("Notes: ")
for i in film_notes:
    print(i)
print(" ")

# Standartization
all_rates = []
for i in range(len(film_notes)):
    film_notes[i][2] = int(film_notes[i][2])
    all_rates.append(film_notes[i][2])

# Find films with highest rating
print("List of films  with highest rating: ")
print("---------------------------")
for i in range(len(film_notes)):
    if (film_notes[i][2] == 5):
        print(film_notes[i][0])
print(" ")

# Find films with lowest rating
print("List of films with lowest rating: ")
print("---------------------------")
for i in range(len(film_notes)):
    if (film_notes[i][2] == 1):
        print(film_notes[i][0])
print(" ")

# Find average rating among all film
average = sum(all_rates) / len(all_rates)
print("Average rating among all films equals:", round(average))
