import { FileDown } from "lucide-react";
import { useEffect, useState, useCallback } from "react";
import { Canvas } from "@react-three/fiber";
import { OrbitControls, Html, Line, Stars } from "@react-three/drei";
import {
  Shield, ShieldAlert, Activity, BrainCircuit,
  Database, Play, RefreshCw, Lock, CheckCircle2
} from "lucide-react";
import "./App.css";
import IncidentStory from "./IncidentStory";

const AGENTS = [
  ["identity", "Identity Intelligence"],
  ["device", "Device & Context"],
  ["behavior", "Behavioral Threat"],
  ["policy", "Policy Decision"],
  ["response", "Security Response"],
];

const SCENARIOS = {
  normal: {
    title: "Trusted Employee",
    user_id: "alice",
    device_id: "laptop-01",
    resource_id: "finance-reports",
    user_role: "finance-admin",
    device_trusted: true,
    failed_login_attempts: 0,
    impossible_travel: false,
  },
  suspicious: {
    title: "Suspicious Login",
    user_id: "bob",
    device_id: "laptop-02",
    resource_id: "finance-reports",
    user_role: "employee",
    device_trusted: false,
    failed_login_attempts: 7,
    impossible_travel: true,
  },
  challenge: {
    title: "Untrusted Device",
    user_id: "charlie",
    device_id: "tablet-03",
    resource_id: "public-dashboard",
    user_role: "employee",
    device_trusted: false,
    failed_login_attempts: 0,
    impossible_travel: false,
  },
};

function Node({ position, label, color }) {
  return (
    <group position={position}>
      <mesh>
        <sphereGeometry args={[0.35, 32, 32]} />
        <meshStandardMaterial
          color={color}
          emissive={color}
          emissiveIntensity={0.7}
        />
      </mesh>
      <Html distanceFactor={12} position={[0, 0.65, 0]} center>
        <div className="node-label">{label}</div>
      </Html>
    </group>
  );
}

function TrustNetwork({ decision }) {
  const denied = decision === "DENY";
  const challenged = decision === "CHALLENGE";
  const linkColor = denied ? "#fb7185" : challenged ? "#fbbf24" : "#2dd4bf";

  return (
    <Canvas camera={{ position: [0, 2, 9], fov: 45 }}>
      <color attach="background" args={["#09121f"]} />
      <ambientLight intensity={0.7} />
      <pointLight position={[5, 5, 5]} intensity={35} />
      <Stars radius={60} depth={30} count={1200} factor={2} fade />

      <Node position={[-3, 0, 0]} label="IDENTITY" color="#38bdf8" />
      <Node position={[0, 1.6, 0]} label="DEVICE" color="#a78bfa" />
      <Node position={[3, 0, 0]} label="RESOURCE" color={linkColor} />
      <Node position={[0, -1.6, 0]} label="AI SECURITY" color="#2dd4bf" />

      <Line points={[[-3, 0, 0], [0, 1.6, 0], [3, 0, 0]]}
        color={linkColor} lineWidth={2} />
      <Line points={[[-3, 0, 0], [0, -1.6, 0], [3, 0, 0]]}
        color="#2dd4bf" lineWidth={1.5} />
      <Line points={[[0, -1.6, 0], [0, 1.6, 0]]}
        color="#a78bfa" lineWidth={1.5} />

      <OrbitControls enablePan={false} minDistance={5} maxDistance={14} />
    </Canvas>
  );
}

