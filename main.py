import sys
import os
from colorama import Fore, Style, init
from core.ingestor import IdentityIngestor
from core.graph_engine import IdentityGraphEngine
from core.analyzer import IdentityAnalyzer
from core.reporter import IdentityReporter
from core.mitigator import IdentityMitigator

# Initialize settings and console coloring filters
init(autoreset=True)

def load_env_natively(file_path=".env"):
    """Parses a local .env file manually to completely bypass external package dependencies."""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                # Skip comments and empty spaces
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, val = line.split("=", 1)
                os.environ[key.strip()] = val.strip()

def main():
    print(Fore.CYAN + "==================================================")
    print(Fore.CYAN + "🛡️  IDENTITY MISCONFIGURATION AUDITOR ENGINE CORE")
    print(Fore.CYAN + "==================================================\n")

    # Ingest runtime variables without external library dependencies
    load_env_natively()
    
    exec_mode = os.getenv("EXECUTION_MODE", "offline").lower()
    ingestor = IdentityIngestor()

    if exec_mode == "online":
        identity_data = ingestor.fetch_live_cloud_telemetry()
    else:
        identity_data = ingestor.load_local_tenant_matrix()

    if not identity_data:
        print(f"{Fore.RED}\n[-] Critical Core Fault: Failed to harvest identity dataset.")
        sys.exit(1)

    print(f"\n{Fore.CYAN}[*] Advancing to Phase 2: Directed Graph Conversion...")
    graph_builder = IdentityGraphEngine()
    directory_graph = graph_builder.assemble_directory_graph(identity_data)

    print(f"\n{Fore.CYAN}[*] Advancing to Phase 3: Recursive Threat Evaluation Loop...")
    analyzer = IdentityAnalyzer(directory_graph)
    vulnerabilities = analyzer.scan_privilege_escalation_paths()

    print(f"\n{Fore.CYAN}[*] Advancing to Phase 3.5: Compiling Remediation Playbooks...")
    mitigator = IdentityMitigator(vulnerabilities)
    remediations = mitigator.generate_remediation_strategies()

    print(f"\n{Fore.CYAN}[*] Advancing to Phase 4: Dynamic Dashboard Compiler Execution...")
    if vulnerabilities:
        reporter = IdentityReporter(vulnerabilities, remediations)
        reporter.compile_html_report()
        print(f"\n{Fore.GREEN}[+] Full remediation-aware engine loop finished cleanly!")
    else:
        print(f"\n{Fore.GREEN}[+] Graph audit finished clean.")

if __name__ == "__main__":
    main()