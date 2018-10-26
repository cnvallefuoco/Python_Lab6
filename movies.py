movie = ""
release = ""
budget = 0
gross= 0
profit = 0
letter= ""
test_profit = 0
test_title = ""
input_file = "movies.csv"

print("This program is designed to analyze data of over 4000 movies, their release dates, "
      "\ntheir budget,and their box office gross .It will analyze data from one input "
      "\nfile and write to two different output files, calculating profit and searching for "
      "\nmovies starting with specific letters."
      "\n\nThe last feature of this program will output the movie title and profit of the"
      "\nhighest profit movie in the input file. ")
print("")

while True:

   try:
       in_file = input ("Please enter the input file you would like to open: ")
       if in_file == "":
           input_file = open ("movies.csv", "r")
       else:
           input_file = open(in_file,"r")

   except IOError:
       print ("Error: File does not appear to exist.")
       continue
   else:
       break

profit_in_file = input("Please enter the name of the output file you wish to write to for profit: ")
profit_file = open (profit_in_file , "w")

letter_in_file = input ("Please enter the output file you wish to write to for the starting letter of the movie: ")
letter_file = open (letter_in_file , "w")

letter= input ("Enter the starting letter the  of movie(s) you wish to search: ")

for line in input_file:
    release , movie , budget , gross = line.split (",")
    profit = (int(gross) - int(budget))
    print(release, ",", movie, "," , profit, file= profit_file, sep = "")


    if letter == movie[0]:
        print (release, ",", movie, "," , profit, file= letter_file, sep="")
        print (release, ",", movie, "," , profit, sep="")
    if int(profit) > int(test_profit):
        test_profit = int (profit)
        test_title = movie
print("The movie with the highest profit is ",test_title," with a profit of " ,test_profit,"US dollars." )

input_file.close()
profit_file.close()
letter_file.close()
