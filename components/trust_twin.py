
import plotly.graph_objects as go


def build_trust_twin(events):
    latest = events[-1] if events else {}
    decision = latest.get("decision", "IDLE")

    status_color = {
        "ALLOW": "#23E6BA",
        "DENY": "#FF5478",
        "IDLE": "#64748B",
    }[decision]

    nodes = {
        "Identity": (0.10, 0.76),
        "Device": (0.32, 0.76),
        "Zero-Trust Core": (0.52, 0.48),
        "Application": (0.78, 0.76),
        "Data Vault": (0.90, 0.28),
        "AI Agents": (0.20, 0.24),
    }

    links = [
        ("Identity", "Device"),
        ("Device", "Zero-Trust Core"),
        ("Zero-Trust Core", "Application"),
        ("Application", "Data Vault"),
        ("AI Agents", "Zero-Trust Core"),
    ]

    fig = go.Figure()

    # Draw glowing connections
    for start, end in links:
        x0, y0 = nodes[start]
        x1, y1 = nodes[end]

        color = (
            status_color
            if "Zero-Trust Core" in (start, end)
            and start != "AI Agents"
            else "#79B6CA"
        )

        fig.add_trace(go.Scatter(
            x=[x0, x1],
            y=[y0, y1],
            mode="lines",
            line=dict(color=color, width=5),
            opacity=0.15,
            hoverinfo="skip",
            showlegend=False,
        ))

        fig.add_trace(go.Scatter(
            x=[x0, x1],
            y=[y0, y1],
            mode="lines",
            line=dict(color=color, width=2),
            hoverinfo="skip",
            showlegend=False,
        ))

    
    # Soft holographic halos around network assets
    for name, (x, y) in nodes.items():
        is_core = name == "Zero-Trust Core"
        halo_color = status_color if is_core else "#48E0EA"

        fig.add_trace(go.Scatter(
            x=[x],
            y=[y],
            mode="markers",
            marker=dict(
                size=112 if is_core else 72,
                color=halo_color,
                opacity=0.10 if is_core else 0.07,
                line=dict(width=0),
            ),
            hoverinfo="skip",
            showlegend=False,
        ))

        if is_core:
            fig.add_trace(go.Scatter(
                x=[x],
                y=[y],
                mode="markers",
                marker=dict(
                    size=92,
                    color=halo_color,
                    opacity=0.16,
                    line=dict(width=0),
                ),
                hoverinfo="skip",
                showlegend=False,
            ))
    

    # Draw interactive network nodes
    for name, (x, y) in nodes.items():
        is_core = name == "Zero-Trust Core"

        fig.add_trace(go.Scatter(
            x=[x],
            y=[y],
            mode="markers+text",
            text=[name],
            textposition="bottom center",
            textfont=dict(size=15, color="#F4FBFF"),
            marker=dict(
                size=65 if is_core else 43,
                color="#234B62",
                line=dict(
                    color=status_color if is_core else "#31D9F4",
                    width=3,
                ),
            ),
            hovertemplate=(
                f"<b>{name}</b><br>"
                f"Latest decision: {decision}<extra></extra>"
            ),
            showlegend=False,
        ))

    fig.update_layout(
        title=dict(
            text="DIGITAL TRUST TWIN · LIVE NETWORK",
            font=dict(size=20, color="#F4FBFF"),
        ),
        paper_bgcolor="#1D3F55",
        plot_bgcolor="#1D3F55",
        height=540,
        margin=dict(l=15, r=15, t=65, b=20),
        xaxis=dict(
            range=[0, 1],
            visible=False,
            fixedrange=True,
        ),
        yaxis=dict(
            range=[0, 1],
            visible=False,
            fixedrange=True,
        ),
        showlegend=False,
        hovermode="closest",
    )

    return fig
