"""
This module contains functions for finding the path 
between a given start and end point using RRT.

Function:
- rrt: Randomly creates a path between a given start and end point.
- rd_location: Randomly generate a location which lies within the free-space.
- getClosest: Retrieve the node closest to the location of `_dir`.
- get_newCoor: Creates a new point if it's valid.
- createEdge: Creates a new edge if it's valid.
- tryReachEnd: Tries creating an edge connecting to the end node.
- dfs: Uses a DFS approach to find the path between start and end nodes.

Dependencies:
- shapely: A package for manipulating geometric shapes.
- random: A module provides functions for generating random numbers or selections.
- math: A module provides a set of mathematical functions and constants.
"""

from typing import Union, List, Tuple, Union, Dict
from shapely.geometry import Point, LineString
import random as rd
import math as m
import tools as t
import config as c
from Area import Area
from Node import Node
from Edge import Edge

def rrt(area : Area, startNode : Node, endNode : Node) -> Tuple[List[Node], List[Edge]]:
    """
    Randomly creates a path between a given start and end nodes.

    :param area: An Area object representing the area.
    :param startNode: A start node.
    :param endNode: An end node.
    :return: A list of nodes and a list of edges which randomly created using RRT approach.
    """

    list_nodes = [startNode]
    list_edges = []
    counter = 0
    while list_nodes[-1] != endNode:
        endEdge = tryReachEnd(area, list_nodes, list_edges, list_nodes[-1], endNode)
        if endEdge:
            list_nodes[-1].neighbor[endNode] = endEdge
            list_edges.append(endEdge)
            list_nodes.append(endNode)
        else:
            _dir = endNode.coor if counter % c.f == 0 else rd_coordinate(area)
            cNode = getClosest(list_nodes, Point(_dir))
            newCoor = get_newCoor(area, cNode, _dir)
            if newCoor:
                _edge = createEdge(area, list_nodes, list_edges, cNode, Point(newCoor))
                if _edge:
                    newNode = Node(newCoor, c.nodeRadius, c.nodeColor)
                    cNode.neighbor[newNode] = _edge
                    list_nodes.append(newNode)
                    list_edges.append(_edge)
        counter += 1
    
    # find the path
    path = {}
    dfs(path, list_nodes[0])
    for node, edge in path.items():
        node.color = c.pathColor
        edge.color = c.pathColor

    endNode.color = c.endColor

    return list_nodes, list_edges

def rd_coordinate(area : Area) ->Tuple[Union[int, float]]:
    """
    Randomly generate a coordinate.

    :param area: An Area object representing the area.
    :return: A randomized coordinate.
    """

    return (rd.uniform(0.0, area.width), rd.uniform(0.0, area.height))

def getClosest(list_nodes : List[Node], _dir : Node) -> Node:
    """
    Retrieve the node closest to the location of `_dir`.

    :param list_nodes: A list of nodes in the area.
    :param _dir: A location towards which the new node will be directed.
    :return: The node closest to the new node.
    """

    currentNode = list_nodes[0]
    d = _dir.distance(currentNode.point)
    for node in list_nodes[1:]:
        new_d = _dir.distance(node.point)
        if new_d < d:
            currentNode = node
            d = new_d
    return currentNode

def get_newCoor(area : Area, cNode : Node, _dir : Tuple[Union[int, float]]) -> Union[Tuple[Union[int, float]], None]:
    """
    Creates a new point if it's valid.

    :param area: The area object representing the area.
    :param cNode: The closest node to the location of `_dir`.
    :param _dir: The location towards which the new node will be directed.
    :return: A new coordinate if it is valid else None.
    """

    x1, y1 = cNode.coor
    x2, y2 = _dir
    angle = m.atan2((y2 - y1), (x2 - x1))
    newCoor = (x1 + c.edgeLength * m.cos(angle), y1 + c.edgeLength * m.sin(angle))
    if t.checkFree(area.list_obstacles, Point(newCoor)):
        return newCoor
    return None

def createEdge(area : Area, list_nodes : List[Node], list_edges : List[Edge], cNode : Node, newCoor : Point) -> Union[Edge, None]:
    """
    Creates a new edge if it's valid.

    :param area: The area object representing the area.
    :param list_nodes: A list of nodes in the area.
    :param list_edges: A list of edges in the area.
    :param cNode: The node closest to the `newCoor`.
    :param newCoor: A coordinate of the new node.
    :return: A new edge if it's valid else None.
    """

    lineString = LineString([cNode.point, newCoor])
    if t.checkCross(area.list_obstacles, list_nodes, list_edges, lineString):
        return Edge(lineString, c.edgeColor)
    return None

def tryReachEnd(area : Area, list_nodes : List[Node], list_edges : List[Edge], currentNode : Node, endNode : Node) -> Union[Edge, None]:
    """
    Tries creating an edge connecting to the end node.

    :param area: The area object representing the area.
    :param list_nodes: A list of nodes in the area.
    :param list_edges: A list of edges in the area.
    :param currentNode: The current node which is trying to connect to the end node.
    :endNode: The end node.
    :return: The edge which connecting to the end node if it's valid else None.
    """

    if currentNode.point.distance(endNode.point) <= c.edgeLength:
        return createEdge(area, list_nodes, list_edges, currentNode, endNode.point)
    return None

def dfs(path : Dict[Node, Edge], currentNode : Node) -> bool:
    """
    Uses a DFS approach to find the path between start and end nodes.

    :param path: A dictionary contains nodes and edges.
    :param currentNode: The current node.
    :return A boolean indicating that the path is found or not.
    """
    if currentNode.isEnd:
        return True
    for node, edge in currentNode.neighbor.items():
        if dfs(path, node):
            path[node] = edge
            return True
    

    



    