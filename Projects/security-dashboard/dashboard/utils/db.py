from sqlalchemy import create_engine, text


engine = create_engine("postgresql://steampipe:6ec2_45b9_8fc5@127.0.0.1:9193/steampipe")


def query_execute(sql_query):
    with engine.connect() as conn:
        conn.execute(text(sql_query))
