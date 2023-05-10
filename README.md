# Flipside Crypto SDK Test Project
Simple repo to test flipside crypto SDK. Created this project to better understand and test functionality introduced in the Flipside Crypto 2.0.x SDK updates.


## Flipside Crypto SDK
https://github.com/FlipsideCrypto/sdk

## To Run
1. Clone the repo
2. Create a .env file that contains your Flipside Crypto API Key. Details on how to get an API key and API Docs can be found at https://docs.flipsidecrypto.com/flipside-api/get-started
3. Create a python environment using venv based on Python Version 3.9.12
4. Install dependencies, `python -m pip install -r requirements.txt`
5. Run the app `python app.py`

Expected results should be similar to:
```
query_stats:
 - query_id: clhhv3pjh00hvn30tng79twb6
 - rows returned: 251
 - elapsed seconds: 15
 - exec seconds: 9
 ```
