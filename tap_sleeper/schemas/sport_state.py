from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("week", th.IntegerType),
    th.Property("season_type", th.StringType, description="pre, post, regular"),
    th.Property("season_start_date", th.StringType, description="regular season start"),
    th.Property("season", th.StringType, description="leage season"),
    th.Property("previous_season", th.StringType),
    th.Property(
        "league_season", th.StringType, description="active season for the league"
    ),
    th.Property("league_create_season", th.StringType, description="flips in December"),
    th.Property("leg", th.IntegerType),
    th.Property(
        "display_week",
        th.IntegerType,
        description="Which week to display in UI, can be different than week",
    ),
).to_dict()
