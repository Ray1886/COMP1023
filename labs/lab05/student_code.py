# student_code.py

# Available actions:
# 'R' - Move right
# 'L' - Move left  
# 'U' - Move up
# 'D' - Move down


# width,height = 5,5 # Example width and height, will be replaced with actual values as needed

def solve_level_one():
    """
    Level 1: Linear Traversal 
    
    
    Returns: A string containing movement actions like "RRRR"
    
    Strategy: Move right across the single row to visit all positions
    """
    actions = "" # this is the string containing all the movements of the hunter
                 # We will use this string to check the correctness of your code
    
    # --- TODO below ---
    # Hint: When the hunter starts, you're already at the first position (index 0)
    # You need to use a for loop to move.
    # Add the actions to the "actions" string 
    # Only use Move Right action: 'R'
    # to add a single "move right action" to the string, you can use actions = actions + "R"
    # assume that "width" and "height" variables are automatically filled out with the 
    # "width" and the "height" of the map by main_game.py. You can use it/them here.
    # ~5 lines of code should be sufficient.
    for i in range(width - 1):
        actions = actions + "R"


    # --- TODO above ---

    return actions  # return the resulting actions to main_game.py. Don't modify this line



def solve_level_two():
    """
    Level 2: S-Pattern Traversal 
    
    Returns: A string containing movement actions like "RRRRRDLLLLDRRRR"
    
    Strategy: Alternate between right and left movement for each row
    """
    actions = ""

    # --- TODO below ---  
    # Hint: You'll need nested loops and conditional logic
    # Add the actions to the "actions" string 
    # Three possible actions: 'R', 'L', 'D' will be needed.
    # assume that "width" and "height" variables are automatically filled out with the 
    # "width" and the "height" of the map by main_game.py. You can use it/them here.
    # ~15 lines of code should be sufficient.
    for i in range(height - 1):
        for j in range(width - 1):
            if i % 2 == 0:
                actions += "R"
            else:
                actions += "L"
        actions += "D"
    for k in range(width - 1):
        if height % 2 == 0:
            actions += "L"
        else:
            actions += "R"







    
    # --- TODO above ---

    return actions # return the resulting actions to main_game.py. Don't modify this line



def solve_level_three():
    """
    Level 3: Spiral Traversal  (Advanced)
    
    Returns: A string containing movement actions in a spiral pattern
    
    Strategy: Process spiral layers from outside to inside using direction tracking
    """
    actions = ""

    # --- TODO below ---    
    # Hint, you'll need to manage boundaries and directions carefully. while loops might be useful.
    # assume that "width" and "height" variables are automatically filled out with the 
    # "width" and the "height" of the map by main_game.py. You can use it/them here.
    # about 30-40 lines of code should be sufficient.
    # Initialize boundaries for the spiral
    top_row = 0
    bottom_row = height
    left_col = 0
    right_col = width
    row_boundaries = bottom_row - top_row
    col_boundaries = right_col - left_col
    while row_boundaries > 1 and col_boundaries > 1:
        for i in range(col_boundaries - 1):
            actions += "R"
        for j in range(row_boundaries - 1):
            actions += "D"
        for k in range(col_boundaries - 1):
            actions += "L"
        for q in range(row_boundaries - 2):
            actions += "U"
        top_row += 1
        bottom_row -= 1
        left_col += 1
        right_col -= 1
        actions += "R"
        row_boundaries = bottom_row - top_row
        col_boundaries = right_col - left_col
    if row_boundaries == 1:
        for p in range(col_boundaries - 1):
            actions += "R"
    if col_boundaries == 1 and row_boundaries != 1:
        for y in range(row_boundaries - 1):
            actions += "D"


    # --- TODO above ---

    return actions # return the resulting actions to main_game.py. Don't modify this line