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
SDK = Flipside(FLIPSIDE_API_KEY)


def main():
    _sql = """
            SELECT
            BLOCK_NUMBER,
            BLOCK_TIMESTAMP,
            TO_VARCHAR(BLOCK_TIMESTAMP, 'YYYY-MM-DD HH24:MI:SS') AS MOD_TIMESTAMP,
            TX_HASH,
            EVENT_INDEX,
            LOWER(DECODED_LOG['_profileURI']) AS PROFILE_NAME,
            TO_TIMESTAMP(DECODED_LOG['_extendedExpiry']) AS EXTENDED_EXPIRY,
            TO_VARCHAR(EXTENDED_EXPIRY, 'YYYY-MM-DD HH24:MI:SS') AS MOD_EXT_EXPIRY
            FROM
            ethereum.core.fact_decoded_event_logs
            WHERE
            CONTRACT_ADDRESS = '0x98ca78e89dd1abe48a53dee5799f24cc1a462f2d'
            AND EVENT_NAME = 'ExtendExpiry'
            AND BLOCK_TIMESTAMP > '2023-05-31 02:08:35'
            ORDER BY
            BLOCK_TIMESTAMP DESC
            LIMIT
            20000;
        """

    i = 1  # this is the initial iterator value
    N = 1  # this is the total time to run

    while i <= N:
        try:
            query_result_set = SDK.query(
                sql=_sql,
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


if __name__ == '__main__':
    main()
