import pandas as pd

# Define the strategy legend
STRATEGY_LEGEND = {
    "P": "SPLIT",
    "S": "STAND",
    "H": "HIT",
    "D": "DOUBLE DOWN",
    "Sr": "Not sure"
}

# Load the strategy data
df = pd.read_csv('basicstrategy_hit_soft17.csv')

def calculate_basic_strategy(player_cards, dealer_card):
    if 'A' in player_cards or len(set(player_cards)) == 1:
        player = ''.join(player_cards)
    else:
        player = sum(int(card) for card in player_cards)

    player_moves = df[df['Player'] == f'{player}']
    dealer_moves = player_moves[f'{dealer_card}'].values[0]

    return STRATEGY_LEGEND[dealer_moves]

def main():
    while True:
        # Initialize player and dealer hands
        player_cards = []
        dealer_card = ""

        # Get player cards
        for i in range(2):
            card = input(f"Enter player card {i+1}: ")
            player_cards.append(card)

        # Get dealer card
        dealer_card = input("Enter dealer card: ")

        # Calculate and print the recommended strategy
        strategy = calculate_basic_strategy(player_cards, dealer_card)
        print(f"You should: {strategy}")

        # Ask the user if they want to continue
        play_again = input("Do you want to play again? (y/no): ")
        if play_again.lower() != "y":
            break

if __name__ == "__main__":
    main()
