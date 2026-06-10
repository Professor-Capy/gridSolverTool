# gridSolver

## Purpose
Im making ts project as part of a cs50 thingie im taking, no other real reason

## main.py
Doesnt have anything yet, but will have all of the main code for actually running the project

## logic.py
Contains all of the real code

### Nodes
Basically just gridboxes on the grid, im calling it a node since it sounds cooler
Nodes also have magic method *__repr__* incase u try printing a node
I also may call these *'gridboxes'* and *'boxes'*.

#### setNode
Is a method of the Node class that basically changes the value of a node
Takes in one param newNode, type string, which it uses for changing the value of the node. the entire method returns None

### Grids
The big thing, for the way im using it, it may also be treated as a map, or sum
Grids _ALSO_ have magic method *__repr__* incase u try printing one, which i should update soon to make it look nice

#### findNeighbours
A useful method of the Grid class, which returns a tuple of tuples of row by col coordinates, the coordinates being directions to the possible neighbours of the starting gridbox
takes in 2 int params, row, and col, which is used to find the starting node.

#### minimizeMDistance
Incomplete
