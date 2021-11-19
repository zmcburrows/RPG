
def character_information():
    while (True):
        menu = input('''
        Type option:

        Background
        The House on Ash Tree Lane
        Family and Friends
        Quit

        ''')
        if menu == "background":
            print('''
        You are Will Navidson, a Pulitzer prize winning photojournalist 
        who set out to make a film about him and his family settling down
        in Virginia, only to come across something entirely
        ''')
        elif menu == "the house on ash tree lane":
            print('''
        The events that occured in the House on Ash Tree Lane 
        started with a room that was 3/4 of an inch bigger on the inside than the outside of the house. 
        This gradual expansion continued with new rooms until a doorway appeared in the living room,
        leading to an impossible hallway filled with ink black endless hallways and rooms that grew and grew into great rooms 
        and staircases that stretched for miles that would grow and shrink based on the occupant. The House is of an unknown age 
        but is at least older than our solar system. No one knows who built the House, or whether the House was even built by 
        a somebody 
        as it seems to be its own entity, but there is something that exists in the House. It has no form, but stalks
        whoever enters the House and haunts those who know of its existence. The House has claimed three lives.
        ''')
        elif menu == "family and friends":
            print(''' 
        Karen(wife) - Alive
        Chad(son) - Alive
        Daisy(daugther) - Alive
        Tom Navidson(brother) - Dead(swallowed by the House)
        Billy Reston(friend) - Alive
        Holloway Roberts(friend) - Dead(driven to suicide by the 'Monster')
        Kirby(friend) - Alive
        Jed(friend) - Dead(shot by Holloway)
            ''')
        elif menu == "quit":
            break