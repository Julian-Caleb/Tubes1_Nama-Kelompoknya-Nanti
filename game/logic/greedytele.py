from typing import Optional
from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction

class GreedyTele(BaseLogic) :
    def __init__(self) :
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.current_direction = 0

    def distance(self, a: Position, b:Position):
        return abs(a.x - b.x) + abs(a.y - b.y)
    
    def nearestWithTele(self, targetPos : Position, botPos : Position, listTeleporters : list[GameObject]):
        TeleA = listTeleporters[0].position
        TeleB = listTeleporters[1].position
        teleState = 0
        nearestDistance = self.distance(botPos, targetPos)
        if (nearestDistance > (self.distance(botPos, TeleA) + self.distance(TeleB, targetPos))):
            teleState = 1
            nearestDistance = self.distance(botPos, TeleA) + self.distance(TeleB, targetPos)
        if (nearestDistance > (self.distance(botPos, TeleB) + self.distance(TeleA, targetPos))):
            teleState = 2
            nearestDistance = self.distance(botPos, TeleB) + self.distance(TeleA, targetPos)
        return nearestDistance, teleState


    def findNearestDiamond(self, listDiamond: list[GameObject], listTeleporters: list[GameObject], bot: GameObject):
        nearestDistance = 0
        nearestDiamond = Position(0,0)
        teleState = 0
        firstItem = True
        for diamond in listDiamond:
            if firstItem:
                nearestDistance, teleState = self.nearestWithTele(diamond.position, bot.position, listTeleporters)
                nearestDiamond = diamond.position
            else:
                tempDistance, tempTeleState = self.nearestWithTele(diamond.position, bot.position, listTeleporters)
                if (tempDistance) < (nearestDistance):
                    nearestDistance = tempDistance
                    nearestDiamond = diamond.position
                    teleState = tempTeleState
            firstItem = False
        
        return nearestDiamond, teleState

    def next_move(self, board_bot: GameObject, board: Board) :        

        props = board_bot.properties
        current_position = board_bot.position
        
        listDiamond = board.diamonds
        listTeleporters = [d for d in board.game_objects if d.type == "TeleportGameObject"]
        if props.diamonds < 3 :
            self.goal_position, teleState = self.findNearestDiamond(listDiamond, listTeleporters, board_bot)
            if teleState == 1:
                self.goal_position = listTeleporters[0].position
                print(f"TeleporterA : ({self.goal_position.x}, {self.goal_position.y})")
            elif teleState == 2:
                self.goal_position = listTeleporters[1].position
                print(f"TeleporterB : ({self.goal_position.x}, {self.goal_position.y})")
            else: #teleState == 0:
                print(f"Diamond : x = ({self.goal_position.x}, {self.goal_position.y})")
            
        else :
            base = board_bot.properties.base
            _, teleState = self.nearestWithTele(base, board_bot.position, listTeleporters)
            self.goal_position = base
            if teleState == 1:
                self.goal_position = listTeleporters[0].position
                print(f"TeleporterA (Base) : ({self.goal_position.x}, {self.goal_position.y})")
            elif teleState == 2:
                self.goal_position = listTeleporters[1].position
                print(f"TeleporterB (Base) : ({self.goal_position.x}, {self.goal_position.y})")
            else: #teleState == 0:
                print(f"Base : x = {self.goal_position.x}, y = {self.goal_position.y}")
            
        
        delta_x, delta_y = get_direction(
            current_position.x,
            current_position.y,
            self.goal_position.x,
            self.goal_position.y,
        )

        return delta_x, delta_y