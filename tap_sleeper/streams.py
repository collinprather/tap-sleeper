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


class SportStateStream(SleeperStream):
    path = "/state/{sport}"
    schema = schemas.sport_state
    name = "sport-state"

    def get_url(self, context: Optional[dict]) -> str:
        url = self.url_base + self.path.format(sport=self.config["sport"])
        return url

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        context = {"week": record["leg"]}
        return context


class LeagueStream(SleeperStream):
    path = "/league/{league_id}"
    schema = schemas.league
    name = "league"
    parent_stream_type = SportStateStream

    def get_url(self, context: Optional[dict]) -> str:
        url = self.url_base + self.path.format(league_id=self.config["league_id"])
        return url

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        context = {"league_id": record["league_id"]}
        return context


class LeagueRostersStream(LeagueStream):
    path = "/league/{league_id}/rosters"
    schema = schemas.league_rosters
    name = "league-rosters"
    parent_stream_type = LeagueStream


class LeagueUsersStream(LeagueStream):
    path = "/league/{league_id}/users"
    schema = schemas.league_users
    name = "league-users"
    parent_stream_type = LeagueStream


class LeagueMatchupsStream(LeagueStream):
    path = "/league/{league_id}/matchup/{week}"
    schema = schemas.league_matchups
    name = "league-matchups"
    parent_stream_type = LeagueStream


class LeaguePlayoffBracketStream(LeagueStream):
    path = "/league/{league_id}/{bracket_type}"
    # schema = schemas.league_matchups
    parent_stream_type = LeagueStream


class LeaguePlayoffWinnersBracketStream(LeaguePlayoffBracketStream):
    name = "league-playoff-winners-bracket"

    def get_url(self, context: Optional[dict]) -> str:
        url = self.url_base + self.path.format(bracket_type="winners_bracket")
        return url


class LeaguePlayoffLosersBracketStream(LeaguePlayoffBracketStream):
    name = "league-playoff-losers-bracket"

    def get_url(self, context: Optional[dict]) -> str:
        url = self.url_base + self.path.format(bracket_type="losers_bracket")
        return url


class LeagueTransactionsStream(LeagueStream):
    path = "/league/{league_id}/transactions/{round}"
    # schema = schemas.league_transactions
    name = "league-transactions"
    parent_stream_type = LeagueStream


class LeagueTradedPicksStream(LeagueStream):
    path = "/league/{league_id}/traded_picks"
    # schema = schemas.league_transactions
    name = "league-traded-picks"
    parent_stream_type = LeagueStream


class LeagueDraftsStream(LeagueStream):
    path = "/league/{league_id}/drafts"
    # schema = schemas.league_drafts
    name = "league-drafts"
    parent_stream_type = LeagueStream

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        context = {"draft_id": record["draft_id"]}
        return context


class LeagueDraftPicksStream(LeagueDraftsStream):
    path = "/draft/{draft_id}/picks"
    # schema = schemas.league_draft_picks
    name = "league-draft-picks"
    parent_stream_type = LeagueDraftsStream


class LeagueTradedDraftPicksStream(LeagueDraftsStream):
    path = "/draft/{draft_id}/traded_picks"
    # schema = schemas.league_traded_draft_picks
    name = "league-traded-draft-picks"
    parent_stream_type = LeagueDraftsStream


class SportPlayersStream(SleeperStream):
    path = "/players/{sport}"
    # schema = schemas.sport_state
    name = "sport-players"

    def get_url(self, context: Optional[dict]) -> str:
        url = self.url_base + self.path.format(sport=self.config["sport"])
        return url
