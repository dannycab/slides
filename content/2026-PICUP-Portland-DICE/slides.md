---
marp: true
paginate: true

title: PHY 321 — Classical Mechanics 1 at MSU
description: PICUP Portland DICE 2026 — Course overview with computing integration
author: Danny Caballero
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,600;1,300&family=JetBrains+Mono:wght@400&display=swap');

:root {
  --bg:       #F7F7F5;
  --text:     #1C1C1C;
  --accent:   #3D6B8E;
  --accent2:  #5E9E7E;
  --warm:     #C46E3A;
  --muted:    #767676;
  --code:     #E8E8E5;
  --rule:     #D0D0CC;
}

section {
  font-family: 'Inter', sans-serif;
  font-weight: 300;
  font-size: 1.35rem;
  line-height: 1.7;
  background: var(--bg);
  color: var(--text);
  padding: 52px 72px;
}

h1 {
  font-family: 'Inter', sans-serif;
  font-size: 2.8rem;
  font-weight: 700;
  color: var(--accent);
  border-bottom: 4px solid var(--accent);
  padding-bottom: 0.25em;
  margin-bottom: 0.5em;
}

h2 {
  font-size: 1.75rem;
  font-weight: 600;
  color: var(--accent2);
  margin-bottom: 0.45em;
}

h3 {
  font-size: 1.4rem;
  font-weight: 600;
  color: var(--accent);
  margin-bottom: 0.3em;
}

ul, ol {
  padding-left: 1.8em;
  margin: 0.6em 0;
}

li {
  margin-bottom: 0.65em;
  line-height: 1.6;
}

ul > li::marker {
  color: var(--accent);
  font-weight: 600;
}

strong {
  font-weight: 600;
  color: var(--accent);
}

em {
  font-style: normal;
  font-weight: 400;
  color: var(--warm);
}

code {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.85em;
  background: #E8E8E5;
  color: #2D5A4A;
  padding: 0.15em 0.5em;
  border-radius: 4px;
  font-weight: 500;
}

pre {
  background: #2A3D4A;
  padding: 1.2em 1.5em;
  border-radius: 6px;
  border-left: 5px solid var(--accent2);
  overflow-x: auto;
  margin: 0.5em 0;
}

pre code {
  background: none;
  padding: 0;
  font-size: 0.82em;
  color: #E8E8E5;
  font-weight: 400;
}

blockquote {
  border-left: 4px solid var(--accent2);
  margin: 0.8em 0 0;
  padding: 0.35em 1em;
  background: #EEF5F1;
  color: #2A4A3A;
  font-size: 0.95rem;
  border-radius: 0 4px 4px 0;
}

blockquote strong {
  color: var(--accent2);
}

table {
  border-collapse: collapse;
  width: 100%;
  font-size: 1.1rem;
  border: 2px solid var(--accent);
}

th {
  background: var(--accent);
  color: #F7F7F5;
  padding: 0.55em 1em;
  font-weight: 600;
  text-align: left;
  font-size: 1.05rem;
}

td {
  padding: 0.5em 1em;
  border-bottom: 1px solid var(--rule);
  color: var(--text);
}

tr:nth-child(even) td { background: #E8F0F7; }
tr:nth-child(odd) td  { background: #F7F7F5; }

section::after {
  font-size: 0.72rem;
  color: var(--muted);
  content: attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
}

section.title {
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 72px 80px;
  background: linear-gradient(135deg, var(--bg) 0%, #F0F3F7 100%);
}

section.title h1 {
  font-size: 3.2rem;
  color: var(--accent);
  border-bottom: 5px solid var(--accent);
  padding-bottom: 0.3em;
  margin-bottom: 0.3em;
  font-weight: 700;
}

section.title h2 {
  font-size: 1.6rem;
  color: var(--accent2);
  font-weight: 500;
  margin-bottom: 0.4em;
}

section.title p {
  color: var(--text);
  font-weight: 400;
  font-size: 1.1rem;
  margin-top: 0.6em;
}

.placeholder {
  border: 2px dashed var(--warm);
  border-radius: 6px;
  padding: 1em 1.4em;
  background: #FDF4EE;
  color: var(--warm);
  font-size: 1.1rem;
  margin-top: 0.8em;
}

.twocol {
  display: flex;
  flex-direction: row;
  gap: 2.5rem;
  align-items: flex-start;
}

.twocol > div {
  flex: 1;
  min-width: 0;
}

.pill {
  display: inline-block;
  background: var(--accent);
  color: #F7F7F5;
  font-size: 0.82rem;
  font-weight: 600;
  padding: 0.15em 0.7em;
  border-radius: 20px;
  margin-right: 0.4em;
  vertical-align: middle;
}

.pill.green {
  background: var(--accent2);
}

.pill.warm {
  background: var(--warm);
}
</style>

<!-- _class: title -->

# PHY 321: Classical Mechanics 1
## Michigan State University

Danny Caballero · PICUP Portland · June 2026

---

# PHY 321 at a Glance

<div class="twocol">
<div>

**Who takes it**
- 2nd–3rd year physics and astronomy majors
- ~100 students per year 
- Fall ((25-30) and Spring (65-75) semester offerings

**Prerequisites**
- Calculus sequence (MTH 132–133)
- Introductory physics (PHY 183–184)
- **CMSE 201** — Intro computational modeling

</div>
<div>

**Learning goals**

- Analyze forces, apply Newton's laws, and solve equations of motion *analytically and numerically*
- Understand conservation laws as universal principles
- Model nonlinear systems and identify stability
- Apply Lagrangian and Hamiltonian formulations
- Develop fluency with scientific computing

</div>
</div>

---

# Building on CMSE 201

<div class="placeholder">
&#x2190; Space to describe CMSE 201 here: what students learn, what tools they use (Python, NumPy, Matplotlib, Jupyter), and what conceptual framing is in place when they arrive in PHY 321.
</div>

**What I can build on from day one:**

- Students arrive knowing how to write and run Python code
- Familiarity with Jupyter notebooks as a working environment
- Experience with arrays and basic plotting
- Some exposure to numerical methods (what to add specifics here)

> The question is not *whether* to compute — it's *what physics* we can reach with computing that we couldn't reach otherwise.

---

# Course Philosophy

Classical Mechanics is the physics of **large, slow, mechanical systems** — but it's also a course about *how physicists think*.

For every system, we ask:

1. **Analytical** — Can we find a closed-form solution?
2. **Numerical** — Can we evolve the system forward in time?
3. **Geometric** — What does the phase space tell us?

<br>

> **Numerical methods are real physics.** A simulation of a driven pendulum reveals chaos. An energy diagram reveals stability. Neither requires an analytic solution.

---

# How Computing is Integrated

Computing is not a separate track — it is *woven through every topic*.

<div class="twocol">
<div>

**Structure**
- Jupyter notebooks are the primary format for lecture notes, homeworks, and midterms
- Every week introduces a new numerical concept alongside the physics
- Students submit `.ipynb` files; code is graded as part of the solution

</div>
<div>

**Design principle**

Students use computation to:
- Solve equations they *can't* solve analytically
- Visualize behavior that equations alone don't reveal
- Build physical intuition through experimentation
- Check analytical results

</div>
</div>

---

# Numerical Methods Across the Course

| Topic | Numerical Method |
|---|---|
| Equations of motion | Euler, *Euler-Cromer*, Velocity-Verlet |
| Drag & nonlinear forces | Runge-Kutta 4 (RK4) |
| Work, energy integrals | Trapezoidal rule, Simpson's rule |
| Phase space & stability | Numerical ODE solvers, plotting |
| Driven oscillators & chaos | Long-time integration, Poincaré sections |
| Two-body / central force | Symplectic integrators |

<br>

> Students learn *why* methods fail — energy drift in Euler, step-size sensitivity — not just how to use them.

---

# Course Topics with Computing Woven In

**Part I — Foundations** *(Weeks 1–3)*
Newton's Laws → differential equations → numerical solution from day one

**Part II — Conservation Laws** *(Weeks 4–6)*
Work-energy, momentum, potential energy → energy conservation *verified* numerically

**Part III — Nonlinear Dynamics** *(Weeks 7–10)*
Harmonic oscillators → driven oscillators → *chaos discovered through simulation*

**Part IV — Variational Principles** *(Weeks 11–14)*
Calculus of variations → Lagrangian mechanics → Hamiltonian systems

<br>

<span class="pill">Python</span> <span class="pill green">NumPy</span> <span class="pill green">SciPy</span> <span class="pill warm">Matplotlib</span> used throughout

---

# Example: Projectile Motion with Drag

The canonical first computation: *what does air resistance actually do?*

```python
# Euler-Cromer integration — energy-conserving for oscillators
for i in range(1, N):
    v[i] = v[i-1] + (F(r[i-1], v[i-1]) / m) * dt   # update velocity first
    r[i] = r[i-1] + v[i] * dt                        # then position
```

**What students discover:**
- Analytical solution (no drag) vs. numerical solution (with drag): *they diverge immediately*
- Terminal velocity emerges naturally — not from a formula, from the simulation
- Step-size matters: *too large and energy isn't conserved*

> This is the moment students see that computing reveals physics, not just computes answers.

---

# Assessments

<div class="twocol">
<div>

**Weekly Homeworks (8 total)**
Mix of pencil-and-paper and computational problems. Students submit a single PDF — handwritten work scanned alongside notebook output.

**Midterm Projects (2)**
Longer investigations of a single physical system. Students choose among several options and must combine analysis and simulation.

</div>
<div>

**Final Project**
Open-ended investigation with:
- Written essay
- Oral presentation
- Working simulation

Students choose their own system; past projects have included coupled oscillators, orbital mechanics, and chaotic billiards.

</div>
</div>

---

# What Students Can Do by the End

After PHY 321, students can:

- Set up a physical system from scratch and write a numerical solver for it
- Know when to trust (and distrust) a numerical solution
- Move fluidly between analytical, numerical, and geometric descriptions
- Read and write documented, reproducible scientific code

**The bigger goal:**

> They leave with a computational practice — not just computational skills. They know *how* to use computing as a thinking tool, not just a calculator.

