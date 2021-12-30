from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("player_id", th.StringType, description="The player's unique id"),
    th.Property(
        "count",
        th.IntegerType,
        description="The total number of add or drop events for that player within the lookback period",
    ),
).to_dict()
