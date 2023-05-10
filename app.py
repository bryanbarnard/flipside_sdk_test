import os
from flipside import Flipside
from dotenv import load_dotenv

# load variables from .env file
load_dotenv()


FLIPSIDE_API_KEY = os.environ['FLIPSIDE_API_KEY']
TTL_MINUTES = 60
MAX_AGE_MINUTES = 30
TIMEOUT_MINUTES = 10
RETRY_INTERVAL_SECONDS = 1
PAGE_SIZE = 50000

sdk = Flipside(FLIPSIDE_API_KEY)
sql = f""" 
    SELECT *
    FROM ethereum.core.ez_nft_sales
    WHERE NFT_ADDRESS = '0x6080b6d2c02e9a0853495b87ce6a65e353b74744'
    AND BLOCK_TIMESTAMP > '2023-04-01'
    ORDER BY BLOCK_TIMESTAMP DESC
    """

query_result_set = sdk.query(
    sql=sql,
    ttl_minutes=TTL_MINUTES,
    timeout_minutes=TIMEOUT_MINUTES,
    retry_interval_seconds=RETRY_INTERVAL_SECONDS,
    max_age_minutes=MAX_AGE_MINUTES,
    page_size=PAGE_SIZE
)

log_message = f'query_stats:\n - query_id: {query_result_set.query_id}\n' \
              f' - rows returned: {query_result_set.run_stats.record_count}\n' \
              f' - elapsed seconds: {query_result_set.run_stats.elapsed_seconds}\n' \
              f' - exec seconds: {query_result_set.run_stats.query_exec_seconds}\n'

print(log_message)
