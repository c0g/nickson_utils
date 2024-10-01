import contextlib
import time
import numpy as np

@contextlib.contextmanager
def print_exec_time():
    start = time.time()
    yield
    end = time.time()
    print(f"Time taken: {end - start}")

def ls_npz(path):
    """list the entries inside a .npz file"""
    with np.load(path) as data:
        for key in data.files:
            print(key)

def strided_sequence(data: np.ndarray, seq_len: int, seperation: int):
    """Splits data [l, d] into [m, seq_len, d], where the start index of each
    row is seperated by `seperation` samples, and each row is length seq_len."""
    # Calculate the number of sequences
    num_sequences = (data.shape[0] - seq_len) // seperation + 1

    # Use as_strided to create the strided view
    strided = np.lib.stride_tricks.as_strided(
        data,
        shape=(num_sequences, seq_len, data.shape[1]),
        strides=(data.strides[0] * seperation, data.strides[0], data.strides[1]),
    )
    return strided