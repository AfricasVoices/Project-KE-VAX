from functools import partial

from core_data_modules.cleaners import swahili, Codes
from core_data_modules.data_models import CodeScheme
from core_data_modules.traced_data.util.fold_traced_data import FoldStrategies

from configurations import code_imputation_functions
from configurations.code_schemes import CodeSchemes
from src.lib.configuration_objects import CodingConfiguration, CodingModes, CodingPlan


def clean_age_with_range_filter(text):
    """
    Cleans age from the given `text`, setting to NC if the cleaned age is not in the range 10 <= age < 100.
    """
    age = swahili.DemographicCleaner.clean_age(text)
    if type(age) == int and 10 <= age < 100:
        return str(age)
        # TODO: Once the cleaners are updated to not return Codes.NOT_CODED, this should be updated to still return
        #       NC in the case where age is an int but is out of range
    else:
        return Codes.NOT_CODED



KE_VAX_RQA_PLANS = [
    CodingPlan(
        raw_field="vaccination_thoughts_raw",
        dataset_name="vaccination_thoughts",
        time_field="sent_on",
        run_id_field="vaccination_thoughts_run_id",
        coda_filename="KE_VAX_vaccination_thoughts.json",
        icr_filename="vaccination_thoughts.csv",
        coding_configurations=[
            CodingConfiguration(
                coding_mode=CodingModes.MULTIPLE,
                code_scheme=CodeSchemes.VACCINATION_THOUGHTS,
                coded_field="vaccination_thoughts_coded",
                analysis_file_key="vaccination_thoughts",
                fold_strategy=partial(FoldStrategies.list_of_labels, CodeSchemes.VACCINATION_THOUGHTS)
            )
        ],
        raw_field_fold_strategy=FoldStrategies.concatenate
    ),

    CodingPlan(
        raw_field="other_messages_raw",
        dataset_name="other_messages",
        time_field="sent_on",
        run_id_field="other_messages_run_id",
        coda_filename="KE_VAX_other_messages.json",
        icr_filename="other_messages.csv",
        coding_configurations=[
            CodingConfiguration(
                coding_mode=CodingModes.MULTIPLE,
                code_scheme=CodeSchemes.OTHER_MESSAGES,
                coded_field="other_messages_coded",
                analysis_file_key="other_messages",
                fold_strategy=partial(FoldStrategies.list_of_labels, CodeSchemes.OTHER_MESSAGES)
            )
        ],
        raw_field_fold_strategy=FoldStrategies.concatenate
    )
]

KE_ENGAGEMENT_RQA_PLANS = [
    CodingPlan(
        raw_field="chatting_apps_raw",
        dataset_name="chatting_apps",
        time_field="sent_on",
        run_id_field="chatting_apps_run_id",
        coda_filename="KE_Engagement_poll_chatting_apps.json",
        icr_filename="chatting_apps.csv",
        coding_configurations=[
            CodingConfiguration(
                coding_mode=CodingModes.MULTIPLE,
                code_scheme=CodeSchemes.ENGAGEMENT_POLL_CHATTING_APPS,
                coded_field="chatting_apps_coded",
                analysis_file_key="chatting_apps",
                fold_strategy=partial(FoldStrategies.list_of_labels, CodeSchemes.ENGAGEMENT_POLL_CHATTING_APPS)
            )
        ],
        raw_field_fold_strategy=FoldStrategies.concatenate,
        ws_code = CodeSchemes.WS_CORRECT_DATASET.get_code_with_match_value("KE_Engagement_poll_chatting_apps"),
    ),

    CodingPlan(
        raw_field="access_to_internet_raw",
        dataset_name="access_to_internet",
        time_field="sent_on",
        run_id_field="access_to_internet_run_id",
        coda_filename="KE_Engagement_poll_access_to_internet.json",
        icr_filename="access_to_internet.csv",
        coding_configurations=[
            CodingConfiguration(
                coding_mode=CodingModes.MULTIPLE,
                code_scheme=CodeSchemes.ENGAGEMENT_POLL_ACCESS_TO_INTERNET,
                coded_field="access_to_internet_coded",
                analysis_file_key="access_to_internet",
                fold_strategy=partial(FoldStrategies.list_of_labels, CodeSchemes.ENGAGEMENT_POLL_ACCESS_TO_INTERNET)
            )
        ],
        raw_field_fold_strategy=FoldStrategies.concatenate,
        ws_code = CodeSchemes.WS_CORRECT_DATASET.get_code_with_match_value("KE_Engagement_poll_access_to_internet"),
    ),

    CodingPlan(
        raw_field="facebook_usage_raw",
        dataset_name="facebook_usage",
        time_field="sent_on",
        run_id_field="facebook_usage_run_id",
        coda_filename="KE_Engagement_poll_facebook_usage.json",
        icr_filename="facebook_usage.csv",
        coding_configurations=[
            CodingConfiguration(
                coding_mode=CodingModes.MULTIPLE,
                code_scheme=CodeSchemes.ENGAGEMENT_POLL_FACEBOOK_USAGE,
                coded_field="facebook_usage_coded",
                analysis_file_key="facebook_usage",
                fold_strategy=partial(FoldStrategies.list_of_labels, CodeSchemes.ENGAGEMENT_POLL_FACEBOOK_USAGE)
            )
        ],
        raw_field_fold_strategy=FoldStrategies.concatenate,
        ws_code = CodeSchemes.WS_CORRECT_DATASET.get_code_with_match_value("KE_Engagement_poll_facebook_usage"),
    ),

    CodingPlan(
        raw_field="radio_stations_raw",
        dataset_name="radio_stations",
        time_field="sent_on",
        run_id_field="radio_stations_run_id",
        coda_filename="KE_Engagement_poll_radio_stations.json",
        icr_filename="radio_stations.csv",
        coding_configurations=[
            CodingConfiguration(
                coding_mode=CodingModes.MULTIPLE,
                code_scheme=CodeSchemes.ENGAGEMENT_POLL_RADIO_STATIONS,
                coded_field="radio_stations_coded",
                analysis_file_key="radio_stations",
                fold_strategy=partial(FoldStrategies.list_of_labels, CodeSchemes.ENGAGEMENT_POLL_RADIO_STATIONS)
            )
        ],
        raw_field_fold_strategy=FoldStrategies.concatenate,
        ws_code = CodeSchemes.WS_CORRECT_DATASET.get_code_with_match_value("KE_Engagement_poll_radio_stations"),
    ),

    CodingPlan(
        raw_field="other_messages_raw",
        dataset_name="other_messages",
        time_field="sent_on",
        run_id_field="other_messages_run_id",
        coda_filename="KE_Engagement_poll_other_messages.json",
        icr_filename="engagement_poll_other_messages.csv",
        coding_configurations=[
            CodingConfiguration(
                coding_mode=CodingModes.MULTIPLE,
                code_scheme=CodeSchemes.ENGAGEMENT_POLL_OTHER_MESSAGES,
                coded_field="other_messages_coded",
                analysis_file_key="other_messages",
                fold_strategy=partial(FoldStrategies.list_of_labels, CodeSchemes.ENGAGEMENT_POLL_OTHER_MESSAGES)
            )
        ],
        raw_field_fold_strategy=FoldStrategies.concatenate,
        ws_code = CodeSchemes.WS_CORRECT_DATASET.get_code_with_match_value("KE_Engagement_poll_other_messages"),
    ),

]


