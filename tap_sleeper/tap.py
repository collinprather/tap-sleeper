"""Sleeper tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_sleeper.streams import (
    LeagueMatchupsStream,
    LeaguePlayoffWinnersBracketStream,
    LeaguePlayoffLosersBracketStream,
    LeagueRostersStream,
    LeagueStream,
    LeagueTransactionsStream,
    LeagueTradedPicksStream,
    LeagueUsersStream,
    SportStateStream,
    TrendingDownPlayersStream,
    TrendingUpPlayersStream,
)

STREAM_TYPES = [
    LeagueMatchupsStream,
    LeaguePlayoffWinnersBracketStream,
    LeaguePlayoffLosersBracketStream,
    LeagueRostersStream,
    LeagueStream,
    LeagueTransactionsStream,
    LeagueTradedPicksStream,
    LeagueUsersStream,
    SportStateStream,
    TrendingDownPlayersStream,
    TrendingUpPlayersStream,
]


class TapSleeper(Tap):
    """Sleeper tap class."""

    name = "tap-sleeper"
    config_jsonschema = th.PropertiesList(
        th.Property(
            "sport",
            th.StringType,
            required=True,
            default="nfl",
            description="Professional sport league, ie nfl, nba, etc",
        ),
        th.Property(
            "league_id",
            th.StringType,
            required=True,
            description="Unique identifier for the sleeper league",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        streams = [stream_class(tap=self) for stream_class in STREAM_TYPES]
        return streams
