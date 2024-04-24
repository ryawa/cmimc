import networkx as nx
import random
import sys


class BaseStudent:
    def __init__(
        self, edge_list: list[tuple[int, int, int]], begin: int, ends: list[int]
    ) -> None:
        """
        :param edge_list: A list of tuples representing the edge list of the graph. Tuples are of the
        form (u, v, w), where (u, v) specifies that an edge between vertices u and v exist, and w is the
        weight of that edge.
        :param begin: The label of the vertex which students begin on.
        :param ends: A list of labels of vertices that students may end on (i.e. count as a valid exit).
        """
        pass

    def strategy(
        self,
        edge_updates: dict[tuple[int, int], int],
        vertex_count: dict[int, int],
        current_vertex: int,
    ) -> int:
        """
        :param edge_updates: A dictionary where the key is an edge (u, v) and the value is how much that edge's weight increased in the current round.
        Note that this only contains information about edge updates in the current round, and not previous rounds.
        :param vertex_count: A dictionary where the key is a vertex and the value is how many students are currently on that vertex.
        :param current_vertex: The vertex that you are currently on.
        :return: The label of the vertex to move to. The edge (current_vertex, next_vertex) must exist.
        """
        pass


# Starter strategy
class RandomStudent(BaseStudent):
    def __init__(self, edge_list, begin, ends):
        self.edge_list = edge_list
        self.begin = begin
        self.ends = ends

    def strategy(self, edge_updates, vertex_count, current_vertex):
        # Take a random out-edge
        return random.choice(
            [
                x
                for (_, x, _) in filter(
                    lambda z: z[0] == current_vertex, self.edge_list
                )
            ]
        )

class Dijkstra(BaseStudent):
    def __init__(self, edge_list, begin, ends):
        self.edge_list = edge_list # list of tuples (u,v,w) Edge exists from vertex u to vertex v with weighting w
        self.begin = begin # vertex where students begin
        self.ends = ends # List of verticies of valid exits

        self.graph = nx.DiGraph()
        self.graph.add_weighted_edges_from(edge_list) 

    def strategy(self,edge_updates, vertex_counts, current_vertex):
        shortest_paths = nx.single_source_dijkstra_path_length(self.graph, source=current_vertex)
        exit_paths = {vertex: shortest_paths[vertex] for vertex in self.ends if vertex in shortest_paths}
        return min(exit_paths, key=exit_paths.get)

class DijkstraAverage(BaseStudent):
    def __init__(self, edge_list, begin, ends):
        self.edge_list = edge_list
        self.begin = begin
        self.ends = ends
        self.graph = nx.DiGraph()
        self.graph.add_weighted_edges_from(edge_list)
    def strategy(self, edge_updates, vertex_count, current_vertex):
        out_vertices = [out_edge[1] for out_edge in self.graph.out_edges(current_vertex)]
        path_sets_from_vertex = {vertex: nx.single_source_dijkstra_path_length(self.graph, source=vertex) for vertex in out_vertices}

        print([(vertex, path_set) for vertex, path_set in path_sets_from_vertex])
        # path_lengths_from_vertex = {vertex: sum(path_set.values()) for vertex, path_set in path_sets_from_vertex}
        # print(path_lengths_from_vertex, file=sys.stderr)
