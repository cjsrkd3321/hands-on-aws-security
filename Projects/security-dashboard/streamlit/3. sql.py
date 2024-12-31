import pandas as pd
from sqlalchemy import create_engine


engine = create_engine("postgresql://steampipe:6ec2_45b9_8fc5@127.0.0.1:9193/steampipe")

df = pd.read_sql_query(
    "SELECT start_time, steampipe_version, fdw_version, cache_max_ttl, cache_enabled FROM steampipe_server_settings",
    con=engine,
)

print(df)
