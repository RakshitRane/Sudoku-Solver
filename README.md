# Sudoku Solver and Puzzle Difficulty Rater

This is a Python-based Sudoku Solver project that uses backtracking and a difficulty rating system to solve Sudoku puzzles and assess their complexity. The difficulty of each puzzle is calculated based on various solving strategies such as naked singles, hidden singles, naked doubles, hidden doubles, and naked and hidden triples.

## Features

**Backtracking Algorithm**:  Efficiently solves any solvable Sudoku puzzle.<br/><br/>
**Puzzle Difficulty Rating**:  The program rates the puzzle's difficulty based on naked and hidden solving techniques.<br/><br/>
**User-Friendly Input**:  Takes input in a 9x9 grid format and checks for invalid inputs.<br/><br/>
**Time Tracking**:  Shows the time taken to solve the puzzle.<br/><br/>
**Readable Output**:  Displays the solved puzzle in a readable format.<br/><br/>

## Requirements

You need Python 3.x installed to run the project. No external libraries are required.

## Usage

**Input Format** - <br/><br/>
*The program prompts the user to input the Sudoku puzzle, row by row.* <br/><br/>
*Each row should contain 9 comma-separated integers.*<br/><br/>
*Use -1 to represent empty cells that need to be solved.*<br/><br/>
*Numbers must be between 1 and 9 (inclusive) for filled cells.*<br/><br/>

## Solving Process

**Backtracking** : The program uses a recursive backtracking approach, attempting to fill each empty cell by checking if placing a number between 1 and 9 is valid according to Sudoku rules.<br/><br/>
**Validation** : For each empty cell, the program checks whether a number can be placed without breaking the rules in the row, column, or 3x3 subgrid.<br/><br/>
**Difficulty Rating** : Before solving the puzzle, the program calculates the difficulty rating based on the following criteria.<br/><br/>

## Difficulty Rating System

The difficulty of the Sudoku puzzle is rated using the following techniques:

**Naked Singles** : Cells where only one candidate number is possible.<br/><br/>
**Hidden Singles** : Numbers that can only be placed in one position within a row, column, or subgrid.<br/><br/>
**Naked Doubles** : Pairs of cells where only two numbers can be placed.<br/><br/>
**Hidden Doubles** : Pairs of numbers that can only fit in two positions within a row, column, or subgrid.<br/><br/>
**Naked Triples** : Three cells where only three numbers can be placed.<br/><br/>
**Hidden Triples** : Three numbers that can only be placed in three specific positions.<br/><br/>

*The difficulty score is calculated by assigning different weights to each of these techniques* :<br/><br/>

**Naked Singles** : 2 points each<br/><br/>
**Hidden Singles** : 1 point each<br/><br/>
**Naked Doubles** : 4 points each<br/><br/>
**Hidden Doubles** : 3 points each<br/><br/>
**Naked Triples** : 6 points each<br/><br/>
**Hidden Triples** : 5 points each<br/><br/>

The total difficulty score is the sum of these values. Thd weightage is given as such as mostly hidden are easier to find than naked.

## Code Overview

**get_user_input()** : Asks the user to enter the Sudoku grid row by row and validates the input.<br/>
**find_empty_place()** : Finds the next empty spot (represented by -1) in the grid.<br/>
**is_safe_to_place()** : Checks whether placing a number in a specific cell follows Sudoku rules.<br/>
**solve_sudoku()** : Implements the backtracking algorithm to solve the puzzle.<br/>
**get_numbers()** : Returns the possible numbers that can be placed in a specific empty cell.<br/>
**count_naked_singles(), count_hidden_singles(), etc.** : Counts various solving techniques used in Sudoku puzzles.<br/> 
**rate_difficulty()** : Rates the difficulty of the puzzle by calculating scores for different solving techniques.<br/>

