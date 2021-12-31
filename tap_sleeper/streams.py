"""Stream type classes for tap-sleeper."""

import requests
from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream

from tap_sleeper import schemas


class SleeperStream(RESTStream):

    url_base = "https://api.sleeper.app/v1"
    records_jsonpath = "$[*]"


class TrendingPlayersStream(SleeperStream):
    path = "/players/{sport}/trending/{type}"
    schema = schemas.trending_players

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        params = {
            "lookback_hours": self.config.get("trending_players_lookback_hours", 24),
            "limit": self.config.get("trending_players_limit", 25),
        }
        return params


class TrendingPlayersUpStream(TrendingPlayersStream):
    name = "trending-players-up"

    def get_url(self, context: Optional[dict]) -> str:
        url = self.url_base + self.path.format(sport=self.config["sport"], type="add")
        return url


class TrendingPlayersDownStream(TrendingPlayersStream):
    name = "trending-players-down"

    def get_url(self, context: Optional[dict]) -> str:
        url = self.url_base + self.path.format(sport=self.config["sport"], type="drop")
        return url


class LeagueStream(SleeperStream):
    pass
