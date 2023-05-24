import argparse
from typing import Any, Callable, Union

import pytest

from cruisecontrolclient.client import ExecutionContext


@pytest.mark.parametrize('endpoint', ExecutionContext.NAME_TO_ENDPOINT.keys())
def test_check(endpoint: str,
               namespace_builder: Union[Callable[[Any], argparse.Namespace], Callable[[Any, Any], argparse.Namespace]],
               capsys):
    if not ExecutionContext.NAME_TO_ENDPOINT[endpoint].requires_broker_ids:
        with pytest.raises(SystemExit):
            namespace_builder(endpoint, '123')
        captured = capsys.readouterr()

        assert "unrecognized arguments" in captured.err
    else:
        with pytest.raises(SystemExit):
            namespace_builder(endpoint)

        captured = capsys.readouterr()

        assert "the following arguments are required: brokers" in captured.err
