graph = {
    "Computer": ["Documents", "Downloads", "Pictures"],
    "Documents": ["College", "Projects"],
    "College": ["Notes", "Assignments"],
    "Projects": ["AI_Project", "Web_Project"],
    "Downloads": ["Software", "PDFs"],
    "Pictures": ["Photos", "Screenshots"],
    "Notes": [],
    "Assignments": [],
    "AI_Project": [],
    "Web_Project": [],
    "Software": [],
    "PDFs": [],
    "Photos": [],
    "Screenshots": []
}

def dfs(graph, current, target, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(current)
    path.append(current)

    if current == target:
        return path

    for folder in graph[current]:
        if folder not in visited:
            result = dfs(graph, folder, target, visited, path)
            if result:
                return result

    path.pop()
    return None

start = input("Enter starting folder: ")
target = input("Enter folder to find: ")

result = dfs(graph, start, target)

if result:
    print("\nFolder Found")
    print("Path:", " -> ".join(result))
else:
    print("\nFolder Not Found")