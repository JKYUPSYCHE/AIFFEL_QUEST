from __future__ import annotations

from typing import List

import tensorflow as tf


def configure_tensorflow(*, log: bool = True) -> List[tf.config.PhysicalDevice]:
    """Enable GPU (Metal on macOS) when available and keep CPU fallback safe."""
    try:
        gpus = tf.config.list_physical_devices("GPU")
        if gpus:
            for gpu in gpus:
                try:
                    tf.config.experimental.set_memory_growth(gpu, True)
                except Exception:
                    # Some drivers do not support memory growth; ignore and continue.
                    pass
            if log:
                print(f"[tf] GPU devices: {gpus}")
        else:
            if log:
                print("[tf] No GPU found; using CPU.")
        return gpus
    except Exception as exc:
        if log:
            print(f"[tf] GPU setup skipped: {exc}")
        return []
