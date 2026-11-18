from pathlib import Path
from dataclasses import dataclass
from typing import Iterator

import cv2
import numpy as np


@dataclass
class VideoInfo:
    width: int
    height: int
    fps: float
    total_frames: int

    @property
    def duration_seconds(self) -> float:
        return self.total_frames / self.fps if self.fps else 0.0


def get_video_info(video_path: str | Path) -> VideoInfo:
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise FileNotFoundError(f'Could not open video: {video_path}')
    info = VideoInfo(
        width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
        height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
        fps=cap.get(cv2.CAP_PROP_FPS),
        total_frames=int(cap.get(cv2.CAP_PROP_FRAME_COUNT)),
    )
    cap.release()
    return info


def read_frames(video_path: str | Path, stride: int = 1) -> Iterator[tuple[int, np.ndarray]]:
    """Yields (frame_index, frame). stride=5 processes every 5th frame."""
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise FileNotFoundError(f'Could not open video: {video_path}')
    try:
        idx = 0
        while True:
            ok, frame = cap.read()
            if not ok:
                break
            if idx % stride == 0:
                yield idx, frame
            idx += 1
    finally:
        cap.release()


def save_frame(frame: np.ndarray, output_path: str | Path) -> None:
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(output_path), frame)


class VideoWriter:
    """Context manager to write annotated videos."""
    def __init__(self, output_path: str | Path, fps: float, size: tuple[int, int]):
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fourcc = cv2.VideoWriter.fourcc(*'mp4v')
        self._writer = cv2.VideoWriter(str(output_path), fourcc, fps, size)

    def write(self, frame: np.ndarray) -> None:
        self._writer.write(frame)

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self._writer.release()