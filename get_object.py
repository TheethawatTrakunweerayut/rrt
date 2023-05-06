"""
This module contains functions which creating an object and checking whether it
is valid or not.

Functions:
- createArea: Creates a new Area object with the specifed width and height.
- createObstacle: Randomly creates new Obstcles with randomized width and height.
- createStartEnd: Creates start and end node with randomized location.

Classes:
- Area: A class for representing a rectangular box.
- Obstacle: A class for representing an obstacle.
- Node: A class for representing a node.

Dependencies:
- shapely: A package for manipulating geometric shapes.
- random: A module provides functions for generating random numbers or selections.
"""

from typing import Union, List
from shapely.geometry import Polygon, Point
import random as rd
import config as c
import tools as t
from Area import Area
from Obstacle import Obstacle
from Node import Node

def createArea(width : Union[int, float], height : Union[int, float]) -> Area:
    """
    Creates a new Area object with the specified width and height.

    :param width: An integer representing the width of rectangular box.
    :param height: An integer representing the height of rectangular box.
    :return: An instance variable of Area class.
    """
    
    area = Area(Polygon([(0, 0), (width, 0), (width, height), (0, height)]), width, height)

    return area

def createObstacle(area : Area, n : int) -> List[Obstacle]:
    """
    Creates new Obstacles object with randomized width and height.

    :param area: An Area object representing the area.
    :param n: An integer indicating a number of obstacles to be created.
    :return: A list of obstacles.
    """

    list_obstacles = []
    counter = 0

    while counter < n:
        lb_x, lb_y = (rd.uniform(0.0, area.width), rd.uniform(0.0, area.height))
        height = rd.uniform(c.obsHeightRange[0], c.obsHeightRange[1])
        width = rd.uniform(c.obsWidthRange[0], c.obsWidthRange[1])

        polygon = Polygon([(lb_x, lb_y), (lb_x + width, lb_y), (lb_x + width, lb_y + height), (lb_x, lb_y + height)])
        if t.checkArea(area, polygon):
            list_obstacles.append(Obstacle(polygon, (lb_x, lb_y), width, height))
            counter += 1
    return list_obstacles

def createStartEnd(area : Area) -> List[Node]:
    """
    Creates start and end nodes with randomized location.

    :param area: An area object representing the area.
    :return: A tuple that contains start and end nodes.
    """

    list_nodes = []
    counter = 0
    color = c.startColor  

    while counter < 2:
        coor = (rd.uniform(0.0, area.width), rd.uniform(0.0, area.height))
        circle = Point(coor).buffer(c.StartEndRadius)
      
        if t.checkFree(area.list_obstacles, circle):
            list_nodes.append(Node(coor, c.StartEndRadius, color))
            color = c.endColor
            counter += 1
    return list_nodes
    