"""
This module contains a function which displaying a result.

Functions:
- showResult: Display a result after running the algorithm.

Dependencies:
- matplotlib: A package for ploting a graph.
"""

from typing import List
from matplotlib import pyplot as plt, patches as pch
import config as c
from Area import Area
from Node import Node
from Edge import Edge

def showResult(area : Area, list_nodes : List[Node], list_edges : List[Edge]) -> None:
    """
    Display a result after running the algorithm.

    :param area: An Area object representing the area.
    :param list_nodes: A list of nodes in the area.
    :param list_edges: A list of edges in the area.
    :return: None.
    """

    _, ax = plt.subplots()
    
    ax.set_xlim((-1, area.width + 1))
    ax.set_ylim((-1, area.height + 1))

    ax.set_facecolor(c.bgColor)

    # add area to the plot 
    _area = pch.Rectangle((0, 0), area.width, area.height, linewidth = c.areaLinewidth, edgecolor = c.areaEdgecolor, facecolor = c.areaFacecolor)
    ax.add_patch(_area)

    # add obstacles to the plot
    while area.list_obstacles:
        obstacle = area.list_obstacles.pop()
        _obstacle = pch.Rectangle(obstacle.lb, obstacle.width, obstacle.height, edgecolor = c.obsEdgecolor, facecolor = c.obsFacecolor)
        ax.add_patch(_obstacle)

    # add nodes to the plot
    while list_nodes:
        node = list_nodes.pop()
        _node = pch.Circle(node.coor, radius = node.radius, edgecolor = node.color, facecolor = node.color)
        ax.add_patch(_node)

    # add edges to the plot
    while list_edges:
        edge = list_edges.pop()
        x, y = edge.lineString.xy
        ax.plot(x, y, color = edge.color)

    plt.show()


