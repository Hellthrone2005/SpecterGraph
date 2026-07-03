import networkx as nx
from colorama import Fore

class IdentityGraphEngine:
    def __init__(self):
        self.G = nx.DiGraph()

    def assemble_directory_graph(self, data):
        """Builds an interactive, fault-tolerant directed structural network graph map."""
        print(f"{Fore.MAGENTA}[*] Graph Core Active. Building directed structural nodes and topological map...")

        # 1. Ingest User Nodes safely using fault-tolerant fallbacks
        for user in data.get("users", []):
            user_id = user["id"]
            # Fall back to 'name' or a generic label if 'display_name' is missing
            display = user.get("display_name", user.get("name", user_id))
            self.G.add_node(user_id, name=user.get("name", user_id), label=display, type="user")

        # 2. Ingest Service Principal Nodes
        for sp in data.get("service_principals", []):
            sp_id = sp["id"]
            display = sp.get("display_name", sp.get("name", sp_id))
            self.G.add_node(sp_id, name=sp.get("name", sp_id), label=display, type="service_principal")

        # 3. Ingest Group Nodes
        for group in data.get("groups", []):
            group_id = group["id"]
            self.G.add_node(group_id, name=group.get("name", group_id), type="group")

        # 4. Ingest High-Value Asset Boundaries
        for asset in data.get("assets", []):
            asset_id = asset["id"]
            self.G.add_node(asset_id, name=asset.get("name", asset_id), type="asset")

        # 5. Build Dynamic Relationship Edges (Connections)
        # Establish Group Memberships
        for group in data.get("groups", []):
            group_id = group["id"]
            for member_id in group.get("direct_members", []):
                # Edge points from Member ➔ Group to represent upstream path traversal flow
                self.G.add_edge(member_id, group_id)

        # Establish Service Principal Overlaps
        for sp in data.get("service_principals", []):
            sp_id = sp["id"]
            for member_id in sp.get("direct_members", []):
                self.G.add_edge(member_id, sp_id)

        # Establish Asset Governance Controls
        for asset in data.get("assets", []):
            asset_id = asset["id"]
            governing_group = asset.get("controlled_by_group")
            if governing_group:
                self.G.add_edge(governing_group, asset_id)

        print(f"{Fore.GREEN}[+] Graph assembly completed successfully.")
        print(f" └── Total Structural Nodes: {self.G.number_of_nodes()} | Topological Edges: {self.G.number_of_edges()}")
        
        return self.G