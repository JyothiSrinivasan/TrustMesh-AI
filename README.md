# TrustMesh AI

### Multi-Agent Zero Trust Identity & Access Security Platform

**TrustMesh AI** is a working cybersecurity simulation platform that combines deterministic Zero Trust access-policy evaluation, five AI investigation agents, security automation, and an interactive 3D Digital Trust Twin.

Built for **INNOVEX 2026 — Digital Security / AI-Powered Cybersecurity**.

## Overview

TrustMesh AI demonstrates how AI-assisted security operations can help analysts investigate identity, device, and access-related risks while keeping authorization decisions under deterministic policy control.

The platform allows users to simulate access requests, evaluate security risks, visualize the investigation process, review AI-generated findings, and download incident investigation reports.

## Key Features

- **Zero Trust Policy Engine:** Evaluates simulated identity, device, resource, and behavioral signals to return ALLOW, CHALLENGE, or DENY.
- **Five AI Security Agents:** Investigate identity risk, device context, behavioral indicators, policy decisions, and security response.
- **3D Digital Trust Twin:** Interactive visualization of relationships between identities, devices, resources, and security analysis.
- **Attack Simulation Center:** Runs trusted-access, suspicious-login, and untrusted-device scenarios.
- **Incident Investigation Story:** Animated five-stage visualization of the investigation process.
- **Incident History:** Stores and retrieves investigations using SQLite.
- **PDF Investigation Reports:** Generates reports containing security decisions, risk indicators, and AI-agent findings.

## Five AI Security Agents

| Agent | Responsibility |
|---|---|
| Identity Intelligence | Analyzes identity and access-request context |
| Device & Context | Examines device trust and available context |
| Behavioral Threat | Evaluates suspicious login and behavioral indicators |
| Policy Decision | Explains the deterministic access-policy decision |
| Security Response & Audit | Recommends investigation, verification, and response actions |

The AI agents provide advisory analysis. They do not override the deterministic policy engine.

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
| Version Control | Git, GitHub |

## Architecture

```text
React Dashboard
       |
       v
FastAPI Backend
       |
       +---- Deterministic Security Policy Engine
       |               |
       |        ALLOW / CHALLENGE / DENY
       |
       +---- AI Agent Orchestrator
       |               |
       |               v
       |           n8n Workflows
       |               |
       |         Ollama Qwen2.5
       |               |
       |         Five AI Agents
       |
       +---- SQLite Incident Database
       |
       +---- PDF Investigation Reports
```

## Demonstration Scenarios

| Scenario | Decision | Risk Score |
|---|---|---|
| Trusted Employee | ALLOW | 0/100 |
| Untrusted Device | CHALLENGE | 40/100 |
| Suspicious Login | DENY | 100/100 |

These scenarios use predefined simulation inputs and rule-based risk scoring.

## Running Locally

### Requirements

- Python 3.11 or newer
- Node.js and npm
- Ollama with the `qwen2.5:3b` model
- n8n with the five configured TrustMesh AI workflows

### Backend setup

From the project root:

```bash
python -m venv .venv
```

Activate the virtual environment, then install dependencies:

```bash
pip install fastapi "uvicorn[standard]" httpx pydantic python-dotenv reportlab markdown
```

Start the backend:

```bash
python -m uvicorn backend.main:app --reload --port 7654
```

### Frontend setup

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`.

### AI services

Run Ollama with the Qwen2.5 model and start n8n on port `5679`.

Configure and publish the five workflows using these webhook paths:

- `/webhook/trustmesh-identity`
- `/webhook/trustmesh-device`
- `/webhook/trustmesh-behavior`
- `/webhook/trustmesh-policy`
- `/webhook/trustmesh-response`

**Note:** The n8n workflow definitions must be configured separately. The repository's application code alone does not reproduce the full AI-agent environment.

## Security Scope and Limitations

TrustMesh AI is a hackathon prototype and security simulation, not a production-ready identity and access management system.

- Identity, role, and device attributes are supplied as simulation inputs.
- Real identity verification, device attestation, and MFA enforcement are not implemented.
- Access-policy decisions are deterministic; AI analysis is advisory.
- AI-generated explanations may require human review.
- The project should not be used to protect real sensitive resources without further security engineering.

## Future Enhancements

- Verified authentication and role-based access control
- Keycloak integration for IAM and MFA
- Open Policy Agent for centralized policy management
- Wazuh integration for security telemetry
- AI-output validation and consistency checks
- Enterprise audit logging and monitoring

## Project Status

**Functional hackathon prototype:** Backend, AI orchestration, dashboard, security simulations, incident history, and PDF reporting implemented and locally tested.

## Author

**Jyothi Srinivasan**

GitHub: [JyothiSrinivasan](https://github.com/JyothiSrinivasan)

Developed as an AI-powered cybersecurity hackathon project.