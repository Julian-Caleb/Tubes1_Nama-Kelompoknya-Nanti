from typing import Optional
from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction

# The programmer said to the bot,
# "Are you finding the nearest diamond because you are greedy,
# or are you greedy because you are finding the nearest diamond?"

# The bot simply responsed,
# "Nah, I'd greedy".

# The bot always bet on greedy. He used his domain expansion,
# "Malevolent Board" and used his RCT to get to the base faster
# than the opponent's bot.

# And when he win, he said to the opponent's bot,
# "Stand proud, you have optimal time complexity".

class JustMoveBro(BaseLogic) :
    # Cursed energy manipulation: Constructor
    def __init__(self) :
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.current_direction = 0
        
    # Cursed energy manipulation: Move 
    def next_move(self, board_bot: GameObject, board: Board) :        
        # Cursed Technique: Find one's position
        props = board_bot.properties
        current_position = board_bot.position
        
        # Domain Expansion, "Malevolent Board": 
        # Finding the nearest diamond, bot, and base
        listDiamond = board.diamonds
        if props.diamonds < 3 :
            self.goal_position = listDiamond[0].position
            print(f"Diamond : x = {listDiamond[0].position.x}, y = {listDiamond[0].position.y}")
                        
        # Reverse Cursed Technique: Store the diamonds in base
        else :
            base = board_bot.properties.base
            print(f"Base : x = {base.x}, y = {base.y}")
            self.goal_position = base
        
        # Cursed Technique: Find one's position
        delta_x, delta_y = get_direction(
            current_position.x,
            current_position.y,
            self.goal_position.x,
            self.goal_position.y,
        )

        return delta_x, delta_y