class Player:
    def __init__(self, name, position, attributes):
        self.name = name
        self.position = position
        self.attributes = attributes

def read_players(file_path: str) -> list:
    players = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                name = data[0]
                position = data[1]
                attributes = {}
                for attribute in data[2:]:
                    attr_name, attr_value = attribute.split('=')
                    attributes[attr_name.strip()] = int(attr_value)
                player = Player(name, position, attributes)
                players.append(player)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    return players

def choose_best_player(players: list, position: str, attributes_to_measure: list) -> Player:
    best_player = None
    best_score = -1
    for player in players:
        if player.position == position:
            score = sum(player.attributes.get(attr, 0) for attr in attributes_to_measure)
            if score > best_score:
                best_score = score
                best_player = player
    return best_player

def main():
    # Read players from file
    players = read_players('players.txt')

    if not players:
        print("No players found.")
        return

    # Define attributes to measure for each position
    positions_attributes = {
        'CF': ['Finishing', 'Positioning', 'Dribbling', 'Strength', 'Pace', 'Heading Ability', 'Link-Up Play', 'Off-the-ball Movement', 'Vision and Creativity'],
        'RW': ['Dribbling', 'Crossing', 'Pace', 'Shooting', 'Off-the-ball Movement'],
        'LW': ['Dribbling', 'Crossing', 'Pace', 'Shooting', 'Off-the-ball Movement'],
        'DM': ['Tackling', 'Interceptions', 'Passing Accuracy', 'Positioning', 'Work Rate'],
        'LDM': ['Tackling', 'Interceptions', 'Passing Accuracy', 'Positioning', 'Work Rate'],
        'RDM': ['Tackling', 'Interceptions', 'Passing Accuracy', 'Positioning', 'Work Rate'],
        'LB': ['Tackling', 'Positioning', 'Crossing', 'Stamina', 'Defensive Awareness'],
        'LCB': ['Tackling', 'Heading Ability', 'Positioning', 'Strength', 'Passing'],
        'RCB': ['Tackling', 'Heading Ability', 'Positioning', 'Strength', 'Passing'],
        'RB': ['Tackling', 'Positioning', 'Crossing', 'Stamina', 'Defensive Awareness'],
        'Goalkeeper': ['Shot Stopping', 'Handling', 'Positioning', 'Command of Area', 'Distribution']
    }

    # Choose best player for each position
    lineup = {}
    substitutes = []

    for position, attributes in positions_attributes.items():
        best_player = choose_best_player(players, position, attributes)
        if best_player:
            lineup[position] = best_player.name
            players.remove(best_player)  # Remove player from available players
        else:
            print(f"No player found for position {position}.")

    # Output lineup
    print("Starting Lineup:")
    print("________________")
    for position, player in lineup.items():
        print(f"{position}: {player}")

    # Output substitutes
    print("\nSubstitutes:")
    print("________________")
    for player in players:
        print(player.name)


if __name__ == "__main__":
    main()
