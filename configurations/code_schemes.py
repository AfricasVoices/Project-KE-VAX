import json

from core_data_modules.data_models import CodeScheme


def _open_scheme(filename):
    with open(f"code_schemes/{filename}", "r") as f:
        firebase_map = json.load(f)
        return CodeScheme.from_firebase_map(firebase_map)


class CodeSchemes(object):
    VACCINATION_THOUGHTS = _open_scheme("vaccination_thoughts.json")

    WS_CORRECT_DATASET = _open_scheme("ws_correct_dataset.json")
