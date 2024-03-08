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
        rewardnya = 0
        nearestDiamond = Position(0,0)
        teleState = 0
        firstItem = True
        for diamond in listDiamond:
            if firstItem:
                nearestDistance, teleState = self.nearestWithTele(diamond.position, bot.position, listTeleporters)
                rewardnya = diamond.properties.points
                nearestDiamond = diamond.position
            else:
                tempDistance, tempTeleState = self.nearestWithTele(diamond.position, bot.position, listTeleporters)
                if (tempDistance) < (nearestDistance) or (abs(tempDistance-nearestDistance) <= 2 and diamond.properties.points > rewardnya) :
                    nearestDistance = tempDistance
                    nearestDiamond = diamond.position
                    rewardnya = diamond.properties.points
                    teleState = tempTeleState
            firstItem = False
        
        return nearestDiamond, teleState, nearestDistance, rewardnya

    def findNearestDiamondAlt(self, listDiamond: list[GameObject], listTeleporters: list[GameObject], bot: GameObject):
        nearestDistance = 0
        rewardnya = 0
        nearestDiamond = Position(0,0)
        teleState = 0
        firstItem = True
        for diamond in listDiamond:
            if firstItem:
                nearestDistance, teleState = self.nearestWithTele(diamond.position, bot.position, listTeleporters)
                rewardnya = diamond.properties.points
                nearestDiamond = diamond.position
            else:
                tempDistance, tempTeleState = self.nearestWithTele(diamond.position, bot.position, listTeleporters)
                if (tempDistance) < (nearestDistance):
                    nearestDistance = tempDistance
                    nearestDiamond = diamond.position
                    rewardnya = diamond.properties.points
                    teleState = tempTeleState
            firstItem = False
        
        return nearestDiamond, teleState, nearestDistance, rewardnya

    def next_move(self, board_bot: GameObject, board: Board) :        

        props = board_bot.properties
        current_position = board_bot.position
        
        listDiamond = board.diamonds
        listTeleporters = [d for d in board.game_objects if d.type == "TeleportGameObject"]
        listButton = [d for d in board.game_objects if d.type == "DiamondButtonGameObject"]
        if props.diamonds < 3 :
            self.goal_position, teleState, nearestDist, rewardnya = self.findNearestDiamond(listDiamond, listTeleporters, board_bot)
            if teleState == 1:
                self.goal_position = listTeleporters[0].position
                print(f"otw, poinnya {rewardnya}")
                print(f"TeleporterA : ({self.goal_position.x}, {self.goal_position.y})")
            elif teleState == 2:
                self.goal_position = listTeleporters[1].position
                print(f"otw, poinnya {rewardnya}")
                print(f"TeleporterB : ({self.goal_position.x}, {self.goal_position.y})")
            else: #teleState == 0:
                print(f"waktumu sisa {board_bot.properties.milliseconds_left}")
                print(f"otw, poinnya {rewardnya}")
                print(f"Diamond : x = ({self.goal_position.x}, {self.goal_position.y})")
            
        else :
            base = board_bot.properties.base
            _, teleState1 = self.nearestWithTele(base, board_bot.position, listTeleporters)
            gp, teleState2, nearestDistDM, rewardnya = self.findNearestDiamondAlt(listDiamond, listTeleporters, board_bot)
            if (nearestDistDM <= 2 and (props.diamonds+rewardnya)<=5):
                if teleState2 == 1:
                    self.goal_position = listTeleporters[0].position
                elif teleState2 == 2:
                    self.goal_position = listTeleporters[1].position
                else: 
                    self.goal_position = gp
            else:
                self.goal_position = base
                if teleState1 == 1:
                    self.goal_position = listTeleporters[0].position
                    print(f"TeleporterA (Base) : ({self.goal_position.x}, {self.goal_position.y})")
                elif teleState1 == 2:
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