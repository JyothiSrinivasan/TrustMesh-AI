# TrustMesh AI

### Multi-Agent Zero Trust Identity & Access Security Platform

**TrustMesh AI** is a functional cybersecurity simulation platform combining deterministic Zero Trust access-policy evaluation, five AI investigation agents, security automation, and an interactive 3D Digital Trust Twin.

**Hackathon:** INNOVEX 2026 — Global Innovation Hackathon  
**Problem Statement:** PS 05 — AI-Powered Cybersecurity (Digital Security)  
**Development:** Solo project  
**Status:** Functional local prototype

---

## Project Demo & Links

- **GitHub Repository:** https://github.com/JyothiSrinivasan/TrustMesh-AI
- **Frontend Preview:** https://trustmesh-ai.pages.dev
- **YouTube Demonstration:** Coming soon — link will be added after recording.

**Demo availability:** The Cloudflare Pages deployment currently provides a frontend preview. Full AI investigations, backend policy evaluation, incident storage, and PDF reporting run in the local development environment.

---

## Problem Statement

Modern organizations must protect sensitive digital resources against unauthorized access, compromised accounts, suspicious login attempts, and untrusted devices.

Traditional access-monitoring systems can generate alerts without providing sufficient context for security analysts to understand the underlying risk or determine appropriate next steps.

TrustMesh AI explores how deterministic access-control policies and AI-assisted investigations can work together to improve security decision-making and incident analysis.

### Proposed Solution

TrustMesh AI demonstrates a Zero Trust-inspired workflow that:

1. Evaluates simulated identity, device, behavioral, and resource-access signals.
2. Calculates a security risk score.
3. Determines whether access should be **ALLOW**, **CHALLENGE**, or **DENY**.
4. Orchestrates five specialized AI agents to investigate the event.
5. Presents investigation findings through an interactive dashboard.
6. Stores incident records and generates downloadable PDF reports.

The access decision is determined by backend policy rules. AI-generated analysis is advisory and cannot override the decision.

---

## Key Features

- **Zero Trust Policy Engine:** Evaluates simulated identity, device, resource, and behavioral signals to return ALLOW, CHALLENGE, or DENY.
- **Five AI Security Agents:** Investigate identity risk, device context, behavioral indicators, policy decisions, and security response.
- **3D Digital Trust Twin:** Interactive visualization of relationships between identities, devices, resources, and security analysis.
- **Attack Simulation Center:** Runs trusted-access, suspicious-login, and untrusted-device scenarios.
- **Incident Investigation Story:** Animated five-stage visualization of the investigation process.
- **Incident History:** Stores and retrieves investigations using SQLite.
- **PDF Investigation Reports:** Generates reports containing security decisions, risk indicators, and AI-agent findings.
- **Local AI Processing:** Uses Ollama and Qwen2.5 for AI-assisted investigation without relying on a paid cloud LLM API.

---

## Five AI Security Agents

| Agent | Responsibility |
|---|---|
| Identity Intelligence | Analyzes identity and access-request context |
| Device & Context | Examines device trust and available context |
| Behavioral Threat | Evaluates suspicious login and behavioral indicators |
| Policy Decision | Explains the deterministic access-policy decision |
| Security Response & Audit | Recommends investigation, verification, and response actions |

The agents operate through n8n workflows and a locally hosted language model.

**Important:** The AI agents provide advisory analysis. They do not override the deterministic policy engine.

### AI Agent Workflow Source Files

