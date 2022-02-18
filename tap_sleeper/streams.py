"""Stream type classes for tap-sleeper."""

from typing import Any, Dict, Iterable, Optional

from singer_sdk.streams import RESTStream

from tap_sleeper import schemas


class SleeperStream(RESTStream):
    url_base = "https://api.sleeper.app/v1"
    records_jsonpath = "$[*]"


class SportPlayersStream(SleeperStream):
    path = "/players/{sport}"
    schema = schemas.players
    name = "sport-players"
    records_jsonpath = "$.*"

    def get_url(self, context: Optional[dict]) -> str:
        url = self.url_base + self.path.format(sport=self.config["sport"])
        return url


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
        if "league_id" not in self.config.keys():
            raise ConfigIncompleteForSelectedStreamsError(
                """
                Must supply league_id in config to pull league-related streams.
                If you would not like to replicate league-related streams, remove
                them from your catalog.json (or meltano.yml).
                """
            )
        url = self.url_base + self.path.format(league_id=self.config["league_id"])
        return url

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        context = {"league_id": record["league_id"], "week": context["week"]}
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


class LeagueWeeklyStream(LeagueStream):
    def request_records(self, context: Optional[dict]) -> Iterable[dict]:
        """Request records from REST endpoint(s), returning response records.

        Args:
            context: Stream partition or context dictionary.

        Yields:
            An item for every record in the response.
        """
        decorated_request = self.request_decorator(self._request)

        # looping from beginning of season to current week
        for replication_week in range(1, context["week"] + 1):
            context["replication_week"] = replication_week
            prepared_request = self.prepare_request(context, next_page_token=None)
            resp = decorated_request(prepared_request, context)
            for row in self.parse_response(resp):
                yield row

    def post_process(self, row: dict, context: Optional[dict] = None) -> Optional[dict]:
        row["league_id"] = context["league_id"]
        row["week"] = context["replication_week"]
        return row

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        return context

    def get_url(self, context: Optional[dict]) -> str:
        url = self.url_base + self.path.format(
            league_id=context["league_id"], week=context.get("replication_week", 1)
        )
        return url


class LeagueMatchupsStream(LeagueWeeklyStream):
    path = "/league/{league_id}/matchups/{week}"
    schema = schemas.league_matchups
    name = "league-matchups"
    parent_stream_type = LeagueStream


class LeagueTransactionsStream(LeagueWeeklyStream):
    path = "/league/{league_id}/transactions/{week}"
    schema = schemas.league_transactions
    name = "league-transactions"
    parent_stream_type = LeagueStream


class LeaguePlayoffBracketStream(LeagueStream):
    path = "/league/{league_id}/{bracket_type}"
    schema = schemas.league_playoff_bracket
    parent_stream_type = LeagueStream

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        return context

    def post_process(self, row: dict, context: Optional[dict] = None) -> Optional[dict]:
        row["league_id"] = context["league_id"]
        return row


class LeaguePlayoffWinnersBracketStream(LeaguePlayoffBracketStream):
    name = "league-playoff-winners-bracket"

    def get_url(self, context: Optional[dict]) -> str:
        url = self.url_base + self.path.format(
            league_id=context["league_id"], bracket_type="winners_bracket"
        )
        return url

    def post_process(self, row: dict, context: Optional[dict] = None) -> Optional[dict]:
        row = super().post_process(row, context)
        row["bracket_type"] = "winners_bracket"
        return row


class LeaguePlayoffLosersBracketStream(LeaguePlayoffBracketStream):
    name = "league-playoff-losers-bracket"

    def get_url(self, context: Optional[dict]) -> str:
        url = self.url_base + self.path.format(
            league_id=context["league_id"], bracket_type="losers_bracket"
        )
        return url

    def post_process(self, row: dict, context: Optional[dict] = None) -> Optional[dict]:
        row = super().post_process(row, context)
        row["bracket_type"] = "losers_bracket"
        return row


class LeagueTradedPicksStream(LeagueStream):
    path = "/league/{league_id}/traded_picks"
    schema = schemas.league_traded_picks
    name = "league-traded-picks"
    parent_stream_type = LeagueStream

    def post_process(self, row: dict, context: Optional[dict] = None) -> Optional[dict]:
        row["league_id"] = context["league_id"]
        return row


class LeagueDraftsStream(LeagueStream):
    path = "/league/{league_id}/drafts"
    schema = schemas.league_drafts
    name = "league-drafts"
    parent_stream_type = LeagueStream

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        context = {"draft_id": record["draft_id"], "league_id": record["league_id"]}
        return context


class LeagueDraftPicksStream(LeagueDraftsStream):
    path = "/draft/{draft_id}/picks"
    schema = schemas.league_draft_picks
    name = "league-draft-picks"
    parent_stream_type = LeagueDraftsStream

    def get_url(self, context: Optional[dict]) -> str:
        url = self.url_base + self.path.format(
            league_id=context["league_id"], draft_id=context["draft_id"]
        )
        return url

    def post_process(self, row: dict, context: Optional[dict] = None) -> Optional[dict]:
        row["league_id"] = context["league_id"]
        return row


class LeagueDraftTradedPicksStream(LeagueDraftPicksStream):
    path = "/draft/{draft_id}/traded_picks"
    schema = schemas.league_traded_picks
    name = "league-traded-draft-picks"
    parent_stream_type = LeagueDraftsStream


class ConfigIncompleteForSelectedStreamsError(Exception):
    pass
