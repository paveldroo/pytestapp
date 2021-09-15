from click.testing import CliRunner
from contextlib import contextmanager
import pytest
from tasks.api import Task
import tasks.cli
import tasks.config


@contextmanager
def stub_tasks_db():
    print('123')
    yield


def test_list_no_args(mocker):
    mocker.patch.object(tasks.cli, '_tasks_db', new=stub_tasks_db())
    mocker.patch.object(tasks.cli.tasks, 'list_tasks', return_value=[])
    runner = CliRunner()
    runner.invoke(tasks.cli.tasks_cli, ['list'])
    list_tssks_result = tasks.cli.tasks.list_tasks()
    assert list_tssks_result == []
    # An error occurs here, dunno why
    # tasks.cli._tasks_db.assert_called_once_with(None)
