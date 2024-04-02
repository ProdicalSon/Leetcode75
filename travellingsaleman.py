from itertools import permutations

def tsp_brute_force(distances):
    # distances is a matrix representing distances between cities
    shortest_distance = float('inf')
    shortest_path = None
    for permutation in permutations(range(len(distances))):
        # Calculate total distance for each permutation
        current_distance = 0
        for i in range(len(permutation) - 1):
            current_distance += distances[permutation[i]][permutation[i + 1]]
        current_distance += distances[permutation[-1]][permutation[0]]  # Add distance back to starting city
        if current_distance < shortest_distance:
            shortest_distance = current_distance
            shortest_path = permutation
    return shortest_path, shortest_distance

# Example usage (assuming distances is defined)
path, distance = tsp_brute_force(distances)
print("Shortest Path:", path)
print("Shortest Distance:", distance)