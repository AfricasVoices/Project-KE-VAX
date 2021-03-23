from functools import partial

from core_data_modules.cleaners import swahili
from core_data_modules.data_models import CodeScheme
from core_data_modules.traced_data.util.fold_traced_data import FoldStrategies

from configurations.code_schemes import CodeSchemes
from src.lib.configuration_objects import CodingConfiguration, CodingModes, CodingPlan


def get_rqa_coding_plans(pipeline_name):
    return [
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


def get_demog_coding_plans(pipeline_name):
    return []


def get_ws_correct_dataset_scheme(pipeline_name):
    return CodeSchemes.WS_CORRECT_DATASET


def get_follow_up_coding_plans(pipeline_name):
    return []
