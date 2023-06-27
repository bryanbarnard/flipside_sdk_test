# test_app.py
import app
from time import perf_counter


def test_app():
    start = perf_counter()
    result = app.main()
    stop = perf_counter()
    elapsed_seconds = stop - start
    expected_in_seconds = 10
    assert elapsed_seconds < expected_in_seconds
