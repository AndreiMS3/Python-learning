
import csv

with open("movies.csv", "r") as file:
    csv_reader = csv.reader(file)  # Pass the file object, not a string
    header = next(csv_reader)  # Skip the header
    #Variables
    max_rate = 0
    best_rated_movie = None
    
    
    for line in csv_reader:
        if len(line) >= 4: 
            rate = float(line[3])
            if rate > max_rate:
                max_rate = rate
                best_rated_movie = line
               
with open("movies.csv", "r") as file:
    csv_reader = csv.reader(file)  # Pass the file object, not a string
    header = next(csv_reader)  # Skip the header
    #Variables
    max_votes= 0
    most_voted_movie = None
                   
    for line in csv_reader:
        if len(line) >= 5:  
            votes = int(line[4])
            if votes> max_votes:
                max_votes = votes
                most_voted_movie = line       

with open("top_movies.csv","w", newline="") as output_file:
    csv_writer= csv.writer(output_file)
    output_file.write("Category,Title,Year,Genre,Rating,Vote\n")
    output_file.write(f"Best-rated movie,{best_rated_movie}\n")
    output_file.write(f"Most voted movie,{most_voted_movie}\n")
    
  
