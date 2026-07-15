import httpx
import ssl


class VirkClient:
    def __init__(self, certifikat_sti: str, certifikat_nøglefil: str):
        # Public url
        self.base_url = "https://erst-api.virk.dk/distribution-service-cvr-ekstern"

        # Build SSL context explicitly so the client cert chain is loaded
        # the same way as in integrations that use ssl.load_cert_chain.
        ssl_context = ssl.create_default_context()
        ssl_context.load_cert_chain(
            certfile=certifikat_sti,
            keyfile=certifikat_nøglefil,
        )

        self.client = httpx.Client(base_url=self.base_url, verify=ssl_context)

    def get(self, endpoint: str, params: dict = None):
        response = self.client.get(endpoint, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint: str, data: dict = None):
        response = self.client.post(endpoint, json=data)
        response.raise_for_status()
        return response.json()

    def put(self, endpoint: str, data: dict = None):
        response = self.client.put(endpoint, json=data)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint: str):
        response = self.client.delete(endpoint)
        response.raise_for_status()
        return response.status_code

    def hent_deltager(self, cpr: str) -> dict | None:
        endpoint = f"/HentAktuelDeltagerEkstern/cprnr/{cpr}?virksomheder&attributter"

        try:
            return self.get(endpoint)
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            raise

    def hent_virksomhed(self, cvr: str):
        endpoint = f"/HentAktuelVirksomhedEkstern/cvrnr/{cvr}?deltagere&attributter"

        try:
            return self.get(endpoint)
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                return None
            raise
