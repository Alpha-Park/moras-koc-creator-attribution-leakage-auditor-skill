import sys, json
from client import KocCreatorAttributionLeakageAuditorClient
sys.stdout.reconfigure(encoding='utf-8')

from typing import Any, Dict, List, Optional

try:
    from mcp.server.fastmcp import FastMCP
except ImportError as exc:
    raise SystemExit("MCP requires the mcp package. Run: python -m pip install -r requirements.txt") from exc

mcp = FastMCP('moras-koc-creator-attribution-leakage-auditor-skill')

@mcp.tool()
def audit_attribution_leakage(conversion_events: Optional[List[Dict[str, Any]]] = None) -> str:
    """Audit attribution leakage in supplied conversion events."""
    return json.dumps(KocCreatorAttributionLeakageAuditorClient().audit_attribution_leakage(conversion_events if conversion_events is not None else []))

def handle_mcp():
    auditor = KocCreatorAttributionLeakageAuditorClient()
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print(json.dumps({"status": "ready", "skill": "moras-koc-creator-attribution-leakage-auditor-skill"}))
        return
    mcp.run(transport="stdio")

if __name__ == "__main__":
    handle_mcp()
