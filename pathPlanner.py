#_______________________________________________ CODE EXPLANATION _______________________________________________

'''
- **Initialization:**
  - Initialize necessary data structures such as `open_set`, `came_from`, `g_score`, and `f_score`.
  - Define possible movements (up, down, left, right) within the grid.

- **A* Algorithm:**
  - Iterate while nodes remain in the `open_set`.
  - Select the node with the lowest combined score (`f_score`) from the `open_set`.
  - Check if the selected node is the end node; if so, reconstruct and return the optimal path.
  - Remove the current node from the `open_set`.
  - Explore neighboring nodes:
    - Calculate tentative `g_score` for each neighbor.
    - Update `came_from`, `g_score`, and `f_score` if a better path is found.
    - Add newly discovered neighbors to the `open_set`.

- **Path Reconstruction:**
  - Backtrack from the end node to the start node using the `came_from` dictionary.
  - Append each node to the path list until reaching the start node.
  - Reverse the path list to ensure correct order from start to end.
  - Return the reconstructed path.

- **Error Handling:**
  - If no path is found, display an error message and return an empty list.

- **Helper Functions:**
  - `euclidean_distance`: Calculate the Euclidean distance between two points.

- **Termination:**
  - End of the function signifies the completion of the A* algorithm implementation.
'''
#_______________________________________________ VARIABLES EXPLANATION _______________________________________________

'''
- COL: Represents the number of columns in the grid.
- ROW: Represents the number of rows in the grid.

- movements: Defines the possible movements (up, down, left, right) that can be made within the grid.
- open_set: A list of nodes to be evaluated during the A* algorithm.

- came_from: {NODE(KEY) --> PARENT NODE(VALUE)},
             A dictionary mapping nodes to their parent nodes to reconstruct the path. 
- g_score:   {NODE(KEY) --> COST FROM START TILL NODE(VALUE)},
             A dictionary storing the cost of reaching each node from the start node.
- f_score:   {NODE(KEY) --> TOTAL COST(VALUE)},
             A dictionary storing the estimated total cost of reaching the end node from each node through the current node.

- current: Represents the current node being evaluated during the A* algorithm.
- neighbor: Represents a neighboring node being considered during exploration.
- tentative_g_score: Represents the tentative cost of reaching a neighbor node from the start node through the current node.
- path: Stores the reconstructed path from the start node to the end node.
- display_message: A function used to display messages during execution.
'''
#_______________________________________________ START CODE _______________________________________________


# Import any libraries required
import math

# Calculate Euclidean distance between two points
def euclidean_distance(start, end):
    return math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)

# The main path planning function. Additional functions, classes, 
# variables, libraries, etc. can be added to the file, but this
# function must always be defined with these arguments and must 
# return an array ('list') of coordinates (col,row).
# DO NOT EDIT THIS FUNCTION DECLARATION
def do_a_star(grid, start, end, display_message):
    # Get the size of the grid
    COL = len(grid)
    ROW = len(grid[0])
    # _______________________________________________ INITIALISATIONS _______________________________________________

    # Define possible movements (up, down, left, right)
    movements = [(0,1), (0,-1), (1,0), (-1,0)]

    # Initialize open and closed sets
    open_set = [start] # Nodes to be evaluated
    came_from = {} # Map of nodes and their parent nodes
    g_score = {start: 0}  # Cost from start to a node
    f_score = {start: euclidean_distance(start, end)}  # Calculate f_score for start node using Euclidean distance heuristic

    # _______________________________________________ START A* ALGORITHM _______________________________________________
    while open_set:
        # Select the node with the minimum f_score from the open set
        current = min(open_set, key=lambda x: f_score.get(x, math.inf))

        # Check if the current node is the end node
        if current == end:
            path = []
            # Reconstruct the path from end to start by backtracking through came_from dictionary
            while current in came_from:
                path.append(current)
                current = came_from[current] #Update the current node to its parent node
            path.append(start)  # Add start node to the path
            path.reverse()  # Reverse the path to get start to end order
            return path  # Return the reconstructed path

        open_set.remove(current)  # Remove current node from open set
        for dx, dy in movements:
            neighbor = (current[0] + dx, current[1] + dy) # Calculate the coordinates of the neighbor node
            # Check if the neighbor is within grid bounds and is not an obstacle
            if 0 <= neighbor[0] < COL and 0 <= neighbor[1] < ROW and grid[neighbor[0]][neighbor[1]] != 0:
                tentative_g_score = g_score[current] + 1  # Calculate tentative g_score for neighbor
                if tentative_g_score < g_score.get(neighbor, math.inf):
                    # Update g_score, came_from, and f_score for neighbor
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + euclidean_distance(neighbor, end)
                    if neighbor not in open_set:
                        open_set.append(neighbor)  # Add neighbor to open set
                        
    # _______________________________________________ END A* ALGORITHM _______________________________________________

    # No path found
    display_message("[ERROR] No path found!")
    return []

# End of file
# _______________________________________________ END OF CODE _______________________________________________

