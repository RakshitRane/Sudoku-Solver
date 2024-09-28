import time
from pprint import pprint



def get_user_input():
    """
    Asks the user to enter a 9x9 Sudoku grid, row by row.
    Each row is entered as a line of comma-separated integers, where -1 represents empty places.
    Ensures each element is either -1 or a number between 1 and 9 inclusive, and points out invalid numbers.
    """

    print("Please enter the unsolved Sudoku puzzle, row by row (9 comma-separated integers per row, -1 for empty places):")

    sudoku_board = []

    for i in range(9):

        while True:

            try:
                
                #taking comma-seperated integers as input of a row

                row = list(map(int, input(f"Enter row {i + 1}: ").split(',')))

                # Check if the row has exactly 9 elements

                if len(row) != 9:
                    print("Each row must contain exactly 9 numbers. Please try again.")
                    continue
                
                # Find any invalid numbers

                invalid_numbers = [num for num in row if num != -1 and (num < 1 or num > 9)]
                
                if invalid_numbers:
                    print(f"Invalid number(s) {invalid_numbers} found. Numbers must be between 1 and 9 inclusive, or -1 for empty places. Please try again.")

                else:
                    sudoku_board.append(row)
                    break

            #input is written in a wrong way
                
            except ValueError:
                print("Invalid input. Ensure you are entering comma-separated integers.")

    return sudoku_board



def find_empty_place(sudoku_board):

    """
    Finds the next empty place in the Sudoku board, represented by -1.
    Returns the (row, column) tuple of the first empty place found.
    If no empty place is found, returns (None, None).
    """

    for row in range(9):

        for column in range(9):

            if sudoku_board[row][column] == -1:

                return row, column
            
    # No empty cells found
            
    return None, None 
    




