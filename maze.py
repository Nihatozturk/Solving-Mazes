class Stack:
    def __init__(self):
        self._data = [] # nonpublic list instance

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e) # new item stored at end of list

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1] # the last item in the list

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

class MazeSolver():
    _cellstack = Stack()
    _explored = []
    _maze = None
    def __init__(self, path):
        isExitExists = False
        isStartExists = False
        self._maze = self.text_to_array(path)
        if len(self._maze) > 3:
            n = len(self._maze[0])
            for maze in self._maze:
                if len(maze) < 3 or n != len(maze):
                    raise Exception("InvalidMazeException")
        else:
            raise Exception("InvalidMazeException")

		# x not in ["X", "O", "S", "E"]
		# x == "E" and isExitExists is False: isExitExists = true
		# else raise Exception("InvalidMazeException")
		# x == "S" and isStartExists is False: isStartExists = true
		# else raise Exception("InvalidMazeException")

    def text_to_array(self, path):
        newarr = []
        with open(path) as file:
            array = [arr for arr in (file.read().split("\n"))]
            for arr in array:
                newarr.append([a for a in arr])
            return newarr

    def get_a_neighbor(self, a_tuple):
        for n in range(0, 2):
            for k in [-1, +1]:
                if n == 0:
                    x, y = a_tuple[0] + k, a_tuple[1]
                else:
                    x, y = a_tuple[0], a_tuple[1] + k
                if x >= 0 and x < len(self._maze) and y >=0 and y < len(self._maze[x]):
                    if (self._maze[x][y] == "E" or self._maze[x][y] == "O") and (x,y) not in self._explored:
                        return (x,y)

    def get_start(self):
        for x in range(0, len(self._maze)):
            for y in range(0, len(self._maze[x])):
                if self._maze[x][y] == "S": return (x, y)

    def get_exit(self):
        for x in range(0, len(self._maze)):
            for y in range(0, len(self._maze[x])):
                if self._maze[x][y] == "E": return (x, y)

    def solve_maze(self):
        self._cellstack = Stack()
        self._cellstack.push(self.get_start())
        while not self._cellstack.is_empty():
            c = self._cellstack.top()
            if c not in self._explored:
                self._explored.append(c)
            if c == self.get_exit():
                return self._cellstack._data
            if self.get_a_neighbor(c) is None:
                self._cellstack.pop()
            else:
                self._cellstack.push(self.get_a_neighbor(c))

        return (-1, -1)

# InvalidMazeException  class
class InvalidMazeException(Exception):
    # Constructor or Initializer
    def __init__(self, message):
        self.message = message

    # _str_ is to print() the value
    def _str_(self):
        return self.message


# Maze Class
class Maze(object):
    # constructor
    def __init__(self, grid):
        # m = number of rows
        self.m = len(grid)
        # number of rows should be gearter than 3
        if (self.m <= 3):
            raise InvalidMazeException("m should be greater than 3")
        # n = number of columns
        self.n = len(grid[0])
        # number of columns should be greater than 3
        if (self.n <= 3):
            raise InvalidMazeException("n should be greater than 3")
        # all inner list must be of same length
        for i in range(self.m):
            if (len(grid[i]) != self.n):
                raise InvalidMazeException("All inner lists must be of same length")
        # initialize grid
        self.grid = [['' for i in range(self.n)] for j in range(self.m)]
        # set start and end cells of grid to None
        self.start = None
        self.end = None
        # check all cells
        for i in range(self.m):
            for j in range(self.n):
                # check if each cell contains only valid symbols
                if (grid[i][j] == 'O' or grid[i][j] == 'X' or grid[i][j] == 'S' or grid[i][j] == 'E'):
                    self.grid[i][j] = grid[i][j]
                else:
                    raise InvalidMazeException("Maze object should be 'O' or 'X' or 'S' or 'E' .")

                if (grid[i][j] == 'S'):
                    # There should not be more than one instance of start cell
                    if (self.start == None):
                        # start cell should lie at border
                        if (i == 0 or j == 0 or i == self.m - 1 or j == self.n - 1):
                            self.start = (i, j)
                        else:
                            raise InvalidMazeException("Start of the maze should lie at the border.")
                    else:
                        raise InvalidMazeException("Maze should have only one start")
                if (grid[i][j] == 'E'):
                    # There should not be more than one instance of end cell
                    if (self.end == None):
                        # end cell should lie at border
                        if (i == 0 or j == 0 or i == self.m - 1 or j == self.n - 1):
                            self.end = (i, j)
                        else:
                            raise InvalidMazeException("End of the Maze should lie at the border")
                    else:
                        raise InvalidMazeException("Maze should contain only one end")
        # There should be at least one of start cell and end cell
        if (self.start == None):
            raise InvalidMazeException("There is no starting cell in the Maze")
        if (self.end == None):
            raise InvalidMazeException("There is no ending cell in the Maze")

    def get_start(self):
        # this method returns the start cell (row index, col index)
        return self.start

    def get_end(self):
        # this method returns the start cell (row index, col index)
        return self.end,

def text_to_array(path):
    newarr = []
    with open(path) as file:
        array = [arr for arr in (file.read().split("\n"))]
        for arr in array:
            newarr.append([a for a in arr])
        return newarr

'''
# test with some mazes
try:
    maze1 = [['X', 'S', 'O', 'O'], ['X', 'O', 'O', 'X'], ['E', 'O', 'O', 'O'], ['X', 'X', 'X', 'X']]
    myMaze = Maze(maze1)

    print("start = ", myMaze.get_start(), "end = ", myMaze.get_end())
except InvalidMazeException as e:
    print(e)

try:
    maze2 = [['X', 'S', 'O', 'O'], ['X', 'O', 'O', 'X'], ['E', 'O', 'O', 'O'], ['X', 'A', 'X', 'X']]
    myMaze = Maze(maze2)

    print("start = ", myMaze.get_start(), "end = ", myMaze.get_end())
except InvalidMazeException as e:
    print(e)

try:
    maze3 = [['X', 'S', 'S', 'O'], ['X', 'O', 'O', 'X'], ['E', 'O', 'O', 'O'], ['X', 'X', 'X', 'X']]
    myMaze = Maze(maze3)

    print("start = ", myMaze.get_start(), "end = ", myMaze.get_end())
except InvalidMazeException as e:
    print(e)

try:
    maze4 = [['X', 'S', 'O'], ['O', 'O', 'X'], ['O', 'O', 'O'], ['X', 'X', 'X']]
    myMaze = Maze(maze4)

    print("start = ", myMaze.get_start(), "end = ", myMaze.get_end())
except InvalidMazeException as e:
    print(e)

try:
    maze5 = [['X', 'O', 'O', 'O'], ['X', 'O', 'O', 'X'], ['E', 'O', 'O', 'O'], ['X', 'X', 'X', 'X']]
    myMaze = Maze(maze5)

    print("start = ", myMaze.get_start(), "end = ", myMaze.get_end())
except InvalidMazeException as e:
    print(e)
'''

m = MazeSolver("file.txt")

print(m.solve_maze())

try:
    map = text_to_array("file.txt")
    validation = Maze(map)
    print("start = ", validation.get_start(), "end = ", validation.get_end())
except InvalidMazeException as e:
    print(e)