from typing import TypeVar, Generic, List, Tuple
from graph import Graph
from weighted_edge import WeightedEdge

V = TypeVar('V') # type of the vertices in the graph


class WeightedGraph(Generic[V], Graph[V]):
    def __init__(self, vertices: List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[WeightedEdge]] = [[] for _ in vertices]

    def add_edge_by_indices(self, u: int, v: int, weight: float) -> None:
        edge: WeightedEdge = WeightedEdge(u, v, weight)
        self.add_edge(edge) # call superclass version

    def add_edge_by_vertices(self, first: V, second: V, weight: float) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v, weight)

    def neighbors_for_index_with_weights(self, index: int) -> List[Tuple[V, float]]:
        distance_tuples: List[Tuple[V, float]] = []
        for edge in self.edges_for_index(index):
            distance_tuples.append((self.vertex_at(edge.v), edge.weight))
        return distance_tuples

    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index_with_weights(i)}\n"
        return desc


if __name__ == "__main__":
    city_graph2: WeightedGraph[str] = WeightedGraph(["Mombasa", "Mariakani", "Miasenyi", "Voi", "Mtito Andei", "Kibwezi", "Emali", "Athi River", "Syokimau", "Nairobi", "Ngong", "Ongata Rongai", "Mai Mahiu", "Suswa"])

    city_graph2.add_edge_by_vertices("Mombasa", "Kibwezi", 1737)
    city_graph2.add_edge_by_vertices("Mombasa", "Mariakani", 678)
    city_graph2.add_edge_by_vertices("Mariakani", "Voi", 386)
    city_graph2.add_edge_by_vertices("Mariakani", "Miasenyi", 348)
    city_graph2.add_edge_by_vertices("Miasenyi", "Voi", 50)
    city_graph2.add_edge_by_vertices("Miasenyi", "Mtito Andei", 357)
    city_graph2.add_edge_by_vertices("Voi", "Mtito Andei", 307)
    city_graph2.add_edge_by_vertices("Voi", "Kibwezi", 1704)
    city_graph2.add_edge_by_vertices("Mtito Andei", "Ngong", 887)
    city_graph2.add_edge_by_vertices("Mtito Andei", "Ongata Rongai", 1015)
    city_graph2.add_edge_by_vertices("Ngong", "Kibwezi", 805)
    city_graph2.add_edge_by_vertices("Ngong", "Syokimau", 721)
    city_graph2.add_edge_by_vertices("Ngong", "Ongata Rongai", 225)
    city_graph2.add_edge_by_vertices("Ongata Rongai", "Syokimau", 702)
    city_graph2.add_edge_by_vertices("Ongata Rongai", "Nairobi", 968)
    city_graph2.add_edge_by_vertices("Syokimau", "Kibwezi", 588)
    
    city_graph2.add_edge_by_vertices("Syokimau", "Nairobi", 604)
    city_graph2.add_edge_by_vertices("Kibwezi", "Mai Mahiu", 238)
    city_graph2.add_edge_by_vertices("Mai Mahiu", "Emali", 613)
    city_graph2.add_edge_by_vertices("Mai Mahiu", "Athi River", 482)
    city_graph2.add_edge_by_vertices("Emali", "Athi River", 190)
    city_graph2.add_edge_by_vertices("Athi River", "Suswa", 81)
    
    print(city_graph2)

