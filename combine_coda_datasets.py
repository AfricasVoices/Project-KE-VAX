import argparse
import glob
import json

from core_data_modules.data_models import Message


def latest_labels(labels):
    out = []
    seen_scheme_ids = set()
    for l in labels:
        if l.code_id == "SPECIAL-MANUALLY_UNCODED":
            continue
        if l.scheme_id not in seen_scheme_ids:
            out.append(l)
            seen_scheme_ids.add(l.scheme_id)
    return out


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Combines the various Coda demographic datasets from the previous "
                                                 "pool projects and combines them into one dataset.")

    parser.add_argument("input_dir", metavar="input-dir",
                        help="A directory containing the Coda messages files to combine. Each file should be in the "
                             "format {ProjectName}_{demog}. This script supports datasets from COVID19, WorldVision, "
                             "OXFAM-WASH, and UNICEF-COVID19_KE as of March 2021")
    parser.add_argument("output_dir", metavar="output-dir",
                        help="A directory to write the combined messages files to. Files will be written in the "
                             "format Kenya_Pool_{demog}")

    args = parser.parse_args()
    input_dir = args.input_dir
    output_dir = args.output_dir

    for demog in ["gender", "age", "location", "disabled"]:
        print()
        print(demog)
        input_datasets = glob.glob(f"{input_dir}/*_{demog}.json")
        output_messages = dict()  # of message id -> message
        conflicting_messages = set()  # of message id. This will contain messages that appear in multiple datasets and have different codes
        for path in input_datasets:
            with open(path) as f:
                messages = [Message.from_firebase_map(m) for m in json.load(f)]
                print(f"Loaded {len(messages)} messages from {path}")
                for m in messages:
                    if m.message_id not in output_messages:
                        output_messages[m.message_id] = m
                    else:
                        message_label_ids = {x.code_id for x in latest_labels(m.labels)}
                        existing_message_label_ids = {x.code_id for x in latest_labels(output_messages[m.message_id].labels)}
                        if message_label_ids != existing_message_label_ids:
                            print("Differing labels", message_label_ids, existing_message_label_ids, m.text)
                            conflicting_messages.add(m.message_id)

                    for l in m.labels:
                        # Rewrite scheme and code ids that represent the same concept but were different across
                        # the input projects.

                        # Gender
                        if l.scheme_id == "Scheme-2bba4420":
                            l.scheme_id = "Scheme-12cb6f95"

                        # Age
                        if l.scheme_id == "Scheme-016f646a":
                            l.scheme_id = "Scheme-4189e74c"

                        # Constituency
                        if l.scheme_id == "Scheme-a992ef8f":
                            l.scheme_id = "Scheme-4c5b955d"

                        # County
                        if l.scheme_id == "Scheme-81b34b9d":
                            l.scheme_id = "Scheme-af6c3ef0"

                        # WorldVision WS remaps
                        if l.scheme_id == "Scheme-ffff1797":
                            if l.code_id == "code-9bd0f2b1":  # s01e01
                                l.code_id = "code-eb71f375"
                            if l.code_id == "code-f0c22231":  # s01e02
                                l.code_id = "code-21b6b981"
                            if l.code_id == "code-c6d30e11":  # s01e03
                                l.code_id = "code-a0ec4383"

                        # Oxfam WS remaps
                        if l.scheme_id == "Scheme-ffff43a6":
                            if l.code_id == "code-be80a219":  # s01e01
                                l.code_id = "code-aec91680"
                            if l.code_id == "code-501501c6":  # s01e02
                                l.code_id = "code-d6d8acd5"
                            if l.code_id == "code-33462fdd":  # s01e03
                                l.code_id = "code-7934d45b"

                        # WS - Correct Dataset
                        if l.scheme_id.startswith("Scheme-ffff"):
                            l.scheme_id = "Scheme-fffffbfc"

                        # WS age
                        if l.code_id in {"code-70ac05ab"}:
                            l.code_id = "code-c473f7bb"
                        # WS location
                        if l.code_id in {"code-dda6e4b4"}:
                            l.code_id = "code-02d4450d"
                        # WS gender
                        if l.code_id in {"code-6774cedd"}:
                            l.code_id = "code-80edd5c3"

        with open(f"{output_dir}/Kenya_Pool_{demog}.json", "w") as f:
            messages_to_write = output_messages.values()
            for m in messages_to_write:
                # If the labels that were assigned conflict between different datasets, require these to be labelled
                # again. To speed up the process, keep one of the sets of labels that was applied but just set
                # checked to False.
                if m.message_id in conflicting_messages:
                    for l in latest_labels(m.labels):
                        l.checked = False

            json.dump([m.to_firebase_map() for m in messages_to_write], f)
