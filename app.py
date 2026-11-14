from components.trust_twin import build_trust_twin
import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go


API_URL = "http://127.0.0.1:4861"

st.set_page_config(
    page_title="TrustMesh AI | Mission Control",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


st.markdown("""
<style>
/* MAIN PAGE */
.stApp,
[data-testid="stAppViewContainer"] {
    background: #254B60 !important;
    color: #EAF8FF !important;
}

/* TOP HEADER */
[data-testid="stHeader"] {
    background: #254B60 !important;
}

/* MAIN CONTENT */
.block-container {
    padding-top: 1.5rem;
    max-width: 1500px;
}

/* ALL HEADINGS */
h1, h2, h3, h4, h5, h6 {
    color: #FFFFFF !important;
}

/* NORMAL TEXT AND LABELS */
.stApp p,
.stApp label,
.stApp span,
.stApp small,
[data-testid="stWidgetLabel"],
[data-testid="stMetricLabel"],
[data-testid="stMetricValue"],
[data-testid="stCaptionContainer"] {
    color: #EAF8FF !important;
}

/* METRIC CARDS */
[data-testid="stMetric"] {
    background: #315B70 !important;
    border: 1px solid #5A91A5 !important;
    border-radius: 14px;
    padding: 20px;
}

[data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-size: 2rem !important;
    font-weight: 700 !important;
}

[data-testid="stMetricLabel"] {
    color: #C6F2FA !important;
}

/* BUTTONS */
div.stButton > button {
    background: #1D657B !important;
    color: #FFFFFF !important;
    border: 1px solid #48E0EA !important;
    border-radius: 10px;
    font-weight: 600;
}

div.stButton > button:hover {
    background: #287F95 !important;
    color: #FFFFFF !important;
}

/* INPUTS */
[data-baseweb="select"] > div {
    background: #EAF8FF !important;
    color: #183747 !important;
}

/* EXPANDERS */
[data-testid="stExpander"] {
    background: #315B70 !important;
    border: 1px solid #6D9FB1 !important;
    border-radius: 10px;
}

/* DIVIDERS */
hr {
    border-color: #6896A8 !important;
}

/* STATUS MESSAGES */
[data-testid="stAlert"] {
    border-radius: 10px;
}

/* ===== TRUSTMESH AI READABILITY FIX ===== */

/* Security Gateway notification */
[data-testid="stAlert"] {
    border-radius: 12px !important;
    border: 1px solid #6A9DAF !important;
}

/* Make text readable inside light status boxes */
[data-testid="stAlert"] p,
[data-testid="stAlert"] span,
[data-testid="stAlert"] div[data-testid="stMarkdownContainer"] {
    color: #173A4B !important;
    font-weight: 600 !important;
}

/* SUCCESS — soft mint background */
[data-testid="stAlert"][data-baseweb="notification"][kind="positive"],
[data-testid="stAlert"]:has([data-testid="stAlertContentSuccess"]) {
    background-color: #DDF7EE !important;
}

/* ERROR — soft pink background */
[data-testid="stAlert"][data-baseweb="notification"][kind="negative"],
[data-testid="stAlert"]:has([data-testid="stAlertContentError"]) {
    background-color: #FFE5E9 !important;
}

/* Improve evidence expander contrast */
[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary p,
[data-testid="stExpander"] summary span {
    color: #FFFFFF !important;
    font-weight: 600 !important;
}

/* Make captions easier to read */
[data-testid="stCaptionContainer"] p {
    color: #D5EDF4 !important;
}

/* Improve selectbox and other widget labels */
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] label {
    color: #F0FBFF !important;
}

/* Keep dropdown text dark on white */
[data-baseweb="select"] span,
[data-baseweb="select"] input {
    color: #173A4B !important;
}

/* ===== TRUSTMESH AI PREMIUM THEME ===== */

/* Page background */
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stHeader"] {
    background: #254B60 !important;
}

/* Clear, readable typography */
.stApp h1, .stApp h2, .stApp h3 {
    color: #F4FBFF !important;
}

[data-testid="stCaptionContainer"] p {
    color: #D0E9F2 !important;
}

/* Premium metric cards */
[data-testid="stMetric"] {
    background: linear-gradient(
        135deg, #315B70 0%, #294E65 100%
    ) !important;
    border: 1px solid #5D98AA !important;
    border-radius: 16px !important;
    padding: 22px !important;
    box-shadow: 0 6px 20px #102D3D30;
}

[data-testid="stMetric"]:hover {
    border-color: #48E0EA !important;
    box-shadow: 0 0 18px #48E0EA30;
}

[data-testid="stMetricValue"] {
    color: #FFFFFF !important;
    font-weight: 750 !important;
}

[data-testid="stMetricLabel"] p {
    color: #D7F1F8 !important;
}

/* Interactive buttons */
div.stButton > button {
    background: linear-gradient(
        120deg, #216D82, #285B79
    ) !important;
    color: #FFFFFF !important;
    border: 1px solid #48E0EA !important;
    border-radius: 12px !important;
    box-shadow: 0 0 12px #48E0EA18;
    transition: all 0.2s ease;
}

div.stButton > button:hover {
    background: #287F95 !important;
    box-shadow: 0 0 20px #48E0EA55;
}

/* Evidence panels */
[data-testid="stExpander"] {
    background: #2D566D !important;
    border: 1px solid #6C9EB0 !important;
    border-radius: 12px !important;
}

/* Preserve dark readable text on light alerts */
[data-testid="stAlert"] p,
[data-testid="stAlert"] span {
    color: #173A4B !important;
}

/* Section separators */
hr {
    border-color: #7099A9 !important;
    opacity: 0.65;
}


/* ===== TRUSTMESH AI EVIDENCE READABILITY FIX ===== */

/* Dark evidence panel instead of white */
[data-testid="stJson"] {
    background-color: #193C50 !important;
    border: 1px solid #5B91A5 !important;
    border-radius: 10px !important;
    padding: 14px !important;
}

/* JSON viewer text: readable on dark background */
[data-testid="stJson"] *,
[data-testid="stJson"] span,
[data-testid="stJson"] div {
    color: #F1FAFF !important;
}

/* Expander heading and arrow */
[data-testid="stExpander"] summary,
[data-testid="stExpander"] summary *,
[data-testid="stExpander"] summary p {
    color: #FFFFFF !important;
    background-color: #2D566D !important;
}

/* Ensure expanded panel stays dark */
[data-testid="stExpander"] > details,
[data-testid="stExpander"] details,
[data-testid="stExpander"] [data-testid="stExpanderDetails"] {
    background-color: #254B60 !important;
    color: #F1FAFF !important;
}

/* JSON syntax-highlighted values */
[data-testid="stJson"] .variable-value,
[data-testid="stJson"] .object-key-val {
    color: #E6F8FF !important;
}

</style>
""", unsafe_allow_html=True)



st.title("⬡ TRUSTMESH AI")
st.caption("THE FIFTH LAYER  |  ZERO-TRUST SECURITY MISSION CONTROL")

try:
    health = requests.get(f"{API_URL}/", timeout=3)
    health.raise_for_status()
    st.markdown(
    """
    <div style="
        display:inline-flex;
        align-items:center;
        gap:10px;
        background:#315B70;
        color:#FFFFFF;
        padding:10px 18px;
        border:1px solid #5A91A5;
        border-radius:10px;
        font-size:15px;
        font-weight:600;
        margin-bottom:12px;
    ">
        <span style="
            width:10px;
            height:10px;
            border-radius:50%;
            background:#48E0A4;
            box-shadow:0 0 10px #48E0A4;
        "></span>
        SECURITY GATEWAY ONLINE · PORT 4861
    </div>
    """,
    unsafe_allow_html=True
)
except requests.RequestException:
    st.error("Security Gateway Offline — start FastAPI on port 4861")

st.divider()

try:
    response = requests.get(f"{API_URL}/audit", timeout=3)
    response.raise_for_status()
    events = response.json()
except (requests.RequestException, ValueError):
    events = []

allowed = sum(e["decision"] == "ALLOW" for e in events)
denied = sum(e["decision"] == "DENY" for e in events)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Access Requests", len(events))
c2.metric("Authorized", allowed)
c3.metric("Blocked", denied)
c4.metric("AI Agents", "0 / 5", help="Agent integration is upcoming")

st.subheader("Digital Trust Twin")

# ===== LIVE SECURITY INVESTIGATION =====

st.subheader("Live Security Investigation")

try:
    response = requests.get(
        "http://127.0.0.1:4861/audit",
        timeout=5
    )
    response.raise_for_status()
    events = response.json()

    if events:
        latest = events[-1]

        decision = latest.get("decision", "UNKNOWN")
        user = latest.get("user_id", "Unknown")
        device = latest.get("device_id", "Unknown")
        resource = latest.get("resource_id", "Unknown")
        reason = latest.get("reason", "Not provided")

        st.markdown("### Latest Access Investigation")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Identity", user)

        with col2:
            st.metric("Device", device)

        with col3:
            st.metric("Decision", decision)

        st.write(f"**Requested Resource:** {resource}")
        st.write(f"**Policy Explanation:** {reason}")

        if decision == "DENY":
            st.error("Access blocked by Zero-Trust policy.")
        elif decision == "ALLOW":
            st.success("Access authorized by Zero-Trust policy.")
        else:
            st.warning(f"Access decision: {decision}")

        
        
        with st.expander("View Investigation Evidence"):
            import json
            import html

            evidence = json.dumps(latest, indent=4)

            st.markdown(
                f"""
                <div style="
                    background:#17394D;
                    color:#FFFFFF !important;
                    padding:20px;
                    border-radius:12px;
                    border:1px solid #5B91A5;
                    font-family:Consolas, monospace;
                    font-size:15px;
                    line-height:1.8;
                    white-space:pre-wrap;
                    overflow-wrap:anywhere;
                ">{html.escape(evidence)}</div>
                """,
                unsafe_allow_html=True
            )



    else:
        st.info("No security events available yet.")

except requests.RequestException as exc:
    st.warning(f"Investigation data unavailable: {exc}")


st.plotly_chart(
    build_trust_twin(events),
    use_container_width=True,
    key="trust_twin"
)
st.subheader("Access Security Simulation")

left, right = st.columns([1, 1.5])

with left:
    scenario = st.selectbox(
        "Select scenario",
        ["Trusted Employee", "Untrusted Device"]
    )

    if st.button("▶ Run Security Simulation", use_container_width=True):
        payload = (
            {
                "user_id": "alice",
                "device_id": "laptop-01",
                "resource_id": "finance-reports"
            }
            if scenario == "Trusted Employee"
            else {
                "user_id": "bob",
                "device_id": "laptop-02",
                "resource_id": "finance-reports"
            }
        )

        try:
            result = requests.post(
                f"{API_URL}/access/request",
                json=payload,
                timeout=5
            )
            data = result.json()
            event = data.get("detail", data)

            if result.status_code == 200:
                st.success(f"ACCESS ALLOWED — {event['reason']}")
            elif result.status_code == 403:
                st.error(f"ACCESS DENIED — {event['reason']}")
            else:
                st.warning(f"Unexpected response: {result.status_code}")
            st.rerun()
        except (requests.RequestException, ValueError, KeyError) as exc:
            st.error(f"Simulation failed: {exc}")

with right:
    fig = go.Figure()
    fig.add_trace(go.Indicator(
        mode="gauge+number",
        value=round(100 * allowed / len(events)) if events else 0,
        title={"text": "Authorized Access Rate (%)"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#20D6C7"},
            "bgcolor": "#315B70"
        }
    ))
    fig.update_layout(
        paper_bgcolor="#315B70",
        font_color="#E8F4FF",
        height=300,
        margin=dict(l=25, r=25, t=50, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)


st.subheader("Live Access Audit")

if events:
    for event in reversed(events[-20:]):
        decision = event.get("decision", "UNKNOWN")

        if decision == "ALLOW":
            st.success(
                f"🟢 ALLOWED | {event.get('user_id')} | "
                f"{event.get('resource_id')} | "
                f"{event.get('reason')}"
            )
        else:
            st.error(
                f"🔴 DENIED | {event.get('user_id')} | "
                f"{event.get('resource_id')} | "
                f"{event.get('reason')}"
            )

        
        with st.expander(f"View evidence — {event['event_id']}"):
            import json
            import html

            evidence = json.dumps(event, indent=4)

            st.markdown(
                f"""
                <div style="
                    background:#17394D;
                    color:#FFFFFF !important;
                    padding:20px;
                    border-radius:12px;
                    border:1px solid #5B91A5;
                    font-family:Consolas, monospace;
                    font-size:15px;
                    line-height:1.8;
                    white-space:pre-wrap;
                    overflow-wrap:anywhere;
                ">{html.escape(evidence)}</div>
                """,
                unsafe_allow_html=True
            )

else:
    st.info("No access events recorded yet.")
