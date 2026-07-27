# a) Extract "Pokemon" from the 5th game's name using string indexing
game_name = video_game_sales[4][NAME]
pokemon_word = game_name[0:7]
print(pokemon_word)

# b) Clean up messy names
messy_names = ['  Wii Sports  ', 'TETRIS', '  mario kart WII']
for name in messy_names:
    cleaned = name.strip().lower()
    print(cleaned)

# c) Formatted summary of the #1 game
top_game = video_game_sales[0]
print(f"#{top_game[RANK]} Best Seller: {top_game[NAME]} ({top_game[YEAR]}) - ${top_game[GLOBAL_SALES]}M global sales")
