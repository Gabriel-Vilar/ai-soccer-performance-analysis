# AI Soccer Performance Analysis

Portfolio project that combines soccer and programming. The goal is to use Python, Computer Vision and Machine Learning to extract performance metrics (distance covered, speed, sprints, positioning) from soccer match footage.

> **Status:** work in progress. The data and video-processing foundations are done; detection, tracking and metrics are being built.

## What it does today

- **Player data model:** `Player` class (name, age, position) with input validation, equality check and dict conversion.
- **Persistence:** save and load players as JSON.
- **Data analysis (Pandas):** average age, players per position, average age per position, oldest players, Young/Experienced categories.
- **Visualization (Matplotlib):** charts of player ages and players per position.
- **Large datasets:** import players from a Kaggle CSV (FIFA/EA FC player data), skipping invalid rows.
- **Video processing (OpenCV):** read video metadata, iterate over frames, save frames and write annotated videos.

## Roadmap

| Step | Status |
|---|---|
| Player data structure | Done |
| Save/load data in JSON | Done |
| Basic data analysis (Pandas) | Done |
| Data visualization (Matplotlib) | Done |
| Video processing (OpenCV) | In progress |
| Player detection (YOLO) | In progress |
| Player tracking | Planned |
| Performance metrics calculation | Planned |
| Dashboard with visualizations | Planned |

## Project structure

```
ai-soccer-performance-analysis/
├── main.py              # entry point with the demos
├── requirements.txt
├── data/                # generated files and datasets (not versioned)
├── videos/              # match footage (not versioned)
└── src/
    ├── models.py        # Player class and list helpers
    ├── storage.py       # JSON save/load
    ├── analysis.py      # Pandas analysis and Matplotlib charts
    ├── data_sources.py  # CSV import (e.g. Kaggle)
    ├── video_utils.py   # OpenCV helpers
    └── detection.py     # YOLO detection and tracking (in progress)
```

## Getting started

```bash
git clone https://github.com/Gabriel-Vilar/ai-soccer-performance-analysis.git
cd ai-soccer-performance-analysis

python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

pip install -r requirements.txt
python main.py
```

### Optional data

- **Players dataset:** download a FIFA/EA FC players CSV from Kaggle and save it as `data/players_22.csv`.
- **Match video:** place a video at `videos/match.mp4`. A fixed camera that shows the whole pitch works best.

Without these files, `main.py` still runs the small players demo and tells you what is missing.

## Planned approach for video analysis

1. Detect players and the ball with YOLO (`ultralytics`).
2. Track them across frames to keep a stable ID per player.
3. Calibrate the pitch (homography) to convert pixels to meters.
4. Compute distance, speed and sprints per player.
5. Show everything in a dashboard.

Metrics in meters need a fixed camera or per-frame pitch calibration. A fixed camera is the first target.

## Tech stack

Python, OpenCV, Pandas, Matplotlib, NumPy, Ultralytics YOLO.

## Data and licensing

Datasets and videos are not included in this repository. If you use a Kaggle dataset, check its license and credit the source.