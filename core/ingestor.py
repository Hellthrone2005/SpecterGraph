import json
import os
from colorama import Fore

class IdentityIngestor:
    def __init__(self, file_path=None):
        self.file_path = file_path if file_path else os.path.join("tests", "mock_tenant.json")

    def load_local_tenant_matrix(self):
        """Ingests and validates the offline identity architecture target matrix."""
        print(f"{Fore.MAGENTA}[*] Ingestion Core Active. Accessing storage repository: {self.file_path}")
        
        if not os.path.exists(self.file_path):
            print(f"{Fore.RED}[- ] Boot Error: Target file workspace path not found.")
            return None

        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                
            # Basic validation checks to ensure clean structural boundaries
            required_keys = ["users", "groups", "service_principals", "assets"]
            if not all(key in data for key in required_keys):
                print(f"{Fore.RED}[- ] Schema Error: Ingested file is missing required identity array keys.")
                return None

            print(f"{Fore.GREEN}[+] Ingestion complete. Ingested data footprint:")
            print(f"    └── Users: {len(data['users'])} | Groups: {len(data['groups'])} | Service Principals: {len(data['service_principals'])}")
            return data

        except json.JSONDecodeError:
            print(f"{Fore.RED}[- ] Parsing Error: The target data stream is corrupted or contains invalid JSON.")
            return None