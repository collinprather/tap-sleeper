from singer_sdk import typing as th

league = th.PropertiesList(
    th.Property("league_id", th.StringType),
    th.Property("previous_draft_id", th.StringType),
    th.Property("draft_id", th.StringType),
    th.Property("avatar", th.StringType),
    th.Property("name", th.StringType),
    th.Property("total_rosters", th.IntegerType),
    th.Property("status", th.StringType),
    th.Property("sport", th.StringType),
    th.Property("season", th.StringType),
    th.Property("season_type", th.StringType),
    th.Property("roster_positions", th.ArrayType(th.StringType)),
    th.Property("settings", th.ObjectType()),
    th.Property("scoring_settings", th.ObjectType()),
).to_dict()

league_rosters = th.PropertiesList(
    th.Property("league_id", th.StringType),
    th.Property("owner_id", th.StringType),
    th.Property("roster_id", th.IntegerType),
    th.Property("players", th.ArrayType(th.StringType)),
    th.Property("starters", th.ArrayType(th.StringType)),
    th.Property("reserve", th.ArrayType(th.StringType)),
    th.Property(
        "settings",
        th.ObjectType(
            th.Property("wins", th.IntegerType),
            th.Property("waiver_position", th.IntegerType),
            th.Property("waiver_budget_used", th.IntegerType),
            th.Property("total_moves", th.IntegerType),
            th.Property("ties", th.IntegerType),
            th.Property("losses", th.IntegerType),
            th.Property("fpts_decimal", th.IntegerType),
            th.Property("fpts_against_decimal", th.IntegerType),
            th.Property("fpts_against", th.IntegerType),
            th.Property("fpts", th.IntegerType),
        ),
    ),
).to_dict()

league_users = th.PropertiesList(
    th.Property("user_id", th.StringType),
    th.Property("username", th.StringType),
    th.Property("display_name", th.StringType),
    th.Property("avatar", th.StringType),
    th.Property("is_owner", th.BooleanType),
    th.Property("metadata", th.ObjectType(th.Property("team_name", th.StringType))),
).to_dict()

league_matchups = th.PropertiesList(
    th.Property("starters", th.ArrayType(th.StringType)),
    th.Property("players", th.ArrayType(th.StringType)),
    th.Property("roster_id", th.IntegerType),
    th.Property("matchup_id", th.IntegerType),
    th.Property("points", th.NumberType),
    th.Property("custom_points", th.NumberType),
).to_dict()
