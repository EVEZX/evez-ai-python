# evez-ai

Free AI API client — 35 models, OpenAI-compatible, **$0/month**.

## Install

```bash
pip install evez-ai
```

## Quick Start

```python
from evez_ai import EVEZClient, signup

# Get a free API key
result = signup("you@email.com")
print(result["key"])  # evez-...

# Use the API
evez = EVEZClient(result["key"])
reply = evez.chat("Explain quantum computing in 3 sentences")
print(reply)

# List models
models = evez.models()
for m in models:
    print(m["id"])
```

## No dependencies. Pure Python 3.7+.

## Pricing

**$0/month.** 60 requests/minute. No credit card.

## Links

- [API Docs](https://evezx.github.io/evez-ai/api-docs.html)
- [Try Demo](https://evezx.github.io/evez-ai/demo.html)
- [GitHub](https://github.com/EVEZX/evez-ai)
