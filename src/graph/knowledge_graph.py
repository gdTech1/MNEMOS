from __future__ import annotations
import networkx as nx
from .edges import Edge
from .nodes import Node

class KnowledgeGraph:

    def __init__(self):
        self._graph = nx.DiGraph()

    def add_node(self, node: Node):
        self._graph.add_node(
            node.id,
            entity_type=node.entity_type.value,
            created_at=node.created_at,
        )

    def get_node(self, node_id: str):
        if not self._graph.has_node(node_id):
            return None

        data = self._graph.nodes[node_id]

        return Node(
            id=node_id,
            entity_type=data["entity_type"],
            created_at=data["created_at"],
        )

    def remove_node(self, node_id: str):
        if self._graph.has_node(node_id):
            self._graph.remove_node(node_id)

    def add_edge(self, edge: Edge):
        self._graph.add_edge(
            edge.source_id,
            edge.target_id,
            id=edge.id,
            relationship_type=edge.relationship_type,
            created_at=edge.created_at,
        )

    def remove_edge(self, source_id: str, target_id: str):
        if self._graph.has_edge(source_id, target_id):
            self._graph.remove_edge(source_id, target_id)

    def get_neighbors(self, node_id: str):
        if not self._graph.has_node(node_id):
            return []

        return list(self._graph.successors(node_id))

    def has_node(self, node_id: str):
        return self._graph.has_node(node_id)

    def has_edge(self, source_id: str, target_id: str):
        return self._graph.has_edge(source_id, target_id)

    def node_count(self):
        return self._graph.number_of_nodes()

    def edge_count(self):
        return self._graph.number_of_edges()

    def clear(self):
        self._graph.clear()