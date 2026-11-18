from pathlib import Path

import pandas as pd
from ultralytics import YOLO

from src.video_utils import get_video_info, VideoWriter

PERSON = 0       # COCO class ids
SPORTS_BALL = 32
CLASS_NAMES = {PERSON: 'player', SPORTS_BALL: 'ball'}


def track_video(video_path: str | Path,
                output_video: str | Path,
                output_csv: str | Path,
                model_name: str = 'yolo11n.pt',
                conf: float = 0.3,
                max_frames: int | None = None) -> pd.DataFrame:
    """Detects + tracks players and ball, writes an annotated video and a CSV of positions."""
    info = get_video_info(video_path)
    model = YOLO(model_name)  # weights are downloaded on the first run

    results = model.track(
        source=str(video_path),
        stream=True,
        persist=True,
        classes=[PERSON, SPORTS_BALL],
        conf=conf,
        tracker='bytetrack.yaml',
        verbose=False,
    )

    rows = []
    with VideoWriter(output_video, info.fps, (info.width, info.height)) as out:
        for frame_idx, r in enumerate(results):
            if max_frames is not None and frame_idx >= max_frames:
                break

            out.write(r.plot())  # frame with boxes and IDs drawn

            boxes = r.boxes
            if boxes is None or len(boxes) == 0:
                continue

            xyxy = boxes.xyxy.tolist()
            confs = boxes.conf.tolist()
            classes = [int(c) for c in boxes.cls.tolist()]
            ids = [int(i) for i in boxes.id.tolist()] if boxes.id is not None else [None] * len(xyxy)

            for (x1, y1, x2, y2), c, cls, tid in zip(xyxy, confs, classes, ids):
                rows.append({
                    'frame': frame_idx,
                    'time_s': frame_idx / info.fps if info.fps else 0,
                    'track_id': tid,
                    'class': CLASS_NAMES.get(cls, str(cls)),
                    'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2,
                    'foot_x': (x1 + x2) / 2,   # bottom-center = where the player touches the ground
                    'foot_y': y2,
                    'conf': c,
                })

    df = pd.DataFrame(rows)
    output_csv = Path(output_csv)
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_csv, index=False)
    print(f'Saved {len(df)} detections to {output_csv}')
    return df