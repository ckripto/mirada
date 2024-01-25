from functools import wraps
from time import sleep, time
from typing import Optional


def wait_for_success(max_wait_time: int = 60, interval: int = 5):
    def wrapper(func):
        @wraps(func)
        def impl(*a, **kw):
            start = time()
            last_exception: Optional[BaseException] = None
            while time() - start <= max_wait_time:
                try:
                    return func(*a, **kw)
                except BaseException as ex:
                    last_exception = ex
                    sleep(interval)

            raise last_exception or TimeoutError(f"No completed in {max_wait_time}s")

        return impl

    return wrapper
