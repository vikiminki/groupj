"""Tournament manager menus module."""


def ask_input(msg, type=str, allow_empty=False):
    """Ask for user input."""
    answer = None
    while answer is None or not allow_empty and answer == '':
        answer = input('% s\n> ' % msg).strip()

    if type == str:
        return answer
    elif type == int:
        try:
            return int(answer)
        except ValueError:
            return 0


def ask_players(num_players=None, min_players=3, max_players=8):
    """Ask user for number of players and the player info."""
    if num_players is None:
        # Ask how many players
        num_players = ask_input('Enter number of players:', type=int)
        while num_players < min_players or num_players > max_players:
            print('The tournament only allows {} to {} players'.format(
                min_players, max_players
            ))
            num_players = ask_input('Enter number of players:', type=int)

    players = []
    names = []
    for n in range(1, num_players+1):
        while True:
            name = ask_input('Enter name of "Player {}":'.format(n))
            if name in names:
                print('Please enter a unique name, try again!')
            else:
                names.append(name)
                break
        ai_types = ["easy", "medium", "hard", ""]
        ai_difficulty = "Dummy"
        while not ai_difficulty in ai_types:
            ai_difficulty = ask_input(
                'Enter AI difficulty (easy/medium/hard or leave empty if human):',
                allow_empty=True
            ).lower()
            if not ai_difficulty in ai_types:
                print("You have entered an invalid input, please try again.")
            pass
        players.append((name, ai_difficulty))
    return players
