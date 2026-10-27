"""Reusable PCD functions for the study desk image classification project."""
from pathlib import Path
import cv2
import numpy as np


def load_rgb(path: str | Path) -> np.ndarray:
    """Load a BGR file with OpenCV and return a RGB image."""
    path = Path(path)
    image = cv2.imread(str(path), cv2.IMREAD_COLOR)
    if image is None:
        raise FileNotFoundError(f"Could not read image: {path}")
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def clahe_rgb(image_rgb: np.ndarray, clip_limit: float = 2.0,
              tile_grid_size: tuple[int, int] = (8, 8)) -> np.ndarray:
    """Apply CLAHE to LAB luminance and return a 3-channel RGB image."""
    lab = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    l = clahe.apply(l)
    return cv2.cvtColor(cv2.merge((l, a, b)), cv2.COLOR_LAB2RGB)


def canny_edges(image_rgb: np.ndarray, low: int = 100,
                high: int = 200) -> np.ndarray:
    """Return 1-channel binary Canny edges for feature extraction."""
    gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)
    smooth = cv2.GaussianBlur(gray, (5, 5), 0)
    return cv2.Canny(smooth, low, high)


def edge_density(edges: np.ndarray) -> float:
    """Fraction of pixels with an edge (0..1)."""
    if edges.size == 0:
        raise ValueError('Empty edge image')
    return float(np.count_nonzero(edges) / edges.size)
