import os
import pytest


def test_hent_deltager(virk):
    cpr = os.getenv("TEST_CPR")
    if not cpr:
        pytest.skip("TEST_CPR is not set")

    deltager = virk.hent_deltager(cpr)
    assert deltager is not None


def test_hent_virksomhed(virk):
    cvr = os.getenv("TEST_CVR")
    if not cvr:
        pytest.skip("TEST_CVR is not set")

    virksomhed = virk.hent_virksomhed(cvr)
    assert virksomhed is not None
