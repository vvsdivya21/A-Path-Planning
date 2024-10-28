A* Path Planning

Overview

A* (A-star) is a popular and powerful pathfinding and graph traversal algorithm widely used in robotics, video games, navigation systems, and AI applications. It finds the shortest path between two points in a grid or graph, balancing exploration efficiency with optimal path cost. This project implements A* path planning to calculate the most efficient route from a start point to a destination while avoiding obstacles.

How A* Path Planning Works

A* is an informed search algorithm, combining aspects of Dijkstra’s Algorithm and Greedy Best-First Search. It uses a heuristic function to estimate the shortest path, optimizing both speed and path quality.

Key Components of A*:

	1.	G Cost (Cost from Start): Represents the exact cost of the path from the start node to the current node.
	2.	H Cost (Heuristic): An estimated cost to reach the goal from the current node. Common heuristic choices include:
	•	Manhattan Distance: Suitable for grids where movement is restricted to four directions.
	•	Euclidean Distance: Suitable for free-moving agents, allowing diagonal movement.
	3.	F Cost (Total Cost): The sum of G and H costs (F = G + H), used to prioritize nodes. A* searches nodes with the lowest F cost first, ensuring that each step brings the algorithm closer to the goal in the shortest path.

Steps of the A* Algorithm:

	1.	Initialization: The start node is added to the open list (nodes yet to be evaluated), with G cost set to 0 and H calculated based on the chosen heuristic.
	2.	Exploration:
	•	The node with the lowest F cost is chosen from the open list.
	•	It is moved to the closed list (nodes already evaluated).
	•	For each neighbor of the current node, the algorithm:
	•	Calculates tentative G, H, and F costs.
	•	Adds neighbors to the open list if they are not there, or updates costs if a shorter path is found.
	3.	Goal Check: This process continues until the goal node is reached or all reachable nodes have been evaluated.
	4.	Path Reconstruction: Once the goal is reached, the algorithm reconstructs the path by tracing back from the goal to the start node, using recorded parent nodes.

Why Use A* for Path Planning?

A* is known for its balance between speed and optimality. By using the heuristic function, it reduces the search area compared to Dijkstra’s algorithm, making it efficient for real-time applications where computation time is crucial. Key benefits of A* in path planning include:

	•	Optimal Paths: Finds the shortest path from start to goal.
	•	Efficiency: Prioritizes nodes that are likely to lead to the goal, reducing computation.
	•	Flexibility: Works on both grid-based and graph-based maps and can adapt to complex, dynamic environments.

Project Implementation

This project’s implementation of A* includes:

	•	Grid Representation: A grid-based map with specified start and goal nodes, along with obstacles that the algorithm must navigate around.
	•	Heuristic Options: Configurable heuristic functions (Manhattan or Euclidean) to adapt to different movement patterns.
	•	Visualization: A graphical representation of the pathfinding process, displaying nodes explored, the shortest path found, and obstacles in the grid.

 ![AMR Coursework2 Example GUI](https://github.com/user-attachments/assets/8f176441-30bc-446d-bd7a-695cab79432c)
