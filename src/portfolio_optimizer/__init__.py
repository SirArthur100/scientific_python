from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("portfolio_optimizer")
except PackageNotFoundError:
    __version__ = "0.0"
