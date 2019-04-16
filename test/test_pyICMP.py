#!/usr/bin/python3

import pytest

import pyICMP

def test_ping_localhost():
    assert pyICMP.ping('127.0.0.1') == True

def test_ping_dns():
    assert pyICMP.ping('google.com') == True

def test_ping_known_bad_address():
    assert pyICMP.ping('100.87.0.0') == False

def test_invalid_ip_address():
    with pytest.raises(ValueError):
        pyICMP.ping('invalid_address')

def test_ping_count():
    assert pyICMP.ping('8.8.8.8', count=8)

def test_ttl():
    assert pyICMP.ping('8.8.8.8', ttl=128)

def test_too_low_ttl():
    assert pyICMP.ping('8.8.8.8', ttl=1) == False