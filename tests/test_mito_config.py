from mitosheet_helper_config.mito_config import MITO_ENTERPRISE_CONFIGURATION
from mitosheet_helper_config.mito_config_utils import MEC_VERSION


def test_mito_config_version_number():
    assert MITO_ENTERPRISE_CONFIGURATION[MEC_VERSION] == 1