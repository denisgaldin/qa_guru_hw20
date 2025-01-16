from pathlib import Path

import tests


def abs_path_from_project(relative_path: str):
    return Path(tests.__file__).parent.parent.joinpath(relative_path).absolute().__str__()