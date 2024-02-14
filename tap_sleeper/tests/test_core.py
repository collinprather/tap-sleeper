"""Tests standard tap features using the built-in SDK tests library."""

import os

from singer_sdk.testing import SuiteConfig, get_tap_test_class

from tap_sleeper.tap import TapSleeper

SAMPLE_CONFIG = {
    "sport": "nfl",
    "league_id": os.environ.get("SAMPLE_CONFIG_LEAGUE_ID", ""),
}

# Run standard built-in tap tests from the SDK:
TestTapSleeper = get_tap_test_class(
    tap_class=TapSleeper,
    config=SAMPLE_CONFIG,
    suite_config=SuiteConfig(max_records_limit=10, ignore_no_records=True),
)


# Run standard built-in tap tests from the SDK:
# def test_standard_tap_tests():
#     """Run standard tap tests from the SDK."""
#     tests = get_standard_tap_tests(TapSleeper, config=SAMPLE_CONFIG)
#     for test in tests:
#         test()
