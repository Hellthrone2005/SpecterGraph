# 🔮 SpecterGraph v1.0.0

SpecterGraph is an advanced, automated defensive security engineering suite designed to audit identity perimeters and hunt down hidden **Transitive Privilege Escalation Paths (Shadow Admins)**. 

By modeling complex directory structures (Users, Groups, Service Principals, and High-Value Assets) into a mathematical directed graph, the engine maps out toxic access combinations and structural cycles that traditional linear scanners miss entirely.

---

## 🎨 System Canvas Telemetry
The framework features a responsive, custom **Black & Deep Purple Cyberpunk UI Dashboard** that outputs identified vulnerabilities alongside interactive multi-hop attack trails and dedicated remediation playbooks.

* **Topological Ingestion Core:** Evaluates structured entity relationships.
* **Dijkstra Path Traversal Engine:** Traces exact structural hop links to core target assets.
* **Dynamic Mitigator Pass:** Generates tailored, architectural fix blueprints per vector.

---

## 🛠️ Architecture Breakdown

The framework is decoupled into modular layers for production-grade maintenance:

```text
📁 SpecterGraph/
 ├── 📁 core/
 │    ├── 📄 ingestor.py      # Fault-tolerant telemetry harvester
 │    ├── 📄 graph_engine.py   # NetworkX directed graph model converter
 │    ├── 📄 analyzer.py       # Recursive path evaluation engine
 │    ├── 📄 mitigator.py      # Heuristic remediation blueprint compiler
 │    └── 📄 reporter.py       # Tailwind CSS UI dashboard compiler
 ├── 📁 tests/
 │    └── 📄 mock_tenant.json  # Stress-test data grid containing cyclical loops
 ├── 📄 main.py               # Central runtime coordinator
 └── 📄 .gitignore            # Local environment protection rules