from typing import List

from blue_options.terminal import show_usage, xtra


def help_clone(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@huggingface",
            "clone",
            "<repo_name>",
        ],
        "clone huggingface/repo_name.",
        mono=mono,
    )


def help_install(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@huggingface",
            "install",
        ],
        "install huggingface.",
        mono=mono,
    )


def help_get_model_path(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@huggingface",
            "get_model_path",
            "<repo_name>",
            "[<model-name>]",
            "[model=object/*saved]",
        ],
        "return model_path for saved/object model repo_name/<model-name>.",
        mono=mono,
    )


def help_save(
    tokens: List[str],
    mono: bool,
) -> str:
    return show_usage(
        [
            "@huggingface",
            "save",
            "<repo-name>",
            "<model-name>",
            "<object-name>",
            "[force]",
        ],
        "[force] save <object-name> as huggingface/<repo-name>/<model-name>.",
        mono=mono,
    )


help_functions = {
    "clone": help_clone,
    "install": help_install,
    "get_model_path": help_get_model_path,
    "save": help_save,
}
