from collections import deque

city = {
    "Home": ["Bus Stand", "Railway Station"],
    "Bus Stand": ["Home", "Market", "Hospital"],
    "Railway Station": ["Home", "College", "Market"],
    "Market": ["Bus Stand", "Railway Station", "Mall"],
    "Hospital": ["Bus Stand", "Mall"],
    "College": ["Railway Station", "Mall"],
    "Mall": ["Market", "Hospital", "College", "Customer"],
    "Customer": ["Mall"]
}

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    front_queue = deque([[start]])
    back_queue = deque([[goal]])

    front_visited = {start: [start]}
    back_visited = {goal: [goal]}

    while front_queue and back_queue:

        front_path = front_queue.popleft()
        front_node = front_path[-1]

        for neighbour in graph[front_node]:
            if neighbour not in front_visited:
                new_path = front_path + [neighbour]
                front_visited[neighbour] = new_path
                front_queue.append(new_path)

                if neighbour in back_visited:
                    return new_path[:-1] + back_visited[neighbour][::-1]

        back_path = back_queue.popleft()
        back_node = back_path[-1]

        for neighbour in graph[back_node]:
            if neighbour not in back_visited:
                new_path = back_path + [neighbour]
                back_visited[neighbour] = new_path
                back_queue.append(new_path)

                if neighbour in front_visited:
                    return front_visited[neighbour] + new_path[-2::-1]

    return None


start = input("Enter starting location: ")
goal = input("Enter destination: ")

path = bidirectional_search(city, start, goal)

if path:
    print("\nShortest Route:")
    print(" -> ".join(path))
    print("Number of road segments:", len(path) - 1)
else:
    print("\nNo route found.")