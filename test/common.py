import os

import synapse.common as s_common

SYNAPSE_PACKAGE_YAML = s_common.genpath(os.path.dirname(__file__), "../s1-validin.yaml")
MOCK_RESPONSES_DIR = s_common.genpath(os.path.dirname(__file__), "mock")
BASE_URL = "https://pilot.validin.com/api/"


def get_mock_file_content(filename, mode="r"):
    file_path = os.path.join(MOCK_RESPONSES_DIR, filename)
    with open(file_path, mode) as f:
        return f.read()
