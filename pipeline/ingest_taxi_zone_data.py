import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm


dtype = {
    "LocationID" : "Int64",
    "Borough" : "string",
    "Zone" : "string",
    "service_zone" : "string"
}

def run():

    url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv'

    pg_user = 'root'
    pg_pass = 'root'
    pg_host = 'localhost'
    pg_port = '5432'
    pg_db = 'ny_taxi'

    engine = create_engine(f'postgresql+psycopg://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    target_table = 'taxi_zone_lookup'

    df = pd.read_csv(
        url,
        dtype = dtype
    )

    df.head(0).to_sql(name=target_table, con=engine, if_exists='replace')

    df.to_sql(name=target_table, con=engine, if_exists='append')


if __name__ == '__main__':
    run()