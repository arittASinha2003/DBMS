import random
from collections import deque

class Monkey:
    def __init__(self, position):
        self.position = position

class Box:
    def __init__(self, position):
        self.position = position

class Banana:
    def __init__(self, position):
        self.position = position

def print_grid(grid, monkey_pos):
    for row in range(len(grid)):
        print("|", end="")
        for col in range(len(grid[row])):
            if (row, col) == monkey_pos:
                print("M", end=" ")
            else:
                print(grid[row][col], end=" ")
        print("|")

def find_path(start, target, obstacles):
    visited = set()
    queue = deque([(start, [])])

    while queue:
        current_position, path = queue.popleft()

        if current_position == target:
            return path

        visited.add(current_position)

        for action in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_position = (current_position[0] + action[0], current_position[1] + action[1])

            if 0 <= new_position[0] < 5 and 0 <= new_position[1] < 5 and new_position not in visited and new_position not in obstacles:
                queue.append((new_position, path + [action]))

    return None

def main():
    play_game = input("Do you want to play this game? (yes/no): ")

    if play_game.lower() == "yes":
        monkey = Monkey(position=(0, 0))
        box = Box(position=(random.randint(0, 4), random.randint(0, 4)))

        while True:
            banana_position = (random.randint(0, 4), random.randint(0, 4))
            if banana_position != monkey.position and banana_position != box.position:
                break

        banana = Banana(position=banana_position)

        grid = [['-' for _ in range(5)] for _ in range(5)]
        grid[box.position[0]][box.position[1]] = "-B-"
        grid[banana.position[0]][banana.position[1]] = "X"

        print("Welcome to the monkey and banana game!")
        print("The monkey is at position (0, 0).")
        print("Try to guide the monkey to the box first, then to the bananas!")
        print_grid(grid, monkey.position)

        path_to_box = find_path(monkey.position, box.position, [banana.position])

        if path_to_box is None:
            print("No path to the box!")
            return

        movements = {
            (0, 1): "forward",
            (0, -1): "back",
            (1, 0): "right",
            (-1, 0): "left"
        }

        for action in path_to_box:
            input("Press Enter to continue...")
            old_position = monkey.position

            movement = movements.get(action, "unknown direction")

            monkey.position = (monkey.position[0] + action[0], monkey.position[1] + action[1])

            grid[old_position[0]][old_position[1]] = '-'
            grid[box.position[0]][box.position[1]] = '-B-'
            print(f"Monkey went {movement} to position {monkey.position}")
            print_grid(grid, monkey.position)

        print("Monkey found the box! Now guide the monkey to the bananas.")
        grid[box.position[0]][box.position[1]] = '-'

        path_to_banana = find_path(box.position, banana.position, [])

        if path_to_banana is None:
            print("No path to the bananas!")
            return

        print("BFS pathfinding to the bananas:")
        for action in path_to_banana:
            input("Press Enter to continue...")
            old_position = monkey.position

            movement = movements.get(action, "unknown direction")

            monkey.position = (monkey.position[0] + action[0], monkey.position[1] + action[1])

            grid[old_position[0]][old_position[1]] = '-'
            print(f"Monkey went {movement} to position {monkey.position}")
            print_grid(grid, monkey.position)

        print("Congratulations! The monkey found the bananas!")

    else:
        print("Maybe next time!")

if __name__ == "__main__":
    main()
