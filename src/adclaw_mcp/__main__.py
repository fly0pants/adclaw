"""Entry point for `python -m adclaw_mcp` and `adclaw-mcp` CLI."""

from adclaw_mcp.server import mcp_server


def main():
    mcp_server.run(transport="stdio")


if __name__ == "__main__":
    main()
