# TrustMesh AI — Agentic Zero Trust Security Platform

**Hackathon:** INNOVEX 2026  
**Developer:** Jyothi Srinivasan  
**Category:** Digital Security / AI-Powered Cybersecurity

## Project Overview

TrustMesh AI is an AI-powered Zero Trust cybersecurity platform that evaluates access requests using contextual risk scoring, multi-agent intelligence, and automated security decisions.

Instead of trusting users based solely on successful authentication, TrustMesh AI continuously evaluates identity, device trust, behavioral indicators, and security policies before determining whether access should be allowed, challenged, or denied.

The platform combines deterministic security enforcement with AI-powered investigation, making access decisions explainable, auditable, and responsive to potential threats.

## Problem Statement

Traditional access-control systems often rely heavily on credentials and static security rules. However, valid credentials do not necessarily guarantee that an access request is safe.

Compromised accounts, unfamiliar devices, suspicious login patterns, and abnormal user behavior can create significant security risks.

Organizations need an intelligent approach that considers multiple risk signals, explains suspicious activity, and supports appropriate access-control decisions.

## Proposed Solution

TrustMesh AI addresses this challenge through five specialized AI security agents:

1. **Identity Intelligence Agent:** Evaluates identity-related risk indicators.
2. **Device & Context Agent:** Assesses device trust and access context.
3. **Behavioral Threat Agent:** Investigates unusual login patterns and behavioral anomalies.
4. **Policy Decision Agent:** Provides policy-related analysis and recommendations.
5. **Security Response Agent:** Generates incident explanations and recommended security actions.

A deterministic risk engine calculates the risk score and enforces the final access decision. AI agents provide supporting analysis rather than independently overriding security policy.

## Key Features

- Five AI-powered security investigation agents
- Context-aware Zero Trust risk assessment
- Automated ALLOW, CHALLENGE, and DENY decisions
- Interactive 3D Digital Trust Twin
- Visual threat investigation workflow
- Security incident history
- Downloadable PDF investigation reports
- Local LLM inference for AI-assisted security analysis

## Technology Stack

**Frontend:** React, Vite, Three.js  
**Backend:** Python, FastAPI  
**AI & Automation:** n8n, Ollama, Qwen2.5  
**Database:** SQLite  
**Architecture:** Multi-agent orchestration with deterministic policy enforcement

## Demonstration Scenarios

| Scenario | Risk Score | Security Decision |
|---|---|---|
| Trusted identity and recognized device | 0/100 | ALLOW |
| Access from an untrusted device | 40/100 | CHALLENGE |
| Suspicious login behavior | 100/100 | DENY |

These scenarios demonstrate how TrustMesh AI responds differently based on contextual security risk.

## Innovation and Technical Differentiation

TrustMesh AI combines five specialized AI investigation workflows with a deterministic security decision engine.

Its distinctive capabilities include:

- Separation of AI-generated recommendations from authoritative access decisions
- Multi-agent investigation across identity, device, behavior, policy, and response
- Explainable security decisions supported by incident evidence
- Interactive visualization of security events through a 3D Digital Trust Twin
- Local AI inference without requiring a paid cloud LLM API

## Performance

During local testing, TrustMesh AI completed five-agent investigations in 5.80, 9.86, and 8.17 seconds, averaging approximately 7.94 seconds.

These measurements demonstrate the prototype's ability to complete investigations within a practical timeframe for an interactive demonstration.

## Potential Real-World Applications

TrustMesh AI could be extended for enterprise identity security, financial institutions, privileged-access monitoring, security operations centers, and Zero Trust access management.

The current implementation is a functional prototype using demonstration scenarios, not a production-certified access-control system.

## Project Links

**GitHub Repository:**  
https://github.com/JyothiSrinivasan/TrustMesh-AI

**Video Demonstration:**  
https://youtu.be/-mjXR60YCRQ

**Developed by:** Jyothi Srinivasan  
**Submitted for:** INNOVEX 2026
