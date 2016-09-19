from unittest.mock import MagicMock

class TestProber:

    def test_sweeps_pid_list(self, prober):
        mock = MagicMock()
        mock.return_value = mock
        prober._pids = [10001,10002,10003]
