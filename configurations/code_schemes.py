import json

from core_data_modules.data_models import CodeScheme


def _open_scheme(filename):
    with open(f"code_schemes/{filename}", "r") as f:
        firebase_map = json.load(f)
        return CodeScheme.from_firebase_map(firebase_map)


class CodeSchemes(object):
    VACCINATION_THOUGHTS = _open_scheme("vaccination_thoughts.json")
    OTHER_MESSAGES = _open_scheme("other_messages.json")

    ENGAGEMENT_POLL_CHATTING_APPS = _open_scheme("engagement_poll_chatting_apps.json")
    ENGAGEMENT_POLL_ACCESS_TO_INTERNET = _open_scheme("engagement_poll_access_to_internet.json")
    ENGAGEMENT_POLL_FACEBOOK_USAGE = _open_scheme("engagement_poll_facebook_usage.json")
    ENGAGEMENT_POLL_RADIO_STATIONS = _open_scheme("engagement_poll_radio_stations.json")
    ENGAGEMENT_POLL_OTHER_MESSAGES = _open_scheme("engagement_poll_other_messages.json")

    GENDER = _open_scheme("gender.json")
    AGE = _open_scheme("age.json")
    AGE_CATEGORY = _open_scheme("age_category.json")
    KENYA_CONSTITUENCY = _open_scheme("kenya_constituency.json")
    KENYA_COUNTY = _open_scheme("kenya_county.json")
    DISABLED = _open_scheme("disabled.json")

    WS_CORRECT_DATASET = _open_scheme("ws_correct_dataset.json")
