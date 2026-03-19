# treasure map 
treasure_map = [["Sand","Sand","Sand"],["Treasure","Sand","Sand"],["Sand","Sand","Sand"]]

while  True : # Everytime  the user doesn't guess the right position he will be asked to guess another time 
    guess_row = int(input("Enter a row  (0,2) :")) # The user enters the value of the row 
    guess_column = int(input("Enter a column (0,2) : ")) # The user enters the value of the column 
    if all(x in range(3) for x in [guess_row,guess_column]) : # check whether the user actually respected the interval or not 
        if treasure_map[guess_row][guess_column] == "Treasure":  
            print("Good job !! You have found the position of the treasure ! ") # user found the exact position 
            break  # The user succesfully escaped the infinite loop !! 
        else : 
            print ("Sorry !! You have to guess again ")
    else : 
        print("Please respect the intervals given to you ")
