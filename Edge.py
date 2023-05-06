"""
This module contains a class for representing an edge.

Classes:
- Edge: A class for representing an edge.

Dependencies:
- shapely: A package for manipulate geometric shapes.
"""

from shapely.geometry import LineString

class Edge:
    """
    Represents an edge.

    :ivar lineString: A LineString object which contains a set of points.
    :ivar color: A color of the edge.
    """
    def __init__(self, lineString : LineString, color : str) -> None:
        """
        Initilizes a new Edge instance with specified a set of points.

        :param lineString: A LineString object which contains a set of points.
        :param color: A color of the edge.
        """

        self.lineString = lineString
        self.color = color