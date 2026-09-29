"""
Minimal Dash app for the NLP Path Planner.
Deploy this first to verify the hosting pipeline works.
"""

import math
import numpy as np
import plotly.graph_objects as go
from dash import Dash, dcc, html

# ==========================================
# CONFIGURATION
# ==========================================
W = 0.19
L = 0.175
r_ball = 0.0635
R_MAX = math.hypot(W, L)
R_SAFE = R_MAX + r_ball + 0.02

FIELD_MAX = 3.66

START_POSE = [W, L, -math.pi / 4]
TARGET_POSE = [3.0, 3.0, -math.pi / 4]

OBSTACLES = [
    [2.00, 2.00],
    [0.50, 1.00],
    [1.50, 1.00],
    [1.00, 1.50],
    [1.75, 2.25],
]

# ==========================================
# FIGURE BUILDER
# ==========================================
def build_figure():
    fig = go.Figure()

    # Field boundary
    fig.add_shape(
        type="rect", x0=0, y0=0, x1=FIELD_MAX, y1=FIELD_MAX,
        line=dict(color="black", width=2),
        fillcolor="rgba(245, 245, 245, 0.5)",
    )

    # Obstacles: safe zone + ball
    for ox, oy in OBSTACLES:
        fig.add_shape(
            type="circle",
            x0=ox - R_SAFE, y0=oy - R_SAFE,
            x1=ox + R_SAFE, y1=oy + R_SAFE,
            line=dict(color="red", width=1, dash="dot"),
            fillcolor="rgba(255, 0, 0, 0.08)",
        )
        fig.add_shape(
            type="circle",
            x0=ox - r_ball, y0=oy - r_ball,
            x1=ox + r_ball, y1=oy + r_ball,
            line=dict(color="darkred", width=1),
            fillcolor="rgba(255, 0, 0, 0.6)",
        )

    # Start
    fig.add_trace(go.Scatter(
        x=[START_POSE[0]], y=[START_POSE[1]],
        mode="markers+text",
        marker=dict(size=14, color="green"),
        text=["START"], textposition="top center",
        name="Start",
    ))

    # Goal
    fig.add_trace(go.Scatter(
        x=[TARGET_POSE[0]], y=[TARGET_POSE[1]],
        mode="markers+text",
        marker=dict(size=18, color="red", symbol="star"),
        text=["GOAL"], textposition="top center",
        name="Goal",
    ))

    fig.update_layout(
        xaxis=dict(range=[-0.3, FIELD_MAX + 0.3], title="X (m)",
                   scaleanchor="y", scaleratio=1),
        yaxis=dict(range=[-0.3, FIELD_MAX + 0.3], title="Y (m)"),
        width=700, height=700,
        margin=dict(l=40, r=40, t=40, b=40),
        showlegend=True,
    )
    return fig

# ==========================================
# APP
# ==========================================
app = Dash(__name__)
app.title = "NLP Path Planner"

app.layout = html.Div([
    html.H2("NLP Path Planner", style={"textAlign": "center"}),
    html.P("Field visualizer — solver integration coming next.",
           style={"textAlign": "center", "color": "gray"}),
    dcc.Graph(id="field", figure=build_figure()),
], style={"maxWidth": "800px", "margin": "0 auto"})

# Expose the Flask server for deployment platforms
server = app.server

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=7860)