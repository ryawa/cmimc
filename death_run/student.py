import networkx as nx
import random


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

        self.graph = nx.DiGraph()
        self.graph.add_weighted_edges_from(edge_list)

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


class GreedyStudent(BaseStudent):
    def __init__(self, edge_list, begin, ends):
        self.edge_list = edge_list
        self.begin = begin
        self.ends = ends

        self.graph = nx.DiGraph()
        self.graph.add_weighted_edges_from(edge_list)

    def strategy(self, edge_updates, vertex_counts, current_vertex):
        for (u, v), w in edge_updates.items():
            self.graph[u][v]["weight"] += w
        # Avoid other students, ties?
        out_edges = list(self.graph.out_edges(nbunch=current_vertex))
        get_edge_weight = lambda edge: self.graph.get_edge_data(*edge)["weight"]
        out_edges = sorted(
            out_edges,
            key=get_edge_weight,
        )
        return out_edges[0][1]