export default function App() {
  const [incidents, setIncidents] = useState([]);
  const [selected, setSelected] = useState(null);
  const [scenario, setScenario] = useState("suspicious");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [activePage, setActivePage] = useState("command");

  
  const loadIncidents = useCallback(async () => {
    try {
      const res = await fetch("/api/incidents");

      if (!res.ok) {
        throw new Error("Unable to load incidents");
      }

      const data = await res.json();
      const rows = data.incidents || [];

      setIncidents(rows);

      setSelected((current) =>
        rows.find((r) => r.id === current?.id) || rows[0] || null
      );

      setError("");
    } catch (err) {
      setError(err.message);
    }
  }, []);


  
  useEffect(() => {
    const timer = setTimeout(() => {
      void loadIncidents();
    }, 0);

    return () => clearTimeout(timer);
  }, [loadIncidents]);


  async function investigate() {
    setLoading(true);
    setError("");

    try {
      const payload = {
        user_id: SCENARIOS[scenario].user_id,
        device_id: SCENARIOS[scenario].device_id,
        resource_id: SCENARIOS[scenario].resource_id,
        user_role: SCENARIOS[scenario].user_role,
        device_trusted: SCENARIOS[scenario].device_trusted,
        failed_login_attempts: SCENARIOS[scenario].failed_login_attempts,
        impossible_travel: SCENARIOS[scenario].impossible_travel,
      };
      const res = await fetch("/api/investigate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      if (!res.ok) throw new Error(`Investigation failed: ${res.status}`);

      const result = await res.json();
      await loadIncidents();

      setSelected({
        id: result.incident_id,
        user_id: payload.user_id,
        device_id: payload.device_id,
        resource_id: payload.resource_id,
        decision: result.security.decision,
        risk_score: result.security.risk_score,
        risk_level: result.security.risk_level,
        reasons: result.security.reasons,
        agent_results: result.agents,
      });
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  const denied = incidents.filter(i => i.decision === "DENY").length;
  const allowed = incidents.filter(i => i.decision === "ALLOW").length;
  const risk = selected?.risk_score ?? 0;


  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand">
          <Shield size={28} />
          TrustMesh<span>AI</span>
        </div>

        <div className="sidebar-heading">
          SECURITY OPERATIONS
        </div>

        <button
          type="button"
          className={activePage === "command" ? "nav-active" : "nav-item"}
          onClick={() => setActivePage("command")}
        >
          <Activity size={18} /> Command Center
        </button>

        <button
          type="button"
          className={activePage === "agents" ? "nav-active" : "nav-item"}
          onClick={() => setActivePage("agents")}
        >
          <BrainCircuit size={18} /> AI Agent Network
        </button>

        <button
          type="button"
          className={activePage === "investigations" ? "nav-active" : "nav-item"}
          onClick={() => setActivePage("investigations")}
        >
          <ShieldAlert size={18} /> Threat Investigations
        </button>

        <button
          type="button"
          className={activePage === "database" ? "nav-active" : "nav-item"}
          onClick={() => setActivePage("database")}
        >
          <Database size={18} /> Incident Database
        </button>

        <div className="sidebar-footer">
          ZERO TRUST SECURITY ENGINE
          <br />
          LOCAL AI · FASTAPI · N8N
        </div>
      </aside>

      <main className="main-content">
        {activePage === "command" && (
          <>
        <header className="topbar">
          <div>
            <div className="eyebrow">SECURITY INTELLIGENCE / OVERVIEW</div>
            <h1>Digital Trust Command Center</h1>
            <p>Multi-agent identity, device and access security monitoring</p>
          </div>
          <div className="system-status"><span className="status-dot" /> SYSTEM ONLINE</div>
        </header>

        <section className="stats-grid">
          <div className="stat-card"><span>Total Investigations</span><strong>{incidents.length}</strong><small>Recorded security events</small></div>
          <div className="stat-card"><span>Blocked Attempts</span><strong className="danger">{denied}</strong><small>Denied by policy engine</small></div>
          <div className="stat-card"><span>Allowed Requests</span><strong className="success">{allowed}</strong><small>Approved by policy engine</small></div>
          <div className="stat-card"><span>Current Risk Score</span><strong>{risk}<small> / 100</small></strong><small>Selected investigation</small></div>
        </section>

        <section className="main-grid">
          <div className="panel network-panel">
            <div className="panel-title"><span><Lock size={18} /> DIGITAL TRUST TWIN</span><small>DRAG TO ROTATE · SCROLL TO ZOOM</small></div>
            <div className="network-canvas">
              <TrustNetwork decision={selected?.decision} />
            </div>
            <div className="network-footer">
              <span>IDENTITY → DEVICE → RESOURCE</span>
              <span className={selected?.decision === "DENY" ? "danger" : "success"}>
                {selected?.decision || "AWAITING EVALUATION"}
              </span>
            </div>
          </div>

          <div className="panel simulation-panel">
            <div className="panel-title"><span><Play size={18} /> ATTACK SIMULATION</span></div>
            <p>Choose a scenario and launch a real five-agent investigation.</p>
            <label>SECURITY SCENARIO</label>
            <select value={scenario} onChange={e => setScenario(e.target.value)}>
              {Object.entries(SCENARIOS).map(([key, value]) =>
                <option key={key} value={key}>{value.title}</option>
              )}
            </select>
            <div className="scenario-info">
              <div><span>User</span><b>{SCENARIOS[scenario].user_id}</b></div>
              <div><span>Device</span><b>{SCENARIOS[scenario].device_id}</b></div>
              <div><span>Resource</span><b>{SCENARIOS[scenario].resource_id}</b></div>
            </div>
            <button className="primary-btn" disabled={loading} onClick={investigate}>
              <Play size={17} /> {loading ? "AI AGENTS INVESTIGATING..." : "LAUNCH INVESTIGATION"}
            </button>
            {error && <div className="error">{error}</div>}
            <div className="decision-box">
              <span>POLICY DECISION</span>
              <strong className={selected?.decision === "DENY" ? "danger" : "success"}>
                {selected?.decision || "PENDING"}
              </strong>
              <small>Risk: {risk}/100 · {selected?.risk_level || "N/A"}</small>
            </div>
          </div>
        </section>

        <section className="panel story-panel">
        <IncidentStory
          key={selected?.id ?? "empty"}
          incident={selected}
        />
        {selected && (
          <a
            className="report-download"
            href={`/api/incidents/${selected.id}/report`}
            download={`TrustMesh_Incident_${selected.id}.pdf`}
          >
            <FileDown size={18} />
            Download PDF Investigation Report
          </a>
        )}
        </section>


        <section className="bottom-grid">
          <div className="panel">
            <div className="panel-title"><span><BrainCircuit size={18} /> AI AGENT INTELLIGENCE</span></div>
            <div className="agent-list">
              {AGENTS.map(([key, name]) => {
                const agent = selected?.agent_results?.[key];
                return (
                  <details key={key} className="agent-card">
                    <summary>
                      <span><CheckCircle2 size={17} /> {name}</span>
                      <small>{agent?.status || "Waiting"}</small>
                    </summary>
                    <div className="agent-analysis">
                      {agent?.analysis || agent?.message || "No investigation results yet."}
                    </div>
                  </details>
                );
              })}
            </div>
          </div>

          <div className="panel">
            <div className="panel-title">
              <span><Database size={18} /> INCIDENT HISTORY</span>
              <button className="icon-btn" onClick={loadIncidents}><RefreshCw size={16} /></button>
            </div>
            <div className="incident-list">
              {incidents.length === 0 && <p>No incidents recorded yet.</p>}
              {incidents.map(item => (
                <button
                  key={item.id}
                  className={`incident-row ${selected?.id === item.id ? "selected" : ""}`}
                  onClick={() => setSelected(item)}
                >
                  <span><b>INC-{String(item.id).padStart(4, "0")}</b><small>{item.user_id} · {item.device_id}</small></span>
                  <span className={item.decision === "DENY" ? "danger" : "success"}>{item.decision}</span>
                  <span>{item.risk_score}/100</span>
                </button>
              ))}
            </div>
          </div>
        </section>
        </>
      )}

{activePage === "agents" && (
  <div className="page-content">
    <h1>AI Agent Network</h1>
    <p>Live investigation intelligence from five AI security agents.</p>

    <div className="agent-list">
      {AGENTS.map(([key, name]) => {
        const agent = selected?.agent_results?.[key];

        return (
          <details key={key} className="agent-card">
            <summary>
              <span>
                <BrainCircuit size={18} /> {name}
              </span>
              <small>{agent?.status || "Waiting"}</small>
            </summary>

            <div className="agent-analysis">
              {agent?.analysis ||
                agent?.message ||
                "Run an investigation to view agent findings."}
            </div>
          </details>
        );
      })}
    </div>
  </div>
)}

{activePage === "investigations" && (
  <div className="page-content">
    <h1>Threat Investigations</h1>
    <p>Review security incidents and AI investigation findings.</p>

    {selected ? (
      <>
        <IncidentStory
          key={selected.id}
          incident={selected}
        />

        <a
          className="report-download"
          href={`/api/incidents/${selected.id}/report`}
          download={`TrustMesh_Incident_${selected.id}.pdf`}
        >
          <FileDown size={18} />
          Download PDF Investigation Report
        </a>
      </>
    ) : (
      <p>No investigation selected yet.</p>
    )}
  </div>
)}

{activePage === "database" && (
  <div className="page-content">
    <h1>Incident Database</h1>
    <p>Security investigation history stored in SQLite.</p>

    <button
      className="primary-btn"
      onClick={loadIncidents}
    >
      <RefreshCw size={17} />
      Refresh Incidents
    </button>

    <div className="incident-list">
      {incidents.length === 0 && <p>No incidents recorded yet.</p>}

      {incidents.map((item) => (
        <button
          key={item.id}
          className={`incident-row ${
            selected?.id === item.id ? "selected" : ""
          }`}
          onClick={() => {
            setSelected(item);
            setActivePage("investigations");
          }}
        >
          <span>
            <b>INC-{String(item.id).padStart(4, "0")}</b>
            <small>{item.user_id} · {item.device_id}</small>
          </span>

          <span>{item.decision}</span>
          <span>{item.risk_score}/100</span>
        </button>
      ))}
    </div>
  </div>
)}

      </main>
    </div>
  );
}