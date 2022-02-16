from singer_sdk import typing as th

league = th.PropertiesList(
    th.Property("league_id", th.StringType),
    th.Property("previous_league_id", th.StringType),
    th.Property("previous_draft_id", th.StringType),
    th.Property("draft_id", th.StringType),
    th.Property("loser_bracket_id", th.IntegerType),
    th.Property("company_id", th.StringType),
    th.Property("group_id", th.StringType),
    th.Property("bracket_id", th.IntegerType),
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
    th.Property("metadata", th.ObjectType()),
    th.Property("shard", th.IntegerType),
    th.Property("last_message_id", th.StringType),
    th.Property("last_author_id", th.StringType),
    th.Property("last_author_display_name", th.StringType),
    th.Property("last_author_avatar", th.StringType),
    th.Property("last_read_id", th.StringType),
    th.Property("last_pinned_message_id", th.StringType),
    th.Property("last_message_time", th.IntegerType),
    th.Property("last_message_text_map", th.ObjectType()),
    th.Property("last_author_is_bot", th.BooleanType),
).to_dict()

league_rosters = th.PropertiesList(
    th.Property("league_id", th.StringType),
    th.Property("owner_id", th.StringType),
    th.Property("roster_id", th.IntegerType),
    th.Property("week", th.IntegerType),
    th.Property("players", th.ArrayType(th.StringType)),
    th.Property("starters", th.ArrayType(th.StringType)),
    th.Property("reserve", th.ArrayType(th.StringType)),
    th.Property("taxi", th.ArrayType(th.StringType)),
    th.Property("co_owners", th.ArrayType(th.StringType)),
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
    th.Property("metadata", th.ObjectType()),
).to_dict()

league_users = th.PropertiesList(
    th.Property("league_id", th.StringType),
    th.Property("user_id", th.StringType),
    th.Property("username", th.StringType),
    th.Property("display_name", th.StringType),
    th.Property("avatar", th.StringType),
    th.Property("is_owner", th.BooleanType),
    th.Property("is_bot", th.BooleanType),
    th.Property("metadata", th.ObjectType()),
    th.Property("settings", th.ObjectType()),
).to_dict()

league_matchups = th.PropertiesList(
    th.Property("league_id", th.IntegerType),
    th.Property("roster_id", th.IntegerType),
    th.Property("matchup_id", th.IntegerType),
    th.Property("week", th.IntegerType),
    th.Property("starters", th.ArrayType(th.StringType)),
    th.Property("players", th.ArrayType(th.StringType)),
    th.Property("points", th.NumberType),
    th.Property("starters_points", th.NumberType),
    th.Property("players_points", th.NumberType),
    th.Property("custom_points", th.NumberType),
).to_dict()

league_transactions = th.PropertiesList(
    th.Property("league_id", th.StringType),
    th.Property("transaction_id", th.StringType),
    th.Property("type", th.StringType, description="trade, free_agent, waiver, etc"),
    th.Property("status", th.StringType),
    th.Property("status_updated", th.IntegerType),
    th.Property("roster_ids", th.ArrayType(th.IntegerType)),
    th.Property("consenter_ids", th.ArrayType(th.IntegerType)),
    th.Property("leg", th.IntegerType, description="in football, this is the week"),
    th.Property("adds", th.ObjectType()),
    th.Property("drops", th.ObjectType()),
    th.Property(
        "settings",
        th.ObjectType(
            th.Property("seq", th.IntegerType), th.Property("priority", th.IntegerType)
        ),
    ),
    th.Property(
        "waiver_budget",
        th.ArrayType(
            th.ObjectType(
                th.Property(
                    "sender", th.IntegerType, description="roster_id of sender"
                ),
                th.Property(
                    "receiver", th.IntegerType, description="roster_id of receiver"
                ),
                th.Property("amount", th.IntegerType),
            ),
        ),
    ),
    th.Property(
        "draft_picks",
        th.ArrayType(
            th.ObjectType(
                th.Property("season", th.StringType),
                th.Property("round", th.IntegerType),
                th.Property("roster_id", th.IntegerType),
                th.Property("owner_id", th.IntegerType),
                th.Property("previous_owner_id", th.IntegerType),
            ),
        ),
    ),
    th.Property("creator", th.StringType),
    th.Property("created", th.IntegerType),
    th.Property("metadata", th.ObjectType()),
).to_dict()

