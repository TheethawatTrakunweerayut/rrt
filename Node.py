"""
This module contains a class for representing a node.

Classes:
- Node: A class for representing a node.
"""

from typing import Union, Tuple, List
from shapely.geometry import Point

class Node:
    """
    Represents a node.

    :ivar coor: A coordinate of the node.
    :ivar point: A coordinate of the node (variable type is Point).
    :ivar radius: The radius of the node.
    :ivar color: The color of the node.
    :ivar neighbor: A dictionary containing the neighbor nodes and edges that connect to them.
    """
    def __init__(self, coor: Union[List[Union[int, float]], Tuple[Union[int, float]]], radius : Union[int, float], color : str) -> None:
        """
        Initilizes a new Point instance with specifed center and radius.

        :param coor: A coordinate of the node.
        :param radius: The radius of the node.
        :param color: The color of the node.
        """

        self.coor = coor
        self.point = Point(coor)
        self.radius = radius
        self.color = color
        self.neighbor = {}
        self.isEnd = False