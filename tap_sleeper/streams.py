"""Stream type classes for tap-sleeper."""

from typing import Any, Dict, Optional

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


class TrendingUpPlayersStream(TrendingPlayersStream):
    name = "trending-up-players"

    def get_url(self, context: Optional[dict]) -> str:
        url = self.url_base + self.path.format(sport=self.config["sport"], type="add")
        return url


class TrendingDownPlayersStream(TrendingPlayersStream):
    name = "trending-down-players"

    def get_url(self, context: Optional[dict]) -> str:
        url = self.url_base + self.path.format(sport=self.config["sport"], type="drop")
        return url


class LeagueStream(SleeperStream):
    pass
