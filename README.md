# NLP Path Planner

An A*-guided two-stage nonlinear trajectory optimization framework for
time-optimal holonomic robot navigation. Designed for FTC/FRC autonomous
path planning with hard obstacle-avoidance and actuator constraints.

## What It Does

Given a start pose, target pose, and a set of circular obstacles, this tool:

1. Runs an **A\* search** to find a collision-free geometric path.
2. Solves an **energy-minimizing NLP** with fixed time horizon as a warm start.
3. Solves a **time-optimal NLP** with smoothed L1 actuator constraints.
4. Produces a dynamically feasible trajectory (position, velocity, acceleration
   over time) that respects the robot's kinematic and actuator limits.

Obstacles are inflated in configuration space to account for the robot's
footprint and safety margin.

## Live App

Coming soon — hosted on Hugging Face Spaces.

## Running Locally

```bash
pip install -r requirements.txt
python app.py