import pytest
import logging
from homework10 import log_event


def test_log_event_success(caplog):
    with caplog.at_level(logging.INFO):
        log_event('user1', 'success')
    assert caplog.records[0].message == 'Login event - Username: user1, Status: success'
    assert caplog.records[0].levelname == 'INFO'


def test_log_event_expired(caplog):
    with caplog.at_level(logging.WARNING):
        log_event('user2', 'expired')
    assert caplog.records[0].message == 'Login event - Username: user2, Status: expired'
    assert caplog.records[0].levelname == 'WARNING'


def test_log_event_failed(caplog):
    with caplog.at_level(logging.ERROR):
        log_event('user3', 'failed')
    assert caplog.records[0].message == 'Login event - Username: user3, Status: failed'
    assert caplog.records[0].levelname == 'ERROR'


def test_log_event_unknown_status(caplog):
    with caplog.at_level(logging.ERROR):
        log_event('user4', 'unknown')
    assert caplog.records[0].message == 'Login event - Username: user4, Status: unknown'
    assert caplog.records[0].levelname == 'ERROR'



