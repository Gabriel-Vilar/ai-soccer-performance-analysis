# AI Soccer Performance Analysis

AI-powered soccer performance analysis using Python and Computer Vision.

## Status
🚧 In development

## Goal
Portfolio project combining interest in soccer and programming, applying
Python, Computer Vision, and Machine Learning to extract performance
metrics (distance covered, speed, sprints, positioning) from soccer match
footage.

## Technologies (so far)
- Python
- Pandas (data analysis)
- Matplotlib (data visualization)

## Roadmap
- [x] Player data structure
- [x] Save/load data in JSON
- [x] Basic data analysis (Pandas)
- [x] Data visualization (Matplotlib)
- [ ] Video processing (OpenCV)
- [ ] Player detection (YOLO)
- [ ] Player tracking
- [ ] Performance metrics calculation
- [ ] Dashboard with visualizations

## How to run

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-repo>
   ```

2. Install dependencies:
   ```bash
   pip install pandas matplotlib
   ```

3. Run the main script:
   ```bash
   python main.py
   ```

This will create/update `data/players.json` with sample player data and
generate two charts in the `data/` folder:
- `player's_age.png` — bar chart of player ages
- `players_per_position.png` — bar chart of players per position

## Author
Gabriel Vilar

