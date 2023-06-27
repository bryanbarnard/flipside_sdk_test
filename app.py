import os
from flipside import Flipside
from dotenv import load_dotenv

# load variables from .env file
load_dotenv()

FLIPSIDE_API_KEY = os.environ['FLIPSIDE_API_KEY']
TTL_MINUTES = 10
MAX_AGE_MINUTES = 10
TIMEOUT_MINUTES = 2
RETRY_INTERVAL_SECONDS = 2
PAGE_SIZE = 100

sdk = Flipside(FLIPSIDE_API_KEY)
sql = """
                SELECT *
                FROM ethereum.core.fact_decoded_event_logs
                WHERE CONTRACT_ADDRESS = '0x98ca78e89dd1abe48a53dee5799f24cc1a462f2d'
                AND EVENT_NAME = 'ExtendExpiry'
                AND BLOCK_TIMESTAMP > '2023-05-31 02:08:35'
                ORDER BY BLOCK_TIMESTAMP DESC
                LIMIT 20000;
    """

i = 1
while i <= 5:
    try:
        query_result_set = sdk.query(
            sql=sql,
            ttl_minutes=TTL_MINUTES,
            timeout_minutes=TIMEOUT_MINUTES,
            retry_interval_seconds=RETRY_INTERVAL_SECONDS,
            max_age_minutes=MAX_AGE_MINUTES,
            page_size=PAGE_SIZE
        )

        log_message = f'query run {i} query_stats:\n - query_id: {query_result_set.query_id}\n' \
                      f' - query status: {query_result_set.status}\n' \
                      f' - rows returned: {query_result_set.run_stats.record_count}\n' \
                      f' - elapsed seconds: {query_result_set.run_stats.elapsed_seconds}\n' \
                      f' - exec seconds: {query_result_set.run_stats.query_exec_seconds}\n'

        print(log_message)
    except Exception as e:
        print(e)
    finally:
        i += 1
