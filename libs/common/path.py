import os
from pathlib import Path
from typing import Union


def _root(
    file_path: Union[Path, str, None] = None, indicator="tests_root_point.txt"
) -> Path:
    file_path = file_path or os.path.dirname(os.path.realpath(__file__))
    try:
        return _root.cached_result
    except AttributeError:
        root_path = None
        for path_part in file_path.split(os.sep):
            root_path = os.path.join(root_path, path_part) if root_path else path_part + os.sep
            root_path = Path(root_path).resolve()
            if list(root_path.glob(indicator)):
                _root.cached_result = root_path
                return root_path
        raise FileNotFoundError(indicator)


def get_full_path_for(file_path: str, as_str=True) -> Union[Path, str]:
    full_path = os.path.join(_root(), file_path.lstrip("/"))
    return str(full_path) if as_str else Path(full_path)
