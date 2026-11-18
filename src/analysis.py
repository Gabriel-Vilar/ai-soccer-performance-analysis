from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


def players_to_dataframe(players: list) -> pd.DataFrame:
    dict_list = [player.to_dict() for player in players]
    df = pd.DataFrame(dict_list)
    df['Category'] = df['Age'].apply(lambda x: 'Young' if x < 30 else 'Experienced')
    return df


def print_summary(df: pd.DataFrame) -> None:
    print(df.head())
    print(df.describe())
    print(df['Age'].mean())

    midfielders = df[df['Position'] == 'Attacking Midfielder']
    print(midfielders)
    print(df)

    count = df['Position'].value_counts()
    print(count)
    print()

    mean_age_per_position = df.groupby('Position')['Age'].mean()
    print(mean_age_per_position)

    ordered_by_age = df.sort_values('Age', ascending=False).head(3)
    print(ordered_by_age)


def plot_player_ages(df: pd.DataFrame, output_dir: Path, show: bool = True) -> None:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(8, 5))
    colors = ['red' if cat == 'Experienced' else 'steelblue' for cat in df['Category']]
    plt.bar(df['Name'], df['Age'], color=colors)
    plt.title("Player's age")
    plt.xlabel('Player')
    plt.ylabel('Age')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(output_dir / "player's_age.png")
    if show:
        plt.show()
    plt.close()


def plot_players_per_position(df: pd.DataFrame, output_dir: Path, show: bool = True) -> None:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    count = df['Position'].value_counts()
    plt.figure(figsize=(8, 5))
    plt.bar(count.index, count.values, color='steelblue')  # type: ignore
    plt.title('Number of players per position')
    plt.xlabel('Position')
    plt.ylabel('Number of players')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(output_dir / 'players_per_position.png')
    if show:
        plt.show()
    plt.close()