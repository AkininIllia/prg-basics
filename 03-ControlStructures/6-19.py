interested_cs = input("Are you interested in computer science? (y/n): ").lower() == 'y'
playing_games = input("Do you like playing computer games? (y/n): ").lower() == 'y'
has_instagram = input("Do you have an Instagram account? (y/n): ").lower() == 'y'

print()

print("SURVEY RESULTS")
print(f"Interested in computer science: {'Yes' if interested_cs else 'No'}")
print(f"Playing computer games: {'Yes' if playing_games else 'No'}")
print(f"Has an Instagram account: {'Yes' if has_instagram else 'No'}")