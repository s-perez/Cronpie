from unittest.mock import MagicMock, patch

import freezegun

from cronpie import runner as runner_module


class TestRunner:

    @freezegun.freeze_time('2016-08-26 23:00:59')
    @patch('time.sleep')
    def test_runner_sleeps_required_time(self, mock, simple_cron_entry,
                                         scheduler, runner):
        scheduler.register(simple_cron_entry)
        runner._sleep_until_next_execution()
        mock.assert_called_with(1)

    def test_runner_spawns_command(self, runner):
        mock = MagicMock()
        mock.pid = 10005
        mock.return_value = mock
        with patch('multiprocessing.Process', mock):
            pid = runner._run_task(['ls'])
            assert pid == 10005
            mock.assert_called_with(
                target=runner_module._run_command,
                args=(['ls'])
            )
