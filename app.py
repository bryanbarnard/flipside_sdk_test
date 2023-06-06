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
        SELECT
          BLOCK_NUMBER as "block_number",
          (SELECT DATE_PART(epoch_second, BLOCK_TIMESTAMP)) as epoch_timestamp,
          BLOCK_TIMESTAMP AS "timestamp",
          TOKENID AS "gk_token_id",
          PRICE AS "eth_amount",
          PLATFORM_NAME AS "exchange",
          SELLER_ADDRESS as "seller",
          BUYER_ADDRESS as "buyer",
          TX_HASH as "tx_hash"
        FROM ethereum.core.ez_nft_sales
        WHERE BLOCK_TIMESTAMP > '2023-04-17 00:00:00.000'
        AND NFT_ADDRESS = '0x8fb5a7894ab461a59acdfab8918335768e411414' 
        ORDER BY BLOCK_TIMESTAMP DESC;
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
