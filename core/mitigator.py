from colorama import Fore

class IdentityMitigator:
    def __init__(self, vulnerabilities):
        self.vulnerabilities = vulnerabilities

    def generate_remediation_strategies(self):
        """Analyzes path patterns to output precise tactical remediation blueprints."""
        print(f"{Fore.MAGENTA}[*] Mitigation Engine Active. Devising architectural fix strategies...")
        remediations = []

        for issue in self.vulnerabilities:
            path = issue["path_trail"]
            risk = issue["risk"]
            target = issue["target_asset"]
            source = issue["source_name"]

            # Strategy 1: Detect Cyclic / Inefficient Nesting
            if any("Cyclic" in node for node in path):
                action = "BREAK CYCLIC DEPENDENCY"
                steps = f"Remove cross-nested group loops between circular groups. Identity tracking is catching infinite loop traps."
                priority = "HIGH"
            
            # Strategy 2: Deep Nesting Chains (More than 2 steps away)
            elif len(path) > 3:
                action = "FLATTEN BOUNDARY DIRECTORIES"
                steps = f"Break nested path chain group links. Direct assignment or an isolated privilege group should replace multi-hop hierarchies."
                priority = "CRITICAL" if "CRITICAL" in risk else "MEDIUM"
                
            # Strategy 3: Standard Direct or Low Hop Access
            else:
                action = "ENFORCE LEAST PRIVILEGE / MFA"
                steps = f"Apply strict Conditional Access policies and Just-In-Time (JIT) scheduling to prevent persistent asset governing control."
                priority = "HIGH"

            remediations.append({
                "source_name": source,
                "target_asset": target,
                "action": action,
                "steps": steps,
                "priority": priority
            })

        print(f"{Fore.GREEN}[+] Remediation strategy matrices compiled successfully.")
        return remediations