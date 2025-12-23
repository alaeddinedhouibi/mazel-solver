import matplotlib.pyplot as plt
import numpy as np

def display_maze(maze, path=None):
    """Display the maze using matplotlib"""
    maze = np.array(maze)  # Convert to numpy array for imshow
    nrows, ncols = maze.shape
    fig, ax = plt.subplots()  # Removed incorrect nrows, ncols parameters
    ax.imshow(maze, cmap='binary')

    if path:
        for (row, col) in path:
            ax.add_patch(plt.Circle((col, row), 0.3, color='red'))  # Fixed: swapped row,col and used add_patch

    ax.set_xticks(range(ncols))
    ax.set_yticks(range(nrows))
    ax.set_xticks([x - 0.5 for x in range(1, ncols)], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, nrows)], minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=2)
    ax.tick_params(left=False, bottom=False, labelbottom=False, labelleft=False)
    plt.show()

def is_safe(maze, row, col):
    """Check if the position is within bounds and not a wall"""
    return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] == 0

def solve_maze(maze, start, end):
    """Finds a path through the maze from start to end using DFS"""
    path = []
    visited = set()

    def dfs(row, col):
        if (row, col) in visited:
            return False
        visited.add((row, col))
        path.append((row, col))

        if (row, col) == end:
            return True

        # Explore neighbors (down, right, up, left)
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_row, new_col = row + dr, col + dc
            if is_safe(maze, new_row, new_col):
                if dfs(new_row, new_col):
                    return True

        # Backtrack if no path found
        path.pop()
        return False

    if dfs(start[0], start[1]):
        return path
    return None

def main():
    """Main function to demonstrate maze solving"""
    # Define a sample maze (0=open, 1=wall)
    maze = [
        [0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 0, 1, 0, 0] ,
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        # Fixed: end position (3,4) should be accessible
    ]

    start = (0, 0)
    end = (3, 4)  # Fixed: end position to match maze dimensions

    print("Original maze:")
    display_maze(maze)
    print("Solving maze...")
    path = solve_maze(maze, start, end)
    if path:
        print("Path found:", path)
        display_maze(maze, path)  # Fixed: pass maze and path together
    else:
        print("No path found")

if __name__ == "__main__":  # Fixed syntax for if statement
    main()