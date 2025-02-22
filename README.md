**# HIVE-CODING-CHALLENGE**

**Challenge 1: Balanced Parentheses**

🧠 Understanding the Problem

    What’s the Problem?
    We need to check if a string of brackets (like (), {}, []) is balanced. Balanced means every opening bracket has a matching closing bracket in the correct order.

    Example:
    "{[()]}" is balanced, but "{[(])}" is not.

🔍 Understanding the Solution

    Why a Stack?
    A stack helps us track the most recent opening bracket and match it with the current closing bracket. It follows the Last-In-First-Out (LIFO) principle, which is perfect for this problem.
    It is a fundamental data structure in computer science that follows the LIFO principle.. It’s a way to organize and manage data in a specific order.
    
    
    How Does It Work?
        
        Made use a stack (LIFO – Last In, First Out).

        Push every opening bracket onto the stack.

        For every closing bracket, check if it matches the top of the stack.

        If it matches, pop the stack. If not, the string is unbalanced.

        At the end, if the stack is empty, the string is balanced.

🎯 Why is this solution the best?

    Efficiency: It runs in O(n) time and space, where n is the length of the string.

    Simplicity: The stack approach is intuitive and easy to implement.

    Edge Cases Handled: Empty string, all opening brackets, all closing brackets.





**Challenge 2: Conway’s Game of Life**

🧠 Understanding the Problem

    What’s the Problem?
    We have a grid of cells that are either alive (1) or dead (0). The grid evolves based on rules about how many live neighbors each cell has.

    Rules:

        A live cell with fewer than 2 or more than 3 live neighbors dies.

        A live cell with 2 or 3 live neighbors survives.

        A dead cell with exactly 3 live neighbors becomes alive.

🔍 Understanding the Solution

    Why a Copy of the Grid?
    We need to compute the next state without modifying the current state, so we use a copy of the grid.

    How Does It Work?

        For each cell, count its live neighbors in a 2D grid system (up to 8).
        
        Each cell can have up to 8 neighbors: top-left, top, top-right, left, right, bottom-left, bottom, and bottom-right.

        Apply the rules to determine if the cell lives, dies, or becomes alive.

        Update the next state in the copy of the grid.


🎯 Why is this solution the best?

    Efficiency: It runs in O(N * M) time and space, where N and M are the grid dimensions.

    Simplicity: The rules are applied directly, and the grid copy ensures correctness.

    Edge Cases Handled: Empty grid, all dead cells, all live cells.





**Challenge 3: Shortest Path in a Grid Maze**

🧠 Understanding the Problem

    What’s the Problem?
    You’re in a grid maze where some cells are blocked (1), and others are open (0). You start at the top-left corner and need to reach the bottom-right corner. Find the shortest path (least number of steps) to the destination. If no path exists, return -1.

🔍 Understanding the Solution

    Why BFS?
    BFS explores all possible paths level by level, guaranteeing the shortest path in an unweighted grid.
    BFS stands for Breadth-First Search. It’s a fundamental algorithm used to traverse or search through graphs and trees.


    How Does It Work?

        Start at (0, 0), explore its neighbors (up, down, left, right).

        Keep track of the distance and mark visited cells.

        If you reach the destination, return the distance. If the queue is exhausted, return -1.


🎯 Why is this solution the best?

    Efficiency: It runs in O(N * M) time and space, where N and M are the grid dimensions.

    Guarantees Shortest Path: BFS ensures the shortest path in an unweighted grid.

    Edge Cases Handled: Start or end blocked, no path exists.