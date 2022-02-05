"""Tests standard tap features using the built-in SDK tests library."""

from singer_sdk.testing import get_standard_tap_tests

from tap_sleeper.tap import TapSleeper

SAMPLE_CONFIG = {"sport": "nfl", "league_id": "706681154622795776"} #"782559862231064576"}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(TapSleeper, config=SAMPLE_CONFIG)
    for test in tests:
        test()


# TODO: Create additional tests as appropriate for your tap.
test_standard_tap_tests()
