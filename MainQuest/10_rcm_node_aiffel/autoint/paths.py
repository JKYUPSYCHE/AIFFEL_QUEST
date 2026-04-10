from __future__ import annotations

from pathlib import Path


PACKAGE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = PACKAGE_DIR.parent
DATA_DIR = PACKAGE_DIR / "data"
MODEL_DIR = PACKAGE_DIR / "model"


def package_dir() -> Path:
    return PACKAGE_DIR


def project_root() -> Path:
    return PROJECT_ROOT


def data_dir() -> Path:
    return DATA_DIR


def model_dir() -> Path:
    return MODEL_DIR
