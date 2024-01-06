import ast

def get_optimal_throws(target):
    # Valid doubles on a standard dartboard
    valid_doubles = [2 * i for i in range(1, 21)]

    for dart1 in range(1, 21):
        for dart2 in range(1, 21):
            for double in valid_doubles:
                if dart1 * 3 + dart2 * 3 + double == target:
                    return [f"triple {dart1}", f"triple {dart2}", f"double {double}"]

    return []


def assign_possible_checkouts(score):
   with open('C:\\Users\\barna\\IdeaProjects\\HelloWorld\\dartscheckouts.txt') as f:
       possible_checkouts = ast.literal_eval(f.read())
   return possible_checkouts.get(score, [])



def play_501_darts():
    player1_name = input("Enter the name for Player 1: ")
    player2_name = input("Enter the name for Player 2: ")

    players = [player1_name, player2_name]
    scores = {player: 501 for player in players}
    total_points = {player: 0 for player in players}
    total_rounds = {player: 0 for player in players}
    current_player = players[0]

    while all(score > 0 for score in scores.values()):
        try:
            points = int(input(f"{current_player}, enter points scored in this throw (or 0 to exit): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if points == 0:
            print("Exiting the game.")
            break
        elif points < 0 or points > 180:
            print("Invalid points. Please enter a number between 0 and 180.")
            continue

        scores[current_player] -= points
        total_points[current_player] += points
        total_rounds[current_player] += 1
        print(f"{current_player}'s score: {scores[current_player]}")

        if scores[current_player] == 0:
            print(f"Congratulations, {current_player}! You've reached zero. You won!")
            break
        elif scores[current_player] < 0:
            print(f"Bust! {current_player}'s score is below zero. Try again.")
            scores[current_player] += points  # Undo the invalid move
        elif scores[current_player] <= 170:
            possible_checkout = assign_possible_checkouts(scores[current_player])
            if possible_checkout:
                print(f"{current_player}, to win, you should throw: {possible_checkout}")
            else:
                print(f"No possible checkouts found for {current_player}'s remaining score.")

        # Switch to the next player
        current_player = players[1] if current_player == players[0] else players[0]

    # Calculate average thrown score for each player
    for player in players:
        average_score = total_points[player] / total_rounds[player] if total_rounds[player] > 0 else 0
        print(f"{player}'s average thrown score: {average_score:.2f}")


if __name__ == "__main__":
    play_501_darts()