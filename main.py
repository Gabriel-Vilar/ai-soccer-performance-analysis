from pathlib import Path

import cv2

from src.models import Player, showplayers, addplayer, findplayer
from src.storage import save_players, load_players
from src.analysis import (players_to_dataframe, print_summary,
                          plot_player_ages, plot_players_per_position)
from src.video_utils import get_video_info, read_frames, save_frame, VideoWriter
from src.data_sources import load_players_from_csv

DATA_DIR = Path(__file__).resolve().parent / 'data'
PLAYERS_FILE = DATA_DIR / 'players.json'
VIDEO = Path(__file__).resolve().parent / 'videos' / 'match.mp4'


def run_players_demo():
    playerlist = []
    p1 = Player('Gabriel Vilar', 18, 'Attacking Midfielder')
    p2 = Player('Matheus Vilar', 18, 'Left Winger')
    p3 = Player('Cristiano Ronaldo', 41, 'Striker')
    p4 = Player('Lionel Messi', 39, 'Right Winger')
    p5 = Player('Neymar Jr', 34, 'Attacking Midfielder')

    addplayer(playerlist, p1, p2, p3, p4, p5)
    showplayers(playerlist)
    findplayer(playerlist, 'vilar')
    print(p1 == p2)

    save_players(playerlist, PLAYERS_FILE)
    print()
    loaded_players = load_players(PLAYERS_FILE)

    df = players_to_dataframe(loaded_players)
    print_summary(df)
    plot_player_ages(df, DATA_DIR)
    plot_players_per_position(df, DATA_DIR)


def run_kaggle_demo():
    players = load_players_from_csv(
        DATA_DIR / 'players_22.csv',
        name_col='long_name',
        age_col='age',
        position_col='player_positions',
        limit=500,
    )
    # salva em outro arquivo pra não sobrescrever o players.json do demo pequeno
    save_players(players, DATA_DIR / 'players_kaggle.json')

    df = players_to_dataframe(players)
    print_summary(df)
    plot_players_per_position(df, DATA_DIR)


def run_video_demo():
    info = get_video_info(VIDEO)
    print(info, f'-> {info.duration_seconds:.1f}s')

    # salva o primeiro frame pra conferir
    for idx, frame in read_frames(VIDEO):
        save_frame(frame, DATA_DIR / 'first_frame.png')
        break

    # copia os primeiros 100 frames com texto desenhado (testa leitura + escrita)
    with VideoWriter(DATA_DIR / 'test_out.mp4', info.fps, (info.width, info.height)) as out:
        for idx, frame in read_frames(VIDEO):
            if idx >= 100:
                break
            cv2.putText(frame, f'frame {idx}', (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
            out.write(frame)


if __name__ == '__main__':
    run_players_demo()
    run_kaggle_demo()

    if VIDEO.exists():
        run_video_demo()
    else:
        print(f'\nVideo not found at {VIDEO}. Put a test video there to run the OpenCV demo.')