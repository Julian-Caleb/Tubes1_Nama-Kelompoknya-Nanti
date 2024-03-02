from typing import Optional
from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction

class GreedyV1(BaseLogic) :
    def __init__(self) :
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.current_direction = 0

    def findNearestDiamond(self, listDiamond: list[GameObject], bot: GameObject):
        nearestDistance = Position(0,0) 
        nearestDiamond = Position(0,0)
        firstItem = True
        for item in listDiamond:
            if firstItem:
                nearestDistance.x = abs(item.position.x - bot.position.x) 
                nearestDistance.y = abs(item.position.y - bot.position.y)
                nearestDiamond = item.position
            else:
                if ((abs(item.position.x - bot.position.x) + abs(item.position.y - bot.position.y)) < (nearestDistance.x + nearestDistance.y)):
                    nearestDistance.x = abs(item.position.x - bot.position.x)
                    nearestDistance.y = abs(item.position.y - bot.position.y)
                    nearestDiamond = item.position
            firstItem = False
        
        return nearestDiamond

    def next_move(self, board_bot: GameObject, board: Board) :        

        props = board_bot.properties
        current_position = board_bot.position
        
        listDiamond = board.diamonds
        if props.diamonds < 5 :
            self.goal_position = self.findNearestDiamond(listDiamond, board_bot)
            print(f"Diamond : x = {self.goal_position.x}, y = {self.goal_position.y}")
                        
        else :
            base = board_bot.properties.base
            print(f"Base : x = {base.x}, y = {base.y}")
            self.goal_position = base
        
        delta_x, delta_y = get_direction(
            current_position.x,
            current_position.y,
            self.goal_position.x,
            self.goal_position.y,
        )

        return delta_x, delta_y