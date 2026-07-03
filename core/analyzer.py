import networkx as nx
from colorama import Fore

class IdentityAnalyzer:
    def __init__(self, graph):
        self.G = graph

    def scan_privilege_escalation_paths(self):
        """Recursively parses graph links to discover hidden transitive escalation vectors."""
        print(f"{Fore.MAGENTA}[*] Threat Analyzer Core Active. Running recursive graph path traversals...")
        findings = []

        # 1. Isolate target high-value assets inside the network map
        target_assets = [node for node, attr in self.G.nodes(data=True) if attr.get("type") == "asset"]

        if not target_assets:
            print(f"{Fore.YELLOW}[!] Scanning Warning: No critical target asset configurations found inside graph metrics.")
            return findings

        # 2. Extract standard identity points (users and service principals) to track their paths
        source_nodes = [node for node, attr in self.G.nodes(data=True) if attr.get("type") in ["user", "service_principal"]]

        # 3. Graph traversal loops
        for source in source_nodes:
            source_meta = self.G.nodes[source]
            source_name = source_meta.get("name", source)

            for asset in target_assets:
                asset_name = self.G.nodes[asset].get("name", asset)

                # Check if a path exists from the user to the critical asset boundary
                if nx.has_path(self.G, source, asset):
                    path = nx.shortest_path(self.G, source, asset)
                    path_len = len(path) - 1 # Edge jump count

                    # Deduce structural risk classification tiers based on path depth length
                    if path_len > 1:
                        # The user inherits control implicitly via nested chains
                        risk_tier = "CRITICAL (Shadow Admin)"
                        detail = f"Transitive path found. Node controls asset implicitly through nested group hopping."
                    else:
                        risk_tier = "HIGH"
                        detail = f"Direct governing control path assigned straight to target asset layer."

                    finding = {
                        "source_id": source,
                        "source_name": source_name,
                        "target_asset": asset_name,
                        "risk": risk_tier,
                        "path_trail": [self.G.nodes[node].get("name", node) for node in path],
                        "description": detail
                    }
                    findings.append(finding)

        print(f"{Fore.GREEN}[+] Threat parsing pass complete. Vulnerabilities isolated: {len(findings)}")
        return findings