
import heapq

# Goal State
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Calculate Manhattan Distance
def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = state[i] - 1
            distance += abs(i // 3 - goal_pos // 3)
            distance += abs(i % 3 - goal_pos % 3)

    return distance


# Generate New States
def get_moves(state):
    moves = []
    zero = state.index(0)

    row = zero // 3
    col = zero % 3

    directions = [(-1, 0), (1, 0),
                  (0, -1), (0, 1)]

    for dr, dc in directions:
        r = row + dr
        c = col + dc

        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c

            temp = list(state)
            temp[zero], temp[new_pos] = temp[new_pos], temp[zero]

            moves.append(tuple(temp))

    return moves


# A* Algorithm
def astar(start):
    queue = []
    heapq.heappush(queue, (heuristic(start), 0, start, [start]))

    visited = set()

    while queue:
        f, g, state, path = heapq.heappop(queue)

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for new_state in get_moves(state):
            if new_state not in visited:
                new_g = g + 1
                new_f = new_g + heuristic(new_state)

                heapq.heappush(
                    queue,
                    (new_f, new_g, new_state, path + [new_state])
                )

    return None


# Main Function
def main():
    start = (1, 2, 3,
             4, 0, 6,
             7, 5, 8)

    solution = astar(start)

    if solution:
        print("Solution Found!")

        for state in solution:
            for i in range(0, 9, 3):
                print(state[i:i+3])
            print()

        print("Total Moves:", len(solution) - 1)

    else:
        print("No Solution Found")


if __name__ == "__main__":
    main()
