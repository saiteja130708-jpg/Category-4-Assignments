graph = {
    "Internet Problem": ["Check Router", "Check WiFi"],
    "Check Router": ["Restart Router", "Check Cable"],
    "Check WiFi": ["Reconnect WiFi", "Check Password"],
    "Restart Router": ["Internet Restored"],
    "Check Cable": ["Replace Cable"],
    "Reconnect WiFi": ["Internet Restored"],
    "Check Password": ["Reset Password"],
    "Internet Restored": [],
    "Replace Cable": [],
    "Reset Password": []
}

def dls(graph, current, target, limit, path=None):
    if path is None:
        path = []

    path.append(current)

    if current == target:
        return path

    if limit == 0:
        path.pop()
        return None

    for next_step in graph[current]:
        if next_step not in path:
            result = dls(graph, next_step, target, limit - 1, path)

            if result:
                return result

    path.pop()
    return None


start = input("Enter problem: ")
target = input("Enter solution: ")
limit = int(input("Enter search depth limit: "))

result = dls(graph, start, target, limit)

if result:
    print("\nSolution Found")
    print("Troubleshooting Path:", " -> ".join(result))
    print("Depth:", len(result) - 1)
else:
    print("\nSolution Not Found Within Depth Limit")
