# TrustMesh AI
### Explainable Multi-Agent Zero Trust Security Platform

**INNOVEX 2026 | Digital Security | AI-Powered Cybersecurity**

TrustMesh AI is a functional cybersecurity prototype combining Zero Trust principles, multi-agent AI investigation, deterministic risk scoring, and explainable access-control decisions.

The platform evaluates simulated access requests using identity, device, and behavioral signals to determine whether access should be **ALLOWED, CHALLENGED, or DENIED**.

**Developed by:** Jyothi Srinivasan

**[Watch Video Demo](https://youtu.be/-mjXR60YCRQ)** | **[GitHub Repository](https://github.com/JyothiSrinivasan/TrustMesh-AI)**

<img width="1890" height="1131" alt="trustmesh_frame" src="https://github.com/user-attachments/assets/935bd51d-a52d-4f8d-a3cf-bd2bb4328f25" />

---

## 1. Problem Statement

Traditional identity-based authentication does not always provide sufficient protection against compromised credentials, unfamiliar devices, and suspicious login activity.

TrustMesh AI demonstrates how contextual risk assessment and AI-assisted security investigations can support more informed and explainable access decisions.

## 2. Key Features

- **Five specialized AI agents:** Identity, Device, Behavior, Policy, and Security Response.
- **Zero Trust Risk Engine:** Deterministic risk scoring and access-policy enforcement.
- **Three Security Decisions:** ALLOW, CHALLENGE, and DENY.
- **3D Digital Trust Twin:** Interactive visualization of security context.
- **Threat Investigations:** Visual incident investigation timeline.
- **AI Explanations:** Agent-generated findings and security recommendations.
- **Incident History:** SQLite-backed investigation records.
- **PDF Reports:** Downloadable investigation summaries.
- **Local AI Processing:** Ollama and Qwen2.5 for local inference.

## 3. Five AI Security Agents

| Agent | Responsibility |
|---|---|
| Identity Intelligence | Analyzes identity and authentication indicators |
| Device & Context | Evaluates device trust and contextual signals |
| Behavioral Threat Analysis | Investigates suspicious login patterns |
| Policy Decision Intelligence | Explains policy considerations and decisions |
| Security Response & Audit | Produces incident explanations and response recommendations |

The agents provide advisory analysis. The deterministic security engine remains responsible for the final access decision.

## 4. System Architecture

```text
React + Vite Dashboard
        |
        v
FastAPI Backend
        |
        +--> Deterministic Risk & Policy Engine
        |
        +--> Multi-Agent Orchestrator
        |          |
        |          v
        |     n8n Workflows
        |          |
        |          v
        |     Ollama + Qwen2.5
        |
        +--> SQLite Incident Database
        |
        +--> PDF Investigation Reports
        |
        v
Final Decision: ALLOW / CHALLENGE / DENY
```

## 5. Technology Stack

| Layer | Technologies |
|---|---|
| Frontend | React, Vite, JavaScript |
| 3D Visualization | Three.js, React Three Fiber, Drei |
| Backend | Python, FastAPI, REST APIs |
| AI Automation | n8n |
| Local LLM | Ollama, Qwen2.5:3b |
| Database | SQLite |
| PDF Generation | ReportLab |
| Development | VS Code, Git, GitHub |
| Frontend Hosting | Cloudflare Pages |

## 6. Demonstration Scenarios

| Scenario | Risk Score | Decision |
|---|---:|---|
| Aruna — Trusted Login | 0/100 | ALLOW |
| Naveen — Untrusted Device | 40/100 | CHALLENGE |
| Ravi — Suspicious Login | 100/100 | DENY |

These scenarios demonstrate contextual security decisions using simulated access events.

## 7. Performance Testing

The five-agent investigation pipeline was tested locally with the following results:

| Test | Processing Time |
|---|---:|
| Test 1 | 5.80 seconds |
| Test 2 | 9.86 seconds |
| Test 3 | 8.17 seconds |
| **Average** | **7.94 seconds** |

These are observed local test results, not guaranteed production performance.

## 8. Running Locally

### Prerequisites

- Python and Node.js
- Ollama with the `qwen2.5:3b` model
- n8n
- Required Python and frontend dependencies

### Backend

From the project root, activate the Python virtual environment and start FastAPI:

```powershell
.\.venv\Scripts\python.exe -m uvicorn backend.main:app --reload --port 7654
```

Backend URL: `http://127.0.0.1:7654`

### Frontend

From the frontend directory, install dependencies and start the Vite development server:

```powershell
npm install
npm run dev
```

Open the local URL displayed by Vite.

### AI Services

Start Ollama and ensure the `qwen2.5:3b` model is installed.

Import the five provided n8n workflows into a running n8n instance and configure their Ollama connections and webhook endpoints.

The FastAPI orchestrator must be configured to use the correct n8n webhook URLs.

**Note:** The Cloudflare Pages deployment hosts the frontend only. Full AI investigation functionality requires the backend, n8n workflows, and Ollama services.

## 9. Security and Design Principles

TrustMesh AI demonstrates:

- Zero Trust access evaluation
- Separation of AI recommendations and security enforcement
- Explainable incident investigations
- Contextual risk assessment
- Local LLM processing
- Auditable security decisions

The application uses simulated security events and is intended for research, education, and prototype demonstration. It is not a production-ready identity and access management system.

## 10. Future Enhancements

- Enterprise identity-provider integration
- Real-time authentication event ingestion
- Continuous session risk monitoring
- SIEM and SOAR integrations
- Agent evaluation and security benchmarking
- Production authentication and access-control integration

## 11. Hackathon Submission

**Event:** INNOVEX 2026

**Project:** TrustMesh AI — Explainable Multi-Agent Zero Trust Security Platform

**Developer:** Jyothi Srinivasan

**Video Demonstration:** https://youtu.be/-mjXR60YCRQ

**Source Code:** https://github.com/JyothiSrinivasan/TrustMesh-AI

---

*TrustMesh AI — Intelligent Investigation. Explainable Decisions. Zero Trust Security.*
