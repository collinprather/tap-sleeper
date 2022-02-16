"""Sleeper tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_sleeper.streams import (
    LeagueDraftPicksStream,
    LeagueDraftsStream,
    LeagueMatchupsStream,
    LeaguePlayoffLosersBracketStream,
    LeaguePlayoffWinnersBracketStream,
    LeagueRostersStream,
    LeagueStream,
    LeagueTradedPicksStream,
    LeagueTransactionsStream,
    LeagueUsersStream,
    SportPlayersStream,
    SportStateStream,
    TrendingDownPlayersStream,
    TrendingUpPlayersStream,
)

STREAM_TYPES = [
    LeagueDraftPicksStream,
    LeagueDraftsStream,
    LeagueMatchupsStream,
    LeaguePlayoffLosersBracketStream,
    LeaguePlayoffWinnersBracketStream,
    LeagueRostersStream,
    LeagueStream,
    LeagueTradedPicksStream,
    LeagueTransactionsStream,
    LeagueUsersStream,
    SportStateStream,
    TrendingDownPlayersStream,
    TrendingUpPlayersStream,
    SportPlayersStream,
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
            required=False,
            description="Unique identifier for the sleeper league",
        ),
        th.Property(
            "trending_players_lookback_hours",
            th.IntegerType,
            required=False,
            description="Total hours to lookback when requesting the current trending players",
        ),
        th.Property(
            "trending_players_limit",
            th.IntegerType,
            required=False,
            description="Total number of players to return when requesting the current trending players",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        streams = [stream_class(tap=self) for stream_class in STREAM_TYPES]
        return streams