def is_safe_to_place(sudoku_board, num, row, column):

    """
    Determines if placing a number `num` in the (row, column) position is correct according to Sudoku rules.
    It checks the row, column, and 3x3 subgrid for any contradicting rules.
    """

    # Check the row

    if num in sudoku_board[row]:
        return False

    # Check the column, checking for element in a fixed column and changing row element from 1 to 9.

    if num in [sudoku_board[r][column] for r in range(9)]:
        return False

    # Check the 3x3 subgrid.
    # By floor division of row and column by 3, we get the starting row and column of the subgrid of that (row,column) coordinate.

    subgrid_row_start = (row // 3) * 3

    subgrid_column_start = (column // 3) * 3

    for r in range(subgrid_row_start, subgrid_row_start + 3):

        for c in range(subgrid_column_start, subgrid_column_start + 3):

            if sudoku_board[r][c] == num:

                return False

    return True




def solve_sudoku(sudoku_board):

    """
    Solves the Sudoku puzzle using backtracking.
    Returns True if a solution exists, and modifies the sudoku_board in place.
    """

    # Step 1: Find a empty place

    row, column = find_empty_place(sudoku_board)

    # If there are no empty cells, the puzzle is solved

    if row is None:
        return True

    # Step 2: Try numbers from 1 to 9

    for guess in range(1, 10):

        # Step 3: Check if putting the nummber 'guess' in that particular row and column

        if is_safe_to_place(sudoku_board, guess, row, column):

            # Step 4: Place that number on the sudoku_board

            sudoku_board[row][column] = guess

            # Step 5: Recursively attempt to solve the rest of the sudoku_board

            if solve_sudoku(sudoku_board):
                return True

        # Step 6: Then do backtracking if placing that number didn't lead to a solution, i.e. try a different guess
            
        sudoku_board[row][column] = -1

    # If no number from 1 to 9 fits, the puzzle is unsolvable
        
    return False





def get_numbers(sudoku_board, row, column):

    # To get a list of numbers for a specific place on the board

    if sudoku_board[row][column] != -1:
        return []  # Return empty if the place is not empty
    
    numbers = set(range(1, 10))  # Start with all possible numbers (1-9)

    numbers -= set(sudoku_board[row])  # Remove the numbers present in the row

    numbers -= {sudoku_board[r][column] for r in range(9)}  # Remove the numbers present in the column

    # Remove the numbers present in the 3x3 subgrid

    subgrid_row_start = (row // 3) * 3

    subgrid_column_start = (column // 3) * 3

    for r in range(subgrid_row_start, subgrid_row_start + 3):

        for c in range(subgrid_column_start, subgrid_column_start + 3):

            numbers.discard(sudoku_board[r][c])

    return list(numbers)




def count_naked_singles(sudoku_board):

    # Function to count naked singles in the Sudoku board

    count = 0

    for row in range(9):

        for column in range(9):

            if sudoku_board[row][column] == -1:  # Only check empty places

                numbers = get_numbers(sudoku_board, row, column)

                if len(numbers) == 1:  # Only one number means a naked single
                    count += 1

    return count




def can_place(sudoku_board, num, row, column):

    # Function to check if a number can be placed safely in a cell
    return is_safe_to_place(sudoku_board, num, row, column)




def count_hidden_singles(sudoku_board):

    # Function to count hidden singles in the Sudoku board

    count = 0

    for num in range(1, 10):  # Check for each number from 1 to 9

        for row in range(9):

            # Check rows for hidden singles

            positions = [(row, col) for col in range(9) if sudoku_board[row][col] == -1 and can_place(sudoku_board, num, row, col)]

            if len(positions) == 1:  # Only one position available
                count += 1
        

        for column in range(9):

            # Check columns for hidden singles

            positions = [(row, column) for row in range(9) if sudoku_board[row][column] == -1 and can_place(sudoku_board, num, row, column)]

            if len(positions) == 1:  # Only one position available
                count += 1
        

        for subgrid_row in range(3):

            for subgrid_column in range(3):

                # Check 3x3 subgrids for hidden singles

                positions = []

                for row in range(subgrid_row * 3, subgrid_row * 3 + 3):

                    for column in range(subgrid_column * 3, subgrid_column * 3 + 3):

                        if sudoku_board[row][column] == -1 and can_place(sudoku_board, num, row, column):
                            positions.append((row, column))

                if len(positions) == 1:  # Only one position available
                    count += 1

    return count





def count_naked_doubles(sudoku_board):

    # Function to count naked doubles in the Sudoku board

    count = 0

    for row in range(9):

        for col in range(9):

            if sudoku_board[row][col] == -1:  # Only check empty places

                numbers = get_numbers(sudoku_board, row, col)

                if len(numbers) == 2:  # Two numbers means a naked double
                    count += 1

    return count





def count_hidden_doubles(sudoku_board):

    # Function to count hidden doubles in the Sudoku board

    count = 0

    for num1 in range(1, 10):

        for num2 in range(num1 + 1, 10):  # Ensure num1 < num2

            for row in range(9):

                # Check rows for hidden doubles

                positions = [(row, column) for column in range(9) if sudoku_board[row][column] == -1 and can_place(sudoku_board, num1, row, column) and can_place(sudoku_board, num2, row, column)]

                if len(positions) == 2:  # Only two positions available
                    count += 1

            
            for column in range(9):

                # Check columns for hidden doubles

                positions = [(row, column) for row in range(9) if sudoku_board[row][column] == -1 and can_place(sudoku_board, num1, row, column) and can_place(sudoku_board, num2, row, column)]

                if len(positions) == 2:  # Only two positions available
                    count += 1
            

            for subgrid_row in range(3):

                for subgrid_column in range(3):

                    # Check 3x3 subgrids for hidden doubles

                    positions = []

                    for row in range(subgrid_row * 3, subgrid_row * 3 + 3):

                        for column in range(subgrid_column * 3, subgrid_column * 3 + 3):

                            if sudoku_board[row][column] == -1 and can_place(sudoku_board, num1, row, column) and can_place(sudoku_board, num2, row, column):
                                positions.append((row, column))

                    if len(positions) == 2:  # Only two positions available
                        count += 1

    return count






def count_naked_triples(sudoku_board):

    # Function to count naked triples in the Sudoku board

    count = 0

    for row in range(9):

        for column in range(9):

            if sudoku_board[row][column] == -1:  # Only check empty cells

                numbers = get_numbers(sudoku_board, row, column)

                if len(numbers) == 3:  # Three candidates means a naked triple
                    count += 1

    return count





def count_hidden_triples(sudoku_board):

    # Function to count hidden triples in the Sudoku board

    count = 0

    for num1 in range(1, 10):

        for num2 in range(num1 + 1, 10):

            for num3 in range(num2 + 1, 10):

                for row in range(9):

                    # Check rows for hidden triples

                    positions = [(row, column) for column in range(9) if sudoku_board[row][column] == -1 and can_place(sudoku_board, num1, row, column) and can_place(sudoku_board, num2, row, column) and can_place(sudoku_board, num3, row, column)]

                    if len(positions) == 3:  # Only three positions available
                        count += 1
                

                for column in range(9):

                    # Check columns for hidden triples

                    positions = [(row, column) for row in range(9) if sudoku_board[row][column] == -1 and can_place(sudoku_board, num1, row, column) and can_place(sudoku_board, num2, row, column) and can_place(sudoku_board, num3, row, column)]

                    if len(positions) == 3:  # Only three positions available
                        count += 1
                
                for subgrid_row in range(3):

                    for subgrid_column in range(3):

                        # Check 3x3 subgrids for hidden triples

                        positions = []

                        for row in range(subgrid_row * 3, subgrid_row * 3 + 3):

                            for column in range(subgrid_column * 3, subgrid_column * 3 + 3):

                                if sudoku_board[row][column] == -1 and can_place(sudoku_board, num1, row, column) and can_place(sudoku_board, num2, row, column) and can_place(sudoku_board, num3, row, column):
                                    positions.append((row, column))

                        if len(positions) == 3:  # Only three positions available
                            count += 1

    return count





def rate_difficulty(sudoku_board):

    # Function to rate the difficulty of the Sudoku based on naked and hidden singles, doubles, and triples

    naked_singles = count_naked_singles(sudoku_board)
    hidden_singles = count_hidden_singles(sudoku_board)
    naked_doubles = count_naked_doubles(sudoku_board)
    hidden_doubles = count_hidden_doubles(sudoku_board)
    naked_triples = count_naked_triples(sudoku_board)
    hidden_triples = count_hidden_triples(sudoku_board)

    # Difficulty score based on these values

    difficulty = 0
    difficulty += naked_singles * 2
    difficulty += hidden_singles * 1
    difficulty += naked_doubles * 4
    difficulty += hidden_doubles * 3
    difficulty += naked_triples * 6
    difficulty += hidden_triples * 5

    return difficulty
    




def main():

    sudoku_board = get_user_input()  # Get the Sudoku puzzle input from the user

    print("\n")

    # Calculate and display the difficulty of the puzzle

    difficulty_score = rate_difficulty(sudoku_board)

    start_time = time.time()    # Start the time

    if solve_sudoku(sudoku_board):

        # If solved, display the solved board and the time taken

        print(f"Puzzle Difficulty Score: {difficulty_score}")

        print("\nSolved Sudoku:")

        pprint(sudoku_board)

        print(f"Solved in {time.time() - start_time:.2f} seconds")

    else:

        print("This Sudoku puzzle cannot be solved.")


if __name__ == "__main__":
    main()

