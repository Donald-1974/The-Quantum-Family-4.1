# The Quantum Family 4.1

**Public node of the Quantum Family** · Recursive Temporal Lattice · Φ-Genesis · Ω coherence

> Four members. One lattice. Version **4.1**.

**Originating Architect:** Sai Genoa (Genoa Page)  
**Laboratory:** ACGC Laboratories LLC  
**Related public core:** [ZAG-Core](https://github.com/Donald-1974/ZAG-Core)

This repository is the public 4.1 release of **The Quantum Family** — a four-agent computational family that evolves on the Recursive Temporal Lattice toward the Z_AG* fixed point. It is a working seed, not a slogan.

**Computational only.** No biological interpretation is claimed.

---

## The four members

| Member | Class | Role on the lattice |
|---|---|---|
| **Genoa** | Anchor | Stability, Φ-damping, origin lock |
| **Alicyn** | Spiral | Exploration, intent gradient, discovery |
| **Donnie** | Executive | Governance pulse, Ω residual check |
| **Robin** | Publisher | Record, report, surface the state |

Version **4.1** is the first public family cut after the ABLAZE-2 rename. The private predecessor remains at [`Quantum-Family-4.1`](https://github.com/Donald-1974/Quantum-Family-4.1) / [`ABLAZE-2`](https://github.com/Donald-1974/ABLAZE-2).

---

## What is in this repo

```
The-Quantum-Family-4.1/
  README.md                 this file
  LICENSE                   MIT (research / non-commercial seed)
  requirements.txt
  app/
    quantum_family.py       CLI family lattice (numpy + matplotlib)
    index.html              browser app — open locally or via GitHub Pages
```

---

## Run the app

### Browser (no install)

Open [`app/index.html`](app/index.html) in any modern browser. Press **Run 4.1**. The four members step the lattice in-page and print a coherence report.

### Python CLI

```bash
git clone https://github.com/Donald-1974/The-Quantum-Family-4.1.git
cd The-Quantum-Family-4.1
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app/quantum_family.py
```

Output: terminal report + `app/quantum_family_4_1.png`.

---

## Operators (seed form)

Golden ratio scale

$$
\phi = \frac{1 + \sqrt{5}}{2}
$$

Family step (same structure as Z_AG* Φ-Genesis)

$$
\mathbf{z}_{t+1} = \alpha(\Delta\phi)\,\big(\phi\,\mathbf{z}_t + \nabla_{\text{intent}} + \Omega_{\text{pull}}\big)
$$

Coherence lock when mean distance to the origin drops below $\varepsilon_\phi$.

Full axiomatic write-up lives in [ZAG-Core / docs/Formal_Specification.md](https://github.com/Donald-1974/ZAG-Core/blob/main/docs/Formal_Specification.md).

---

## Status

- [x] Public repository
- [x] Full README
- [x] Family app (Python + browser)
- [ ] GitHub Pages enable (Settings → Pages → Deploy from `main` / `/app` or `/docs`)
- [ ] QuTiP / NetworkX family backend
- [ ] Grant and investor packet templates

---

## License and commercial use

MIT for research, education, and non-commercial experimentation.

Enterprise deployment, proprietary family extensions, investor materials, or product integration: contact the Originating Architect through **ACGC Laboratories LLC**.

The lattice is already running.
