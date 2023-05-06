"""
Configuration file.

This file contains various variables that control the result.

Variables:
- Area
    - areaWidth: An integer or float indicating the width of the rectangular box.
    - areaHeight: An integer of float indicating the height of the rectangular box.
    - areaLinewidth: An integer or float indicating the width of the rectangular box's boundary.
    - areaEdgecolor: A character or string indicating the color of the rectangular box's boundary.
    - areaFacecolor: A character or string indicating the color of the rectangular box's face.
- Obstacles
    - n: An integer indicating a number of obstacles to be created.
    - obsHeightRange: A pair of integer or float indicating the obstacle height range.
    - obsWidthRange: A pair of integer or float indicating the obstacle width range.
    - obsEdgecolor: A character or string indicating the color of the obstacle's boundary.
    - obsFacecolor: A character or string indicating the color of the obstacle's face.
- Start and End nodes
    - StartEndRadius: An integer or float indicating the radius of start and end points.
    - startColor: A string indicating the color of the start point.
    - endColor: A string indicating tje color of the end point.
- Node
    - nodeRadius: An integer or float indicating the radius of the node.
    - nodeColor: A string indicating a color of the node.
- Edge
    - edgeLinewidth: An integer or float indicating the width of the edge.
    - edgeColor: A string indicating the color of the edge.
- Path
    - pathColor: A string indicating the color of the path.
- RRT
    - f: A frequency at which to try creating the way to the end point directly.
- Visualization
    - bgColor: A string indicating the color of the background.
"""

# Area
areaWidth, areaHeight = (50, 30)
areaLinewidth = 2
areaEdgecolor = "black"
areaFacecolor = "none"

# Obstacle
n = 15
obsHeightRange = (2, 5)
obsWidthRange = (2, 5)
obsEdgecolor = "black"
obsFacecolor = "black"

# Start-End nodes
StartEndRadius = 1
startColor = "green"
endColor = "red"

# Node
nodeRadius = 0.08
nodeColor = "blue"

# Edge
edgeLength = 1.5
edgeLinewidth = 1
edgeColor = "purple"

# Path
pathColor = "yellow"

# RRT
f = 10

# Visualization
bgColor = "lightgray"
