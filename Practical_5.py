# Practical 5: Blocks World using BFS

from collections import deque

def initial_state():
    return (("B", "A"), ("C",), ())

def is_goal(state):
    return state[0] == ("B", "A", "C")

def solve_blocks():
    start = initial_state()

    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, moves = queue.popleft()

        if is_goal(state):
            return moves

        for i in range(3):
            for j in range(3):

                if i == j or not state[i]:
                    continue

                block = state[i][-1]

                stacks = [list(stack) for stack in state]
                stacks[i].pop()
                stacks[j].append(block)

                new_state = tuple(tuple(stack) for stack in stacks)

                if new_state not in visited:
                    visited.add(new_state)

                    new_moves = moves + [(block, i, j)]
                    queue.append((new_state, new_moves))

    return []

def main():
    stacks = ["Table 1", "Table 2", "Table 3"]

    solution = solve_blocks()

    print("Blocks World using BFS")
    print("Initial State: B-A | C | Empty")
    print("Goal State: B-A-C | Empty | Empty")
    print("--------------------------------")

    for step, (block, source, target) in enumerate(solution, 1):
        print("Move", step, ": Block", block,
              "from", stacks[source], "to", stacks[target])

    print("--------------------------------")
    print("Total moves:", len(solution))

if __name__ == "__main__":
    main()