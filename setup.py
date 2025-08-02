from setuptools import setup, find_packages

# Read the version from pyproject.toml
with open("pyproject.toml", "r") as f:
    for line in f:
        if line.startswith("version = "):
            version = line.split("=")[1].strip().strip('"')
            break

setup(
    name="atomic-mcp",
    version=version,
    packages=find_packages(where="atomic-mcp"),
    package_dir={"atomic_mcp": "atomic-mcp/atomic_mcp"},
    include_package_data=True,
    python_requires=">=3.12",
)
