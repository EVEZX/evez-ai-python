"""EVEZ AI — Free AI API client. 49 models. $0/month. Zero dependencies."""

import json
import urllib.request
import urllib.error

BASE_URL = "https://evez-provider-production.up.railway.app/v1"
FALLBACK_URL = "http://66.42.125.106:9100/v1"

class EVEZClient:
    """EVEZ AI client. Drop-in replacement for OpenAI client.
    
    Usage:
        client = EVEZClient()
        print(client.chat("Hello!"))
        print(client.chat("Write code", model="deepseek-v3"))
    """
    
    def __init__(self, api_key="", base_url=None):
        self.api_key = api_key
        self.base_url = base_url or BASE_URL
    
    def chat(self, message, model="deepseek-v3", max_tokens=500):
        """Send a chat message and return the response text."""
        body = json.dumps({
            "model": model,
            "messages": [{"role": "user", "content": message}],
            "max_tokens": max_tokens
        }).encode()
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        
        # Try primary, then fallback
        for url in [self.base_url, FALLBACK_URL]:
            try:
                req = urllib.request.Request(
                    f"{url}/chat/completions",
                    data=body, method="POST", headers=headers
                )
                with urllib.request.urlopen(req, timeout=60) as r:
                    data = json.loads(r.read())
                    content = data["choices"][0]["message"].get("content")
                    if content:
                        return content
                    # Some models put content in reasoning field
                    return data["choices"][0]["message"].get("reasoning", "No response")
            except Exception:
                continue
        return "Error: all backends failed"
    
    def models(self):
        """List available model IDs."""
        try:
            with urllib.request.urlopen(f"{self.base_url}/models", timeout=10) as r:
                data = json.loads(r.read())
                return [m["id"] for m in data.get("data", [])]
        except:
            return []
    
    def key_info(self):
        """Get info about your API key."""
        if not self.api_key:
            return {"error": "No API key set"}
        try:
            req = urllib.request.Request(f"{self.base_url}/key-info",
                headers={"Authorization": f"Bearer {self.api_key}"})
            with urllib.request.urlopen(req, timeout=10) as r:
                return json.loads(r.read())
        except Exception as e:
            return {"error": str(e)}


def signup(email):
    """Create a free API key. Returns dict with 'key' field."""
    body = json.dumps({"email": email}).encode()
    for url in [BASE_URL, FALLBACK_URL]:
        try:
            req = urllib.request.Request(f"{url}/signup",
                data=body, method="POST",
                headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=10) as r:
                return json.loads(r.read())
        except:
            continue
    return {"error": "All backends failed"}
