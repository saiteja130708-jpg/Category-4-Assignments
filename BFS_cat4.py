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

def bfs_shortest_route(city, start, destination):
    queue = deque([[start]])
    visited = set()

    while queue:
        route = queue.popleft()
        current = route[-1]

        if current == destination:
            return route

        if current not in visited:
            visited.add(current)

            for next_location in city[current]:
                if next_location not in visited:
                    queue.append(route + [next_location])

    return None

start = input("Enter starting location: ")
destination = input("Enter destination: ")

route = bfs_shortest_route(city, start, destination)

if route:
    print("\nShortest Route:")
    print(" -> ".join(route))
    print("Number of road segments:", len(route) - 1)
else:
    print("\nNo route found.")