All five sanitized n8n workflows are available in the [n8n-workflows directory](https://github.com/JyothiSrinivasan/TrustMesh-AI/tree/main/n8n-workflows).

The directory contains the Identity Intelligence, Device & Context, Behavioral Threat, Policy Decision, and Security Response & Audit agents.

Each workflow can be imported into n8n and configured with a local Ollama connection. The exports exclude credential references and private instance metadata.

See the directory's README for setup instructions.

---

## Technology Stack

| Layer | Technologies |
|---|---|
| Frontend | React, Vite, JavaScript, CSS |
| 3D Visualization | Three.js, React Three Fiber, Drei |
| Backend | Python, FastAPI, Pydantic |
| AI Orchestration | n8n |
| Local Language Model | Ollama, Qwen2.5:3b |
| Database | SQLite |
| PDF Reports | ReportLab, Python-Markdown |
| UI Components | Lucide React |
| Frontend Hosting | Cloudflare Pages |
| Version Control | Git, GitHub |

---

## System Architecture

```text
                   React Dashboard
                          |
                          v
                    FastAPI Backend
                          |
           +--------------+--------------+
           |              |              |
           v              v              v
     Security Policy   AI Orchestrator  Incident Storage
         Engine             |              SQLite
           |                v
           |          n8n Workflows
           |                |
           |                v
           |          Ollama Qwen2.5
           |                |
           |                v
           |          Five AI Agents
           |                |
           +-------+--------+
                   |
                   v
           Investigation Results
                   |
                   v
          Dashboard + PDF Reports
```

### Architecture Principles

**Deterministic enforcement:** Access decisions are made using backend rules, not LLM-generated responses.

**AI-assisted investigation:** Specialized agents interpret security indicators and recommend follow-up actions.

**Separation of concerns:** The frontend handles visualization, FastAPI handles policy evaluation and orchestration, and SQLite maintains incident history.

**Local-first development:** AI inference and workflow orchestration operate locally.

---

## Demonstration Scenarios

| Scenario | Decision | Risk Score |
|---|---|---|
| Trusted Employee | ALLOW | 0/100 |
| Untrusted Device | CHALLENGE | 40/100 |
| Suspicious Login | DENY | 100/100 |

### Scenario 1 — Trusted Employee

A simulated authorized employee accesses a permitted resource from a trusted device.

**Expected result:** ALLOW — Low Risk.

### Scenario 2 — Untrusted Device

A simulated access request originates from a device marked as untrusted.

**Expected result:** CHALLENGE — Medium Risk.

The decision indicates that additional verification is required. A live MFA challenge is not implemented in the current prototype.

### Scenario 3 — Suspicious Login

A simulated access request contains multiple high-risk indicators.

**Expected result:** DENY — High Risk.

The backend policy engine evaluates the supplied risk indicators and denies access when the configured threshold is reached.

These scenarios use predefined simulation inputs and rule-based risk scoring.

---

## How to Test TrustMesh AI

The application supports an end-to-end local demonstration.

1. Start the FastAPI backend, n8n workflows, Ollama, and React frontend.
2. Open `http://localhost:5173`.
3. Navigate to **Command Center**.
4. Select one of the three security scenarios.
5. Click **Launch Investigation**.
6. Review the risk score and ALLOW, CHALLENGE, or DENY decision.
7. Navigate to **AI Agent Network** to explore the five agents.
8. Open **Threat Investigations** to review the visual incident story.
9. Download the PDF investigation report.
10. Open **Incident Database** to review stored investigations.

The AI services must be configured and running for the complete investigation workflow.

---

## Running Locally

### Requirements

- Python 3.11 or newer
- Node.js and npm
- Ollama with the `qwen2.5:3b` model
- n8n with the five configured TrustMesh AI workflows

### Backend Setup

From the project root:

```bash
python -m venv .venv
```

Activate the virtual environment.

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install fastapi "uvicorn[standard]" httpx pydantic python-dotenv reportlab markdown
```

Start the backend:

```bash
python -m uvicorn backend.main:app --reload --port 7654
```

The backend runs at:

`http://localhost:7654`

### Frontend Setup

Open a separate terminal:

```bash
cd frontend
npm install
npm run dev
```

Open:

`http://localhost:5173`

### AI Services

Install and configure Ollama:

```bash
ollama pull qwen2.5:3b
```

Start n8n on port `5679` and configure the five workflows with these webhook paths:

- `/webhook/trustmesh-identity`
- `/webhook/trustmesh-device`
- `/webhook/trustmesh-behavior`
- `/webhook/trustmesh-policy`
- `/webhook/trustmesh-response`

**Setup limitation:** The n8n workflow definitions must be configured separately. The repository's application code alone does not currently reproduce the complete AI-agent environment.

---

## Innovation & Technical Differentiation

TrustMesh AI combines several complementary cybersecurity capabilities into a single prototype.

**1. Multi-agent security investigation**

Five specialized agents examine different aspects of the same access event, rather than relying on one general-purpose AI response.

**2. Deterministic policy enforcement**

Backend security rules determine access decisions independently of AI-generated explanations.

**3. Interactive 3D Digital Trust Twin**

A visual interface helps demonstrate relationships between access requests, security risks, and investigation workflows.

**4. End-to-end investigation lifecycle**

The platform connects risk evaluation, AI analysis, incident storage, visual storytelling, and PDF reporting.

**5. Local AI architecture**

The project uses a locally hosted language model, providing a foundation for future privacy-conscious security analysis.

---

## Potential Real-World Impact

TrustMesh AI demonstrates concepts that could support:

- **Security Operations Centers:** AI-assisted investigation and incident documentation.
- **Financial institutions:** Risk assessment for access to sensitive financial resources.
- **Enterprise IT security:** Review of suspicious employee access requests.
- **Identity and Access Management teams:** Analysis of device trust and authentication-related risk indicators.
- **Cybersecurity training:** Interactive demonstrations of Zero Trust concepts and security investigations.

The prototype is intended to demonstrate these applications, not to claim production deployment or measured improvements in operational performance.

---

## Security Scope and Limitations

TrustMesh AI is a hackathon prototype and security simulation, not a production-ready identity and access management system.

- Identity, role, and device attributes are supplied as simulation inputs.
- Real identity verification, device attestation, and MFA enforcement are not implemented.
- Access-policy decisions are deterministic; AI analysis is advisory.
- AI-generated explanations may require human review.
- The current backend does not provide production-grade authentication, authorization, or rate limiting.
- The project should not be used to protect real sensitive resources without further security engineering.
- The public Cloudflare Pages frontend is not a fully connected hosted deployment of the local backend and AI services.

---

## Future Enhancements

- Verified authentication and role-based access control
- Keycloak integration for IAM and MFA
- Open Policy Agent for centralized policy management
- Wazuh integration for security telemetry
- AI-output validation and consistency checks
- Enterprise audit logging and monitoring
- Secure remote deployment with authenticated API access
- Importable n8n workflow definitions and reproducible environment configuration

---

## Project Status

**Functional hackathon prototype**

Implemented and locally tested:

- React dashboard and interactive 3D visualization
- FastAPI security policy engine
- Five-agent AI orchestration
- Simulated access scenarios
- SQLite incident database
- PDF investigation reports

**Public deployment:** Frontend preview hosted on Cloudflare Pages.

**Full functionality:** Available through the local development environment with the required services running.

---

## Demo & Functional Verification

TrustMesh AI has been locally tested as a functional Zero Trust cybersecurity simulation platform.

### Verified Demonstration

| Component | Verification |
|---|---|
| React Command Center | Working |
| Interactive 3D Digital Trust Twin | Working |
| FastAPI Security Policy Engine | Working |
| ALLOW / CHALLENGE / DENY Decisions | Verified with predefined scenarios |
| Five n8n AI Agent Workflows | All five reported successful execution |
| Local Ollama Qwen2.5 Integration | AI investigation findings generated |
| SQLite Incident Database | Incident records stored and retrieved |
| PDF Investigation Reports | Successfully generated and downloaded |

### Security Scenario Results

| Scenario | Decision | Risk Score |
|---|---|---|
| Trusted Employee | ALLOW | 0/100 |
| Untrusted Device | CHALLENGE | 40/100 |
| Suspicious Login | DENY | 100/100 |

### Verified Incident: INC-0011

The suspicious-login simulation produced the following results:

- **Identity:** bob
- **Device:** laptop-02
- **Protected Resource:** finance-reports
- **Security Decision:** DENY
- **Risk Score:** 100/100 (HIGH)
- **AI Agent Execution:** 5/5 successful

The generated six-page PDF report includes security indicators, AI-generated findings, recommended investigation actions, and audit information.

These results demonstrate simulated security-policy enforcement and AI-assisted investigation. They do not constitute production identity verification or real-world attack detection.

## Demonstration Links

- **Source Code:** https://github.com/JyothiSrinivasan/TrustMesh-AI
- **Frontend Preview:** https://trustmesh-ai.pages.dev
- **Video Demonstration:** Coming soon

**Deployment note:** The Cloudflare Pages deployment is a frontend preview. Full investigation functionality requires the local FastAPI backend, n8n workflows, Ollama model, and SQLite environment.

---

## Author

**Jyothi Srinivasan**

GitHub: https://github.com/JyothiSrinivasan

Developed as an individual project for **INNOVEX 2026 — PS 05: AI-Powered Cybersecurity**.
