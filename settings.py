"""
System Configuration
Industrial AI Safety Monitoring System
"""

from pathlib import Path


class Settings:

    # =========================================
    # CAMERA SETTINGS
    # =========================================

    CAMERA_SOURCE = 0

    FRAME_WIDTH = 1280

    FRAME_HEIGHT = 720

    FPS = 20


    # =========================================
    # AI SETTINGS
    # =========================================

    CONFIDENCE_THRESHOLD = 0.4

    FIRE_CONFIDENCE = 0.4

    SMOKE_CONFIDENCE = 0.4


    # =========================================
    # OUTPUT SETTINGS
    # =========================================

    OUTPUT_DIR = "outputs"

    SNAPSHOT_FORMAT = "jpg"

    VIDEO_CODEC = "mp4v"

    VIDEO_FPS = 20

    CLIP_DURATION_SECONDS = 10


    # =========================================
    # ALERT SETTINGS
    # =========================================

    ALERT_COOLDOWN_SECONDS = 10

    TELEGRAM_ENABLED = False

    EMAIL_ENABLED = False

    SIREN_ENABLED = False


    # =========================================
    # MODEL PATHS
    # =========================================

    FIRE_SMOKE_MODEL = "weights/fire_smoke.pt"

    OBJECT_MODEL = "weights/yolov8n.pt"


    # =========================================
    # TRACKING SETTINGS
    # =========================================

    TRACK_MAX_AGE = 30

    TRACK_MIN_HITS = 3


    # =========================================
    # PATHS
    # =========================================

    BASE_DIR = Path(__file__).resolve().parent.parent

    OUTPUT_PATH = BASE_DIR / OUTPUT_DIR

    OUTPUT_PATH.mkdir(
        exist_ok=True
    )