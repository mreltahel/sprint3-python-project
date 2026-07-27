# a) Total number of games
total_games = len(video_game_sales)
print(total_games)

# b) Average global sales across all 20 games
total_global_sales = sum(game[GLOBAL_SALES] for game in video_game_sales)
avg_global_sales = total_global_sales / total_games
print(f"Average global sales across all {total_games} games: {avg_global_sales:.2f} million")

# c) Percentage share of the top game (Wii Sports, index 0)
top_game_share = (video_game_sales[0][GLOBAL_SALES] / total_global_sales) * 100
print(f"{video_game_sales[0][NAME]} accounts for {top_game_share:.2f}% of total global sales")
