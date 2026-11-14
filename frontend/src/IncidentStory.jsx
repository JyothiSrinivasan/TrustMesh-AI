
import { useEffect, useState } from "react";
import {
  UserRound,
  Laptop,
  Activity,
  ShieldAlert,
  BrainCircuit,
  CheckCircle2
} from "lucide-react";

const STAGES = [
  {
    title: "Access Request",
    icon: UserRound,
    description: "An identity requests access to a protected resource."
  },
  {
    title: "Device Verification",
    icon: Laptop,
    description: "Device trust and access context are evaluated."
  },
  {
    title: "Behavior Analysis",
    icon: Activity,
    description: "Suspicious login and travel indicators are assessed."
  },
  {
    title: "Policy Decision",
    icon: ShieldAlert,
    description: "The security engine determines the access decision."
  },
  {
    title: "AI Investigation",
    icon: BrainCircuit,
    description: "Five AI agents provide analysis and recommendations."
  }
];

export default function IncidentStory({ incident }) {
  const [active, setActive] = useState(-1);

  useEffect(() => {
    if (!incident) return;

    const timers = STAGES.map((_, index) =>
      setTimeout(() => setActive(index), (index + 1) * 850)
    );

    return () => timers.forEach(clearTimeout);
  }, [incident]);

  if (!incident) return null;

  return (
    <div className="story-container">
      <div className="story-header">
        <span>INCIDENT INVESTIGATION STORY</span>
        <strong>INC-{String(incident.id).padStart(4, "0")}</strong>
      </div>

      <div className="story-steps">
        {STAGES.map((stage, index) => {
          const Icon = stage.icon;
          const completed = active >= index;

          return (
            <div
              key={stage.title}
              className={`story-step ${completed ? "completed" : ""}`}
            >
              <div className="story-icon">
                {completed ? <CheckCircle2 size={18} /> : <Icon size={18} />}
              </div>
              <div>
                <strong>{stage.title}</strong>
                <p>{stage.description}</p>
              </div>
            </div>
          );
        })}
      </div>

      <div className="story-result">
        <span>FINAL SECURITY DECISION</span>
        <strong className={`decision-${incident.decision.toLowerCase()}`}>
            {incident.decision}
        </strong>
        <small>Risk Score: {incident.risk_score}/100</small>
      </div>
    </div>
  );
}
