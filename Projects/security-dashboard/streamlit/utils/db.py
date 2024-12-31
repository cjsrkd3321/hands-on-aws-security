from sqlalchemy import create_engine, text


engine = create_engine("postgresql://steampipe:6ec2_45b9_8fc5@127.0.0.1:9193/steampipe")


def clear_cache():
    with engine.connect() as conn:
        conn.execute(text("select from steampipe_internal.meta_cache('clear')"))