def get_rqa_coding_plans(pipeline_name):
    if pipeline_name == "KE-VAX":
        return KE_VAX_RQA_PLANS
    else:
        assert pipeline_name == "KE-Engagement-Poll"
        return KE_ENGAGEMENT_RQA_PLANS


def get_demog_coding_plans(pipeline_name):
    return [
        CodingPlan(
            dataset_name="gender",
            raw_field="gender_raw",
            time_field="gender_time",
            coda_filename="Kenya_Pool_gender.json",
            coding_configurations=[
                CodingConfiguration(
                    coding_mode=CodingModes.SINGLE,
                    code_scheme=CodeSchemes.GENDER,
                    cleaner=swahili.DemographicCleaner.clean_gender,
                    coded_field="gender_coded",
                    analysis_file_key="gender",
                    fold_strategy=FoldStrategies.assert_label_ids_equal
                )
            ],
            ws_code=CodeSchemes.WS_CORRECT_DATASET.get_code_with_match_value("gender"),
            raw_field_fold_strategy=FoldStrategies.assert_equal
        ),

        CodingPlan(dataset_name="age",
                   raw_field="age_raw",
                   time_field="age_time",
                   coda_filename="Kenya_Pool_age.json",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.AGE,
                           cleaner=clean_age_with_range_filter,
                           coded_field="age_coded",
                           analysis_file_key="age",
                           include_in_theme_distribution=False,
                           fold_strategy=FoldStrategies.assert_label_ids_equal
                       ),
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.AGE_CATEGORY,
                           coded_field="age_category_coded",
                           analysis_file_key="age_category",
                           fold_strategy=FoldStrategies.assert_label_ids_equal
                       )
                   ],
                   code_imputation_function=code_imputation_functions.impute_age_category,
                   ws_code=CodeSchemes.WS_CORRECT_DATASET.get_code_with_match_value("age"),
                   raw_field_fold_strategy=FoldStrategies.assert_equal),

        CodingPlan(dataset_name="location",
                   raw_field="location_raw",
                   time_field="location_time",
                   coda_filename="Kenya_Pool_location.json",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.KENYA_COUNTY,
                           coded_field="county_coded",
                           analysis_file_key="county",
                           fold_strategy=FoldStrategies.assert_label_ids_equal
                       ),
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.KENYA_CONSTITUENCY,
                           coded_field="constituency_coded",
                           analysis_file_key="constituency",
                           fold_strategy=FoldStrategies.assert_label_ids_equal
                       )
                   ],
                   code_imputation_function=code_imputation_functions.impute_kenya_location_codes,
                   ws_code=CodeSchemes.WS_CORRECT_DATASET.get_code_with_match_value("location"),
                   raw_field_fold_strategy=FoldStrategies.assert_equal),

        CodingPlan(dataset_name="disabled",
                   raw_field="disabled_raw",
                   time_field="disabled_time",
                   coda_filename="Kenya_Pool_disabled.json",
                   coding_configurations=[
                       CodingConfiguration(
                           coding_mode=CodingModes.SINGLE,
                           code_scheme=CodeSchemes.DISABLED,
                           coded_field="disabled_coded",
                           analysis_file_key="disabled",
                           fold_strategy=FoldStrategies.assert_label_ids_equal
                       )
                   ],
                   ws_code=CodeSchemes.WS_CORRECT_DATASET.get_code_with_match_value("disabled"),
                   raw_field_fold_strategy=FoldStrategies.assert_equal)
    ]


def get_ws_correct_dataset_scheme(pipeline_name):
    return CodeSchemes.WS_CORRECT_DATASET


def get_follow_up_coding_plans(pipeline_name):
    return []
