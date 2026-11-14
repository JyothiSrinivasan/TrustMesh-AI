# TrustMesh AI — n8n Workflow Exports

Five sanitized n8n workflow definitions for the TrustMesh AI security simulation.

## Import

1. Run n8n and Ollama locally, and pull the `qwen2.5:3b` model.
2. In n8n, import each JSON file as a new workflow.
3. Open each **Message a model** node and select or create your own Ollama credential (configure the Ollama base URL for your environment).
4. Confirm each webhook path and that your FastAPI backend is configured to call the matching production webhook endpoint.
5. Save, publish/activate each workflow, then test with simulated events.

| File | Webhook path |
|---|---|
| `trustmesh-identity.json` | `trustmesh-identity` |
| `trustmesh-device.json` | `trustmesh-device` |
| `trustmesh-behavior.json` | `trustmesh-behavior` |
| `trustmesh-policy.json` | `trustmesh-policy` |
| `trustmesh-response.json` | `trustmesh-response` |

These exports deliberately omit n8n credential references, webhook IDs, instance metadata, execution history and pinned data. They are **inactive** when imported and must be configured before use. Do not commit secrets or real security-event data. This is a simulation, not a production IAM solution.
