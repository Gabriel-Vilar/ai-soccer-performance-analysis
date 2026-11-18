from pathlib import Path

import pandas as pd

from src.models import Player


def load_players_from_csv(csv_path: str | Path,
                          name_col: str = 'long_name',
                          age_col: str = 'age',
                          position_col: str = 'player_positions',
                          limit: int | None = None) -> list[Player]:
    """Reads a CSV (e.g. a Kaggle FIFA/EA FC dataset) and builds Player objects.
    Adjust the column names to match your file."""
    df = pd.read_csv(csv_path, low_memory=False)
    if limit:
        df = df.head(limit)

    players, skipped = [], 0
    for _, row in df.iterrows():
        try:
            # some datasets list several positions ("RW, ST"): keep the first
            position = str(row[position_col]).split(',')[0].strip()
            players.append(Player(str(row[name_col]), int(row[age_col]), position))
        except (ValueError, TypeError):
            skipped += 1  # invalid name/age (your Player validation rejects it)
    print(f'Loaded {len(players)} players, skipped {skipped} invalid rows')
    return players