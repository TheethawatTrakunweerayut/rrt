"""
This module contains a class for representing an obstacle.

Classes:
- Obstacle: A class for representing an obstacle.

Dependencies:
- shapely: A package for manipulate geometric shapes.
"""

from typing import Union, List, Tuple
from shapely.geometry import Polygon

class Obstacle:
    """
    Represents an obstacle.

    :ivar polygon: A polygon data of the obstacle.
    :ivar lb: The left-bottom point of the obstacle.
    :ivar width: The width of the obstacle.
    :ivar height: The height of the obstacle.
    """
    def __init__(self, polygon : Polygon, lb : Union[List[Union[int, float]], Tuple[Union[int, float]]], width : Union[int, float], height : Union[int, float]) -> None:
        """
        Initializes a new Obstacle instance with the specified width and height.

        :param polygon: The polygon data of the obstacle.
        :param lb: The left-bottom point of the obstacle.
        :param width: The width of the obstacle.
        :param height: The height of the obstacle.
        """
        self.polygon = polygon
        self.lb = lb
        self.width = width
        self.height = height