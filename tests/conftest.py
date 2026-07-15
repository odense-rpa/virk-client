import pytest

from pathlib import Path
from src import VirkClient


PROJECT_ROOT = Path(__file__).parent.parent


@pytest.fixture
def virk() -> VirkClient:
    certifikat_sti = PROJECT_ROOT / "certificates" / "client.crt"
    certifikat_nøglefil = PROJECT_ROOT / "certificates" / "client.key"

    if not certifikat_sti.exists() or not certifikat_nøglefil.exists():
        pytest.skip("Client certificate files are missing in certificates/")

    return VirkClient(        
        certifikat_sti=str(certifikat_sti),
        certifikat_nøglefil=str(certifikat_nøglefil),
    )