league_playoff_bracket = th.PropertiesList(
    th.Property("league_id", th.StringType),
    th.Property("type", th.StringType, description="winner's or loser's bracket"),
    th.Property(
        "r",
        th.IntegerType,
        description="The round for this matchup, 1st, 2nd, 3rd round, etc.",
    ),
    th.Property(
        "m",
        th.IntegerType,
        description="The match id of the matchup, unique for all matchups within a bracket.",
    ),
    th.Property(
        "t1",
        th.IntegerType,
        description="The roster_id of a team in this matchup OR {w: 1} which means the winner of match id 1",
    ),
    th.Property(
        "t2",
        th.IntegerType,
        description="The roster_id of the other team in this matchup OR {l: 1} which means the loser of match id 1",
    ),
    th.Property(
        "w",
        th.IntegerType,
        description="The roster_id of the winning team, if the match has been played.",
    ),
    th.Property(
        "l",
        th.IntegerType,
        description="The roster_id of the losing team, if the match has been played.",
    ),
    th.Property(
        "t1_from",
        th.ObjectType(),
        description="Where t1 comes from, either winner or loser of the match id, necessary to show bracket progression.",
    ),
    th.Property(
        "t2_from",
        th.ObjectType(),
        description="Where t2 comes from, either winner or loser of the match id, necessary to show bracket progression.",
    ),
).to_dict()

league_traded_picks = th.PropertiesList(
    th.Property("league_id", th.StringType),
    th.Property("roster_id", th.IntegerType, description="roster_id of ORIGINAL owner"),
    th.Property("owner_id", th.IntegerType, description="roster_id of current owner"),
    th.Property(
        "previous_owner_id",
        th.IntegerType,
        description="roster_id of the previous owner",
    ),
    th.Property("round", th.IntegerType, description="which round the pick is"),
    th.Property("season", th.StringType, description="which season the pick is for"),
).to_dict()

league_drafts = th.PropertiesList(
    th.Property("league_id", th.StringType),
    th.Property("draft_id", th.StringType),
    th.Property("type", th.StringType),
    th.Property("status", th.StringType),
    th.Property("sport", th.StringType),
    th.Property("season", th.StringType),
    th.Property("season_type", th.StringType),
    th.Property("draft_order", th.ObjectType()),
    th.Property("settings", th.ObjectType()),
    th.Property("metadata", th.ObjectType()),
    th.Property("start_time", th.IntegerType),
    th.Property("creators", th.ArrayType(th.StringType)),
    th.Property("created", th.IntegerType),
    th.Property("last_picked", th.IntegerType),
    th.Property("last_message_time", th.IntegerType),
    th.Property("last_message_id", th.StringType),
).to_dict()

league_draft_picks = th.PropertiesList(
    th.Property("league_id", th.StringType),
    th.Property("draft_id", th.StringType),
    th.Property("roster_id", th.IntegerType),
    th.Property("round", th.IntegerType),
    th.Property("player_id", th.StringType),
    th.Property("pick_no", th.IntegerType),
    th.Property("picked_by", th.StringType),
    th.Property("draft_slot", th.IntegerType),
    th.Property("is_keeper", th.BooleanType),
    th.Property(
        "metadata",
        th.ObjectType(
            th.Property("first_name", th.StringType),
            th.Property("last_name", th.StringType),
            th.Property("team", th.StringType),
            th.Property("sport", th.StringType),
            th.Property("position", th.StringType),
            th.Property("player_id", th.StringType),
            th.Property("number", th.StringType),
            th.Property("years_exp", th.StringType),
            th.Property("news_updated", th.StringType),
            th.Property("injury_status", th.StringType),
        ),
    ),
).to_dict()
