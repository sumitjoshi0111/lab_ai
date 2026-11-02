
# Practical 4: Tower of Hanoi using State Space Search

from collections import deque

# Create initial state
def initial_state(n):
    A = tuple(range(n, 0, -1))
    return (A, (), ())

# Check goal state
def is_goal(state, n):
    return len(state[2]) == n

# BFS algorithm
def solve_hanoi(n):
    start = initial_state(n)

    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, moves = queue.popleft()

        if is_goal(state, n):
            return moves

        for i in range(3):
            for j in range(3):

                if i == j or not state[i]:
                    continue

                disk = state[i][-1]

                if state[j] and state[j][-1] < disk:
                    continue

                rods = [list(rod) for rod in state]
                rods[i].pop()
                rods[j].append(disk)

                new_state = tuple(tuple(rod) for rod in rods)

                if new_state not in visited:
                    visited.add(new_state)

                    new_moves = moves + [(disk, i, j)]
                    queue.append((new_state, new_moves))

    return []

# Main program
def main():
    n = 3
    rods = ["A", "B", "C"]

    solution = solve_hanoi(n)

    print("Tower of Hanoi using BFS")
    print("Number of disks:", n)

    for step, (disk, source, target) in enumerate(solution, 1):
        print("Move", step, ": Disk", disk,
              "from", rods[source], "to", rods[target])

    print("Total moves:", len(solution))

if __name__ == "__main__":
    main()
