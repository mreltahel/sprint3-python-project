# a) Print name and global sales for games with global sales > 25 million
for game in video_game_sales:
    if game[GLOBAL_SALES] > 25:
        print(f"{game[NAME]}: {game[GLOBAL_SALES]}M")

# b) Count games released before 2000
pre_2000_count = 0
for game in video_game_sales:
    if game[YEAR] < 2000:
        pre_2000_count += 1
print(pre_2000_count)

# c) Total NA sales vs total JP sales
total_na_sales = 0
total_jp_sales = 0
for game in video_game_sales:
    total_na_sales += game[NA_SALES]
    total_jp_sales += game[JP_SALES]

print(f"Total NA sales: {total_na_sales:.2f}M")
print(f"Total JP sales: {total_jp_sales:.2f}M")

if total_na_sales > total_jp_sales:
    print("North America had higher sales.")
elif total_jp_sales > total_na_sales:
    print("Japan had higher sales.")
else:
    print("NA and JP sales were equal.")

# d) List of Nintendo-published game names
nintendo_games = []
for game in video_game_sales:
    if game[PUBLISHER] == 'Nintendo':
        nintendo_games.append(game[NAME])
print(nintendo_games)
print(len(nintendo_games))
