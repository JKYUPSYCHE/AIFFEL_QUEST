from .paths import data_dir, model_dir, package_dir, project_root

__all__ = [
    "AutoIntModel",
    "AutoIntMLPModel",
    "configure_tensorflow",
    "data_dir",
    "model_dir",
    "package_dir",
    "predict_model",
    "project_root",
]


def __getattr__(name):
    if name in {"AutoIntModel", "predict_model"}:
        from .autoint import AutoIntModel, predict_model

        exports = {
            "AutoIntModel": AutoIntModel,
            "predict_model": predict_model,
        }
        return exports[name]

    if name == "AutoIntMLPModel":
        from .autointmlp import AutoIntMLPModel

        return AutoIntMLPModel

    if name == "configure_tensorflow":
        from .tf_device import configure_tensorflow

        return configure_tensorflow

    raise AttributeError(f"module 'autoint' has no attribute {name!r}")
