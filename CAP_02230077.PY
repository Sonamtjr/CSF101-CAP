################################
# Sonam Tashi
# 1. Electrical
# 02230077
################################
# REFERENCES
# @DQ-Logo
# @Blackbox.ai
#@ChatGbt
################################
# SOLUTION
# Your Solution Score:50169
# CSF101_CAP/input_9_cap1.txt
################################# Read the input.txt file
def read_input(Input_your_file_name): # define a function "read_input"
    x = [] # create an empty list
    with open(Input_your_file_name, 'r') as files: # For each line in the file
        for y in files: # Using whitespace as the delimiter, divide the lines into two halves.
            others_turn, result = y.split() # Make a tuple with the two components, then add it to the list above.
            x.append((others_turn, result)) # Construct a tuple and append it to the list with the values of "others_turn" and "result."

    return x # return the list with "others_turn" and "result" in it.

# figuring out the scoring for every round or game
def calculate_score(total_Games_Played): # determines a score by using "total Games Played."
    marking = 0 # Every round begins with a starting point of 0.
    for others_turn, result in total_Games_Played: # Go over every game in "total_Games_Played" one after another. 
# and exhibit 'others_turn' and'result' values.
        if result == 'X':  #We must get defeated.
            if others_turn == 'A': # Others decide on Rock
                marking += 3 # Scissor gets defeated by Rock.
            elif others_turn == 'B': # Others decide on paper.
                marking += 1  # Paper defeats rock.
            elif others_turn == 'C': # others decide on scissors
                marking += 2 # Paper is defeated by scissors
        elif result == 'Y':  #We must create a Draw.
            if others_turn == 'A': # an individual selects Rock
                marking += 4  # Rock is draw against Rock.
            elif others_turn == 'B': # an individual choose Paper
                marking += 5  # Paper is draw against Paper.
            elif others_turn == 'C': # an individual selected scissors
                marking += 6  # Scissors are draw against each other.
        elif result == 'Z':  # We must get victory.
            if others_turn == 'A': # someone selected Rock
                marking += 8  # Paper defeats  Rock.
            elif others_turn == 'B': # someone selected Paper
                marking += 9 # Paper gets defeated by scissors.
            elif others_turn == 'C': # someone selected scissors
                marking += 7 # Rock defeats  Scissor.
    print(f"The final outpot of theresult is:{marking}") #printing from the input file the total amount of the markings
# Running the programme
Input_your_file_name = "CSF101-CAP/input_7_cap1.txt"  # The students'  Index Number
calculate_score(read_input(Input_your_file_name)) # Utilizing the information gleaned from reading the input file, compute the score.
