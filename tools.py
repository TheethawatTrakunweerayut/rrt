"""
This module contains functions used to check whether the object is valid or not.

Function:
- checkArea: Checks whether the object is fully in the area.
- checkFree: Checks whether the object is in the free-space.
- checkCross: Checks whether the object crosses the obstacle or not.

Classes:
- Area: A class for representing a rectangular box.
- Obstacle: A class for representing an obstacle.
- Node: A class for representing a node.
- Edge: A class for representing an edge.

Dependencies:
- shapely: A package for manipulating geometric shapes.
"""

from typing import List, Any
from shapely.geometry import Polygon
from Area import Area
from Obstacle import Obstacle
from Node import Node
from Edge import Edge

def checkArea(area : Area, _object : Polygon) -> bool:
    """
    Checks the object whether it is in the area or not.

    :param area: An Area object representing the area.
    :param _object: A polygon data to be checked.
    :return: A boolean indicating the object is valid or not.
    """

    return True if area.polygon.contains(_object) else False

def checkFree(list_obstacles : List[Obstacle], _object : Any) -> bool:
    """
    Checks the object whether it is in the free-space or not.

    :param list_obstacles: A list of obstacles in the area.
    :param _object: An object to be checked.
    :return: A boolean indicating the object is valid or not.
    """

    for obs in list_obstacles:
        if _object.intersection(obs.polygon):
            return False
    return True

def checkCross(list_obstacles : List[Obstacle], list_nodes : List[Node], list_edges : List[Edge], _object : Any) -> bool:
    """
    Checks the object whether it crosses the obstacle or not.

    :param list_obstacles: A list of obstacles in the area.
    :param list_nodes: A list of nodes in the area.
    :param list_edges: A list of edges in the area.
    :param _object: An object to be checked.
    :return: A boolean indicating the object is valid or not.
    """

    for obs in list_obstacles:
        if _object.crosses(obs.polygon):
            return False
        
    for edge in list_edges:
        if _object.crosses(edge.lineString):
            return False
        
    for node in list_nodes:
        if _object.crosses(node.point):
            return False
        
    return True