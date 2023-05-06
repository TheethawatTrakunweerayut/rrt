"""
This module contains a class for representing a rectangular box.

Classes:
- Area: A class for representing a rectangular box.

Dependencies:
- shapely: A package for manipulate geometric shapes.
"""

from typing import Union
from shapely.geometry import Polygon

class Area:
    """
    Represents a rectangular box.

    :ivar polygon: A polygon data of the rectangular box.
    :ivar width: The width of the rectangular box.
    :ivar height: The height of the rectangular box.
    :ivar list_obstacles: A list of obstacles in the rectangular box.
    """
    def __init__(self, polygon : Polygon, width : Union[int, float], height : Union[int, float]) -> None:
        """
        Initializes a new Area instance with the specified width and height.

        :param polygon: The polygon data of the rectangular box.
        :param width: The width of the rectangular box.
        :param height: The height of the rectangular box.
        """
        self.polygon = polygon
        self.width = width
        self.height = height
        self.list_obstacles = []