import functools
import time


def memoize(func):
    """
    Naive memoization decorator
    If the need is speed, use functools.lru_cache instead as lru_cache is ~2x faster.
    """
    cache = {}

    @functools.wraps(func)
    def memo_wrapper(*args, **kwargs):
        nonlocal cache
        # Create unique identifier from args and kwargs passed to the function
        # Probably overkill for the use cases in which this is applied ... but hey ...
        # it's cool!!
        key = hash(args + tuple(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return memo_wrapper


def recursive_timer(func=None, *, stdout: bool = True):
    """
    Timer specifically for recursion
    By default will print out the total elapsed time in microseconds
    """
    is_evaluating = False

    # support passing keyword to @recursive_timer(stdout=False) or @recursive_timer()
    if func is None:
        return functools.partial(recursive_timer, stdout=stdout)

    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        nonlocal is_evaluating, stdout

        if is_evaluating:
            return func(*args, **kwargs)

        start_time = time.perf_counter()
        is_evaluating = True
        try:
            value = func(*args, **kwargs)
        finally:
            is_evaluating = False
        end_time = time.perf_counter()
        if stdout:
            print(
                f"Elapsed time '{func.__name__}{args, kwargs}': "
                f"{(end_time - start_time) * 1000:.6f} ms"
            )
        return value

    return wrapped_func
