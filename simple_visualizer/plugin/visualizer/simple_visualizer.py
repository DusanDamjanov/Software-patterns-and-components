import json
from abc import ABC

from core.services.visualizing import VisualizingService
from django.template import *


class SimpleVisualizer(VisualizingService, ABC):

    def name(self):
        return "Simple Visualizer"

    def id(self):
        return "Simple graph"

    def visualize(self, graph, request):
        # Initialize data structures for storing nodes and edges
        nodes = {}
        edges = []

        for vertex_id, vertex in graph.vertices.items():
            # Define attributes for the node
            node_data = {
                "id": vertex_id,
                "label": f"Node {vertex_id}",
                "attributes": {}  # Additional attributes if needed
            }
            nodes[vertex_id] = node_data

            # Iterate over the edges incident to the current vertex
            for edge in vertex.edges:
                # Define attributes for the edge
                edge_data = {
                    "source": edge.start.id,
                    "target": edge.end.id,
                    "label": edge.label if edge.label else "Edge"  # Example label, you can customize this
                }
                edges.append(edge_data)

        # Assemble the visualization data
        visualization_data = {
            "nodes": list(nodes.values()),
            "edges": edges
        }

        # Return the visualization data
        return visualization_data
