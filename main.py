"""
This script firstly generates a specified rectangular box.
Then, randomly generates obstacles and start-end point.
Finally, finds the path between two points using RRT approach.

To run the script, use the following command:
    python main.py
"""

import config as c
import get_object as go
import find_path as fp
import visualization as v

def main():
    area = go.createArea(c.areaWidth, c.areaHeight)
    area.list_obstacles = go.createObstacle(area, c.n)
    startNode, endNode = go.createStartEnd(area)
    endNode.isEnd = True
    list_nodes , list_edges= fp.rrt(area, startNode, endNode)

    v.showResult(area, list_nodes, list_edges)
    
if __name__ == "__main__":
    main()