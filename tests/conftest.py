import os
import pytest

from pathlib import Path
from src import VirkClient


PROJECT_ROOT = Path(__file__).parent.parent


@pytest.fixture
def virk() -> VirkClient:
    base_url = os.getenv("BASE_URL")
    if not base_url:
        pytest.skip("BASE_URL is not set")

    certifikat_sti = PROJECT_ROOT / "certificates" / "client.crt"
    certifikat_noglefil = PROJECT_ROOT / "certificates" / "client.key"

    if not certifikat_sti.exists() or not certifikat_noglefil.exists():
        pytest.skip("Client certificate files are missing in certificates/")

    return VirkClient(
        base_url=base_url,
        certifikat_sti=str(certifikat_sti),
        certifikat_nøglefil=str(certifikat_noglefil),
    )
