#15X9 with borders. 13X7 without borders.(17X11)
#60 pixels per tile.
from .obstacle_class import *
from .platform_class import *
#Add an obstacle class for 1 in map. Add to platform.all_sprites
def generate_map(platform : platforms, map):
    height = len(map)
    width = len(map[0])
    for idy, i in enumerate(map):
        for idx, j in enumerate(i):
            if j == 1:
                tempObstacle = obstacle(((WIDTH/width)*idx, HEIGHT/height*idy))
                platform.obstacles.add(tempObstacle)
                platform.all_sprites.add(tempObstacle)
            
    #tempObstacle1 = obstacle(((WIDTH/width)*4, HEIGHT/height))
    #tempObstacle = obstacle(((WIDTH/width)*2, HEIGHT/height))
    #platform.obstacles.add(tempObstacle, tempObstacle1)
    #platform.all_sprites.add(tempObstacle, tempObstacle1)
class map_generator():
    def __init__(self) -> None:
        pass