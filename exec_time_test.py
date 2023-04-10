from unittest import TestCase
from contextlib import contextmanager
from datetime import datetime


class ExecTimeTestCase(TestCase):
    @contextmanager
    def assertExecTime(self, exec_time: int) -> None:
        try:
            before_call = datetime.now().timestamp() * 1000
            yield
            after_call = datetime.now().timestamp() * 1000
        finally:
            self.assertLessEqual((after_call - before_call), exec_time)
