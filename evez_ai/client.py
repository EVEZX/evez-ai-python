"""EVEZ AI Client — OpenAI-compatible free AI API."""
import json
import urllib.request
import urllib.error

BASE_URL = "https://evez-provider-production.up.railway.app/v1"


class EVEZClient:
    """Free AI API client — 35 models, $0/month."""

    def __init__(self, api_key: str, base_url: str = BASE_URL):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def _request(self, path: str, data: dict, method: str = "POST"):
        """Make an HTTP request to the EVEZ API."""
        url = f"{self.base_url}{path}"
        body = json.dumps(data).encode()
        req = urllib.request.Request(
            url, data=body, method=method,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            error_body = e.read().decode()
            try:
                return json.loads(error_body)
            except json.JSONDecodeError:
                raise RuntimeError(f"HTTP {e.code}: {error_body}")

    def chat(self, message: str, model: str = "evez-smart") -> str:
        """Send a chat message and return the response text."""
        data = self._request("/chat/completions", {
            "model": model,
            "messages": [{"role": "user", "content": message}],
        })
        if "choices" in data:
            return data["choices"][0]["message"]["content"]
        raise RuntimeError(f"API error: {data}")

    def models(self) -> list:
        """List available models."""
        url = f"{self.base_url}/models"
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {self.api_key}"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
        return data.get("data", [])

    def key_info(self) -> dict:
        """Get info about your API key."""
        return self._request("/key-info", {})


def signup(email: str, name: str = "User") -> dict:
    """Sign up for a free API key. No credit card required."""
    url = f"{BASE_URL}/signup"
    body = json.dumps({"email": email, "name": name}).encode()
    req = urllib.request.Request(
        url, data=body, method="POST",
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read())
