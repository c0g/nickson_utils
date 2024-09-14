import contextlib
import time

@contextlib.contextmanager
def print_exec_time():
    start = time.time()
    yield
    end = time.time()
    print(f"Time taken: {end - start}")