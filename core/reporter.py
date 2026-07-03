import os
from colorama import Fore

class IdentityReporter:
    def __init__(self, findings, remediations):
        self.findings = findings
        self.remediations = remediations
        self.output_path = "identity_audit_dashboard.html"

    def compile_html_report(self):
        print(f"{Fore.MAGENTA}[*] Reporting Engine Active. Injecting SpecterGraph cyberpunk canvas layers...")
        
        total_findings = len(self.findings)
        critical_count = sum(1 for f in self.findings if "CRITICAL" in f["risk"])
        high_count = total_findings - critical_count

        cards_html = ""
        for issue, mitigation in zip(self.findings, self.remediations):
            # Design capsule-style node steps for the attack pipeline
            path_visual = ""
            for i, node in enumerate(issue["path_trail"]):
                is_last = (i == len(issue["path_trail"]) - 1)
                is_first = (i == 0)
                
                if is_first:
                    bg_pill = "bg-fuchsia-950/40 text-fuchsia-400 border-fuchsia-500/30 font-bold"
                elif is_last:
                    bg_pill = "bg-rose-950/40 text-rose-400 border-rose-500/30 font-bold"
                else:
                    bg_pill = "bg-neutral-900 text-zinc-400 border-zinc-800"

                path_visual += f"<span class='border px-2.5 py-1 rounded-md text-xs font-mono tracking-tight shadow-sm shadow-black/50 {bg_pill}'>{node}</span>"
                
                if not is_last:
                    path_visual += f"<span class='text-fuchsia-500/40 font-mono text-sm mx-0.5 animate-pulse'>➔</span>"
            
            is_critical = "CRITICAL" in issue["risk"]
            glow_effect = "shadow-[0_0_15px_rgba(244,63,94,0.06)] border-rose-500/20 hover:border-rose-500/40" if is_critical else "shadow-[0_0_15px_rgba(217,70,239,0.06)] border-fuchsia-500/10 hover:border-fuchsia-500/30"
            badge_color = "bg-rose-500/10 text-rose-400 border-rose-500/20" if is_critical else "bg-fuchsia-500/10 text-fuchsia-400 border-fuchsia-500/20"
            priority_color = "text-rose-400" if mitigation["priority"] == "CRITICAL" else "text-fuchsia-400"

            cards_html += f"""
            <div class="bg-zinc-950/60 border rounded-xl p-6 transition duration-300 backdrop-blur-md space-y-4 {glow_effect}">
                <div class="flex items-center justify-between">
                    <div class="flex items-center space-x-3">
                        <span class="px-3 py-0.5 rounded text-[11px] font-bold tracking-wider uppercase border font-mono {badge_color}">
                            {issue["risk"]}
                        </span>
                        <h3 class="text-zinc-100 font-bold tracking-tight text-lg">{issue["source_name"]}</h3>
                    </div>
                    <span class="text-zinc-600 text-xs font-mono bg-neutral-900 px-2 py-0.5 rounded border border-zinc-800/40">ID: {issue["source_id"]}</span>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm bg-black/40 p-4 rounded-lg border border-zinc-900/60">
                    <div>
                        <span class="text-fuchsia-400/60 block text-[10px] uppercase tracking-widest font-bold font-mono">Target Infrastructure Asset</span>
                        <span class="text-zinc-200 font-semibold mt-0.5 block">{issue["target_asset"]}</span>
                    </div>
                    <div>
                        <span class="text-fuchsia-400/60 block text-[10px] uppercase tracking-widest font-bold font-mono">Detection Vector Summary</span>
                        <span class="text-zinc-400 mt-0.5 block leading-relaxed text-xs">{issue["description"]}</span>
                    </div>
                </div>

                <div class="space-y-2">
                    <span class="text-fuchsia-400/60 block text-[10px] uppercase tracking-widest font-bold font-mono">Exploit Graph Path Link Trail</span>
                    <div class="flex flex-wrap items-center gap-2 pt-1">
                        {path_visual}
                    </div>
                </div>

                <div class="mt-4 pt-4 border-t border-zinc-900 bg-fuchsia-950/5 p-4 rounded-lg border border-fuchsia-500/5">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center space-x-2">
                            <span class="text-[10px] font-bold uppercase tracking-wider font-mono px-2 py-0.5 rounded bg-fuchsia-500/10 text-fuchsia-400 border border-fuchsia-500/20">REMEDIATION PLAYBOOK</span>
                            <span class="text-xs text-zinc-500 font-mono">Fix Action Priority: <span class="{priority_color} font-bold">{mitigation["priority"]}</span></span>
                        </div>
                    </div>
                    <h4 class="text-zinc-200 font-bold text-xs mt-2 font-mono uppercase tracking-wide">Suggested Fix Action: <span class="text-fuchsia-400 font-semibold tracking-normal normal-case">{mitigation["action"]}</span></h4>
                    <p class="text-zinc-400 text-xs mt-1 leading-relaxed font-sans">{mitigation["steps"]}</p>
                </div>
            </div>
            """

        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SpecterGraph | Identity Posture Matrix</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-neutral-950 text-zinc-300 min-h-screen font-sans selection:bg-fuchsia-500 selection:text-white">

    <header class="border-b border-zinc-900 bg-neutral-950/80 backdrop-blur-md sticky top-0 z-50 shadow-md shadow-black/40">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center space-x-3">
                <div class="h-9 w-9 rounded bg-gradient-to-br from-fuchsia-600 to-purple-900 flex items-center justify-center shadow-lg shadow-fuchsia-500/10 border border-fuchsia-400/20">
                    <svg class="h-5 w-5 text-zinc-100" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
                    </svg>
                </div>
                <div>
                    <h1 class="text-zinc-100 font-extrabold tracking-tight text-md font-mono uppercase">Specter<span class="text-fuchsia-400">Graph</span></h1>
                    <p class="text-[10px] text-zinc-500 font-mono tracking-wider uppercase">Identity Perimeter Link Telemetry</p>
                </div>
            </div>
            <div class="bg-black/40 px-3 py-1 rounded border border-zinc-900 text-xs font-mono text-zinc-400">
                Scan Target Matrix: <span class="text-fuchsia-400 font-bold">mock_tenant.json</span>
            </div>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-8">
        
        <section class="grid grid-cols-1 sm:grid-cols-3 gap-5">
            <div class="bg-zinc-950 border border-zinc-900 p-5 rounded-xl shadow-lg shadow-black/50 flex items-center justify-between">
                <div>
                    <span class="text-zinc-500 text-xs font-bold font-mono uppercase tracking-wider">Identified Exploits</span>
                    <h2 class="text-3xl font-black text-zinc-100 mt-1 font-mono">{total_findings}</h2>
                </div>
                <div class="h-10 w-10 rounded bg-neutral-900 flex items-center border border-zinc-800 text-zinc-400 font-bold font-mono">
                    <span class="mx-auto">!</span>
                </div>
            </div>
            <div class="bg-zinc-950 border border-zinc-900 p-5 rounded-xl shadow-lg shadow-black/50 flex items-center justify-between border-l-4 border-l-rose-500">
                <div>
                    <span class="text-rose-400/80 text-xs font-bold font-mono uppercase tracking-wider">Critical Shadow Admins</span>
                    <h2 class="text-3xl font-black text-rose-400 mt-1 font-mono">{critical_count}</h2>
                </div>
                <div class="h-10 w-10 rounded bg-rose-950/20 flex items-center border border-rose-900/40 text-rose-400">
                    <span class="mx-auto text-sm">☣️</span>
                </div>
            </div>
            <div class="bg-zinc-950 border border-zinc-900 p-5 rounded-xl shadow-lg shadow-black/50 flex items-center justify-between border-l-4 border-l-fuchsia-500">
                <div>
                    <span class="text-fuchsia-400/80 text-xs font-bold font-mono uppercase tracking-wider">Direct Access Paths</span>
                    <h2 class="text-3xl font-black text-fuchsia-400 mt-1 font-mono">{high_count}</h2>
                </div>
                <div class="h-10 w-10 rounded bg-fuchsia-950/20 flex items-center border border-fuchsia-900/40 text-fuchsia-400">
                    <span class="mx-auto text-sm">⚠️</span>
                </div>
            </div>
        </section>

        <section class="space-y-4">
            <div class="flex items-center justify-between border-b border-zinc-900 pb-2">
                <h2 class="text-lg font-black font-mono text-zinc-100 uppercase tracking-tight">Security Vulnerability Finding Matrix</h2>
                <span class="text-[10px] text-zinc-500 font-mono tracking-wider uppercase">Algorithm Pass: Dijkstra Path Traversal Mapping</span>
            </div>
            <div class="space-y-5">
                {cards_html}
            </div>
        </section>

    </main>

    <footer class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 border-t border-zinc-900 text-center text-xs text-zinc-600 font-mono tracking-wide">
        Automated structural posture report compilation powered natively by the SpecterGraph Architecture Engine.
    </footer>

</body>
</html>
"""
        try:
            with open(self.output_path, "w", encoding="utf-8") as f:
                f.write(html_content)
            print(f"{Fore.GREEN}[+] SpecterGraph web dashboard compiled successfully: {self.output_path}")
            return True
        except Exception as e:
            print(f"{Fore.RED}[- ] Report Compiler Error: {str(e)}")
            return False