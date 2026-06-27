from utils import Widget
from typing import List


# should only be called when removing a card
def move_cards(index : int, cards : List[Widget], button : Widget, card_width : float, card_height : float, margin : float):
    # moving the button
    move_card_back(button, card_width, card_height, margin, is_button = True)
    for i in range(index, len(cards)):
        move_card_back(cards[i], card_width, card_height, margin)


# moves a widget back in a grid
def move_card_back(widget : Widget, width : float, height : float, margin : float, is_button = False):
    max_cards = int(1 / (width + margin))
    widget.change_x(widget.x - width)
    if widget.x < margin:
        widget.change_y(widget.y - (height + margin))
        new_x = margin * max_cards + (width * (max_cards - 1))
        widget.change_x(new_x)
        if is_button:
            widget.change_x(widget.x + (width / 2))
    
        
