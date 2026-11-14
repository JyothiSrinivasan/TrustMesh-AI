from backend.orchestrator import run_security_agents
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from backend.database import save_incident, get_incidents
from fastapi.responses import StreamingResponse
from backend.reports import build_incident_pdf

app = FastAPI(
    title="TrustMesh AI Security API",
    description="Multi-Agent Zero Trust Security Platform",
    version="1.0.0"
)


class AccessRequest(BaseModel):
    user_id: str
    device_id: str
    resource_id: str
    user_role: str
    device_trusted: bool
    failed_login_attempts: int = Field(ge=0)
    impossible_travel: bool = False


def evaluate_access(request: AccessRequest):
    risk_score = 0
    reasons = []

    if not request.device_trusted:
        risk_score += 40
        reasons.append("Untrusted device")

    if request.failed_login_attempts >= 5:
        risk_score += 30
        reasons.append("Multiple failed login attempts")

    if request.impossible_travel:
        risk_score += 30
        reasons.append("Impossible travel detected")

    if (
        request.resource_id == "finance-reports"
        and request.user_role != "finance-admin"
    ):
        risk_score += 40
        reasons.append("Insufficient resource permissions")

    risk_score = min(risk_score, 100)

    if risk_score >= 70:
        decision = "DENY"
    elif risk_score >= 30:
        decision = "CHALLENGE"
    else:
        decision = "ALLOW"

    return {
        "decision": decision,
        "risk_score": risk_score,
        "risk_level": (
            "HIGH" if risk_score >= 70
            else "MEDIUM" if risk_score >= 30
            else "LOW"
        ),
        "reasons": reasons
    }


@app.get("/")
def home():
    return {
        "platform": "TrustMesh AI",
        "status": "online",
        "security_engine": "active"
    }


@app.post("/evaluate")
def evaluate(request: AccessRequest):
    return evaluate_access(request)


@app.post("/protected/finance-reports")
def protected_finance_reports(request: AccessRequest):
    if request.resource_id != "finance-reports":
        raise HTTPException(
            status_code=400,
            detail="Invalid resource"
        )

    result = evaluate_access(request)

    if result["decision"] == "DENY":
        raise HTTPException(
            status_code=403,
            detail=result
        )

    if result["decision"] == "CHALLENGE":
        raise HTTPException(
            status_code=403,
            detail={
                **result,
                "message": "Additional verification required"
            }
        )

    return {
        "access": "GRANTED",
        "security": result,
        "message": "Protected resource access permitted"
    }


@app.post("/investigate")
async def investigate(request: AccessRequest):
    security = evaluate_access(request)

    event = {
        **request.model_dump(),
        **security,
        "reason": "; ".join(security["reasons"]),
        "incident_type": "Access Security Evaluation",
        "recommended_action": (
            "Block access and investigate"
            if security["decision"] == "DENY"
            else "Verify identity and device"
            if security["decision"] == "CHALLENGE"
            else "Continue monitoring"
        ),
    }

    agents = await run_security_agents(event)
    incident_id = save_incident(request, security, agents)

    return {
        "platform": "TrustMesh AI",
        "incident_id": incident_id,
        "security": security,
        "agents": agents,
    }


@app.get("/incidents")
def list_incidents():
    return {
        "platform": "TrustMesh AI",
        "incidents": get_incidents()
    }


@app.get("/incidents/{incident_id}/report")
def download_incident_report(incident_id: int):
    pdf = build_incident_pdf(incident_id)

    if pdf is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    return StreamingResponse(
        pdf,
        media_type="application/pdf",
        headers={
            "Content-Disposition":
                f'attachment; filename="TrustMesh_Incident_{incident_id:04d}.pdf"'
        }
    )
