import os
import glob
import pandas as pd

game_files = glob.glob(os.path.join(os.getcwd(), 'games', '*.EVE'))
game_files.sort()

keywords = ['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6', 'event']

game_frames = []
for game_file in game_files:
    games = pd.concat(game_frames)
    game_frame = pd.read_csv(game_file, names=keywords)
    game_frames.append(game_frame)

games.loc["", 'multi5']