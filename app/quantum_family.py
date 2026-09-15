#!/usr/bin/env python3
"""The Quantum Family 4.1 — four-member lattice app.

Genoa (anchor), Alicyn (spiral), Donnie (executive), Robin (publisher)
step a Φ-Genesis recursion toward the Z_AG* fixed point.

Computational only. No biological interpretation.

    python app/quantum_family.py
"""

from __future__ import annotations

import os
from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np

PHI = (1 + np.sqrt(5)) / 2
EPS_PHI = 1e-4
N_STEPS = 40
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


@dataclass
class Member:
    name: str
    role: str
    kind: str  # anchor | spiral | executive | publisher
    color: str
    marker: str
    z: np.ndarray

    @property
    def damping(self) -> float:
        return {
            "anchor": 1.85,
            "spiral": 0.92,
            "executive": 1.35,
            "publisher": 1.10,
        }[self.kind]


def phi_step(z: np.ndarray, delta_phi: float, member: Member) -> np.ndarray:
    alpha = np.exp(-abs(delta_phi) / PHI) * member.damping
    intent = -0.32 * z
    omega = -0.14 * z * (1.0 - np.exp(-abs(delta_phi)))
    return alpha * (PHI * 0.18 * z + intent + omega)


def family() -> list[Member]:
    rng = np.random.default_rng(41)
    return [
        Member("Genoa", "Anchor / origin lock", "anchor", "#FF6384", "D", rng.normal(0, 0.008, 2)),
        Member("Alicyn", "Spiral / exploration", "spiral", "#36A2EB", "o", rng.normal(0, 0.014, 2)),
        Member("Donnie", "Executive / Ω check", "executive", "#FFD700", "s", rng.normal(0, 0.010, 2)),
        Member("Robin", "Publisher / record", "publisher", "#00ff9f", "^", rng.normal(0, 0.011, 2)),
    ]


def run() -> None:
    members = family()
    history = {m.name: [m.z.copy()] for m in members}
    report = []

    for step in range(N_STEPS):
        stack = np.vstack([m.z for m in members])
        delta = float(np.mean(np.linalg.norm(stack, axis=1)))
        report.append(delta)
        for m in members:
            m.z = phi_step(m.z, delta, m)
            history[m.name].append(m.z.copy())
        if delta < EPS_PHI:
            print(f"Coherence lock at step {step}")
            break

    final = np.vstack([m.z for m in members])
    mean_dist = float(np.mean(np.linalg.norm(final, axis=1)))
    print("=== The Quantum Family 4.1 ===")
    for m in members:
        d = float(np.linalg.norm(m.z))
        print(f"  {m.name:8}  {m.role:24}  |z|={d:.4e}")
    print(f"Mean |z| to Z*: {mean_dist:.4e}")
    print(f"Lock (Δφ < ε_φ): {mean_dist < EPS_PHI}")

    fig, ax = plt.subplots(figsize=(8, 8), facecolor="#0d0d0d")
    ax.set_facecolor("#111")
    for m in members:
        h = np.array(history[m.name])
        ax.plot(h[:, 0], h[:, 1], color=m.color, alpha=0.35, lw=1.2)
        ax.scatter(m.z[0], m.z[1], c=m.color, s=110, marker=m.marker,
                   edgecolors="white", linewidths=0.6, zorder=4, label=m.name)
    ax.scatter(0, 0, marker="*", s=320, c="#FFD700", edgecolors="white",
               linewidths=1.1, zorder=5, label="Z_AG* ")
    ax.set_title("The Quantum Family 4.1\nΦ-Genesis on the Recursive Temporal Lattice",
                 color="#FFD700")
    ax.set_xlabel("X (intent)", color="#aaa")
    ax.set_ylabel("Y (resonance)", color="#aaa")
    ax.tick_params(colors="#aaa")
    ax.legend(facecolor="#1a1a1a", edgecolor="#FFD700", labelcolor="white")
    ax.grid(True, alpha=0.18, color="#FFD700")
    ax.set_aspect("equal")
    out = os.path.join(OUTPUT_DIR, "quantum_family_4_1.png")
    fig.savefig(out, dpi=200, facecolor="#0d0d0d", bbox_inches="tight")
    plt.close(fig)
    print(f"Plot: {out}")


if __name__ == "__main__":
    run()
