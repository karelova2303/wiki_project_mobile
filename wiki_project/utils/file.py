import wiki_project
from pathlib import Path

def abs_path_from_project(relative_path: str):
    return (
        Path(wiki_project.__file__)
        .parent.parent.joinpath(relative_path)
        .absolute()
        .__str__()
    )