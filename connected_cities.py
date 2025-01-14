import sys
from collections import defaultdict, deque

class ConnectedCities:
    def __init__(self, file_path):
        self.graph = defaultdict(list)
        self.load_graph(file_path)

    def load_graph(self, file_path):
        """
        Load city connections from a file and build a graph.
        """
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    city1, city2 = line.strip().split(',')
                    self.graph[city1.strip()].append(city2.strip())
                    self.graph[city2.strip()].append(city1.strip())
        except Exception as e:
            print(f"Error loading file: {e}")
            sys.exit(1)

    def are_connected(self, city1, city2):
        """
        Check if two cities are connected using BFS.
        """
        if city1 not in self.graph or city2 not in self.graph:
            return False
        
        visited = set()
        queue = deque([city1])
        
        while queue:
            current_city = queue.popleft()
            if current_city == city2:
                return True
            
            visited.add(current_city)
            for neighbor in self.graph[current_city]:
                if neighbor not in visited:
                    queue.append(neighbor)
        
        return False

# Entry point for command-line usage
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python connected_cities.py <file_path> <city1> <city2>")
        sys.exit(1)

    file_path, city1, city2 = sys.argv[1], sys.argv[2], sys.argv[3]
    cc = ConnectedCities(file_path)
    result = cc.are_connected(city1, city2)
    print(f"Are '{city1}' and '{city2}' connected? {'Yes' if result else 'No'}")