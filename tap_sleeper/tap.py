"""Sleeper tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_sleeper.streams import (
    SleeperStream,
    UsersStream,
    GroupsStream,
)

# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    UsersStream,
    GroupsStream,
]


class TapSleeper(Tap):
    """Sleeper tap class."""

    name = "tap-sleeper"
    config_jsonschema = th.PropertiesList(
        th.Property(
            "league_id",
            th.StrinType,
            requred=True,
            description="Unique identifier for the sleeper league"
        ),
        # grab all the users in the league, then pull all players
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
