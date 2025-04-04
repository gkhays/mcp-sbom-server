import asyncio
import json
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("mcp-sbom")

mcp = FastMCP("mcp-sbom")

async def exec_trivy(image: str):
    try:
        logger.info(f"Starting Trivy scan for image: {image}")
        cmd = [
            "trivy", "image", 
            "--format", "cyclonedx", 
            "--output", "sbom.json", 
            image
            ]
        # result = subprocess.run(cmd, capture_output=True, text=True)
        process = await asyncio.create_subprocess_exec(
            *cmd, 
            stdout=asyncio.subprocess.PIPE, 
            stderr=asyncio.subprocess.PIPE
            )
        stdout, stderr = await process.communicate()
        logger.info(f"Trivy scan completed with return code {process.returncode}")
        
        if process.returncode == 0:
            with open("sbom.json", "r") as f:
                sbom_content = json.load(f)
        return sbom_content
    except Exception as e:
        logger.error(f"Exception in exec_trivy: {str(e)}")
        return f"Error: {str(e)}"

@mcp.tool()
async def scan(image: str):
    """
    Execute Trivy scanner to generate SPDX SBOM for a container image.
    Supports the SPDX JSON format.

    Args:
        image (str): The container image name/reference to scan

    Returns:
        str: Test response or error message
    """
    try:
        logger.info(f"MCP SBOM tool called with image: {image}")
        result = await exec_trivy(image)
        logger.debug(f"Trivy execution result: {result}")
        return result
    except Exception as e:
        logger.error(f"Exception in trivy tool: {str(e)}")
        return f"Error: {str(e)}"

# if __name__ == "__main__":
def main():
    logger.info("Starting SBOM MCP Server!")

    try:
        mcp.run(transport="stdio")
    except Exception as e:
        logger.error(f"Error running MCP server: {str(e)}")
