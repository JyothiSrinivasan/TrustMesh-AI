
import asyncio
import httpx

N8N_BASE_URL = "http://127.0.0.1:5679/webhook"

AGENTS = {
    "identity": "trustmesh-identity",
    "device": "trustmesh-device",
    "behavior": "trustmesh-behavior",
    "policy": "trustmesh-policy",
    "response": "trustmesh-response",
}


async def run_security_agents(event: dict):
    results = {}

    async with httpx.AsyncClient(timeout=180.0) as client:

        async def call_agent(name, endpoint):
            try:
                response = await client.post(
                    f"{N8N_BASE_URL}/{endpoint}",
                    json=event,
                )
                response.raise_for_status()

                data = response.json()

                return name, {
                    "status": "success",
                    "analysis": data.get("ai_analysis", ""),
                }

            except Exception as exc:
                return name, {
                    "status": "error",
                    "message": str(exc),
                }

        tasks = [
            call_agent(name, endpoint)
            for name, endpoint in AGENTS.items()
        ]

        responses = await asyncio.gather(*tasks)

        for name, result in responses:
            results[name] = result

    return results
