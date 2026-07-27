# a) Function to sum NA + EU + JP sales for a single game
def calculate_total_sales(game):
    return game[NA_SALES] + game[EU_SALES] + game[JP_SALES]

first_game_total = calculate_total_sales(video_game_sales[0])
print(first_game_total)

# b) Function to filter dataset by genre, with a default genre
def filter_by_genre(data, genre='Platform'):
    filtered = []
    for game in data:
        if game[GENRE] == genre:
            filtered.append(game)
    return filtered

platform_games = filter_by_genre(video_game_sales)
racing_games = filter_by_genre(video_game_sales, 'Racing')

print(f"Platform games (default): {[g[NAME] for g in platform_games]}")
print(f"Racing games: {[g[NAME] for g in racing_games]}")

# c) Function to build a formatted summary string for a game
def get_summary(game):
    return f"{game[NAME]} ({game[YEAR]}) - {game[GENRE]} - ${game[GLOBAL_SALES]}M"

for game in video_game_sales:
    print(get_summary(game))
