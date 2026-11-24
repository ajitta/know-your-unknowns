"""Load a service's config.yaml into attribute access: settings.log_level."""
from pathlib import Path
from types import SimpleNamespace

import yaml

ROOT = Path(__file__).resolve().parent.parent


def load_settings(service):
    with open(ROOT / "services" / service / "config.yaml", encoding="utf-8") as handle:
        return SimpleNamespace(**yaml.safe_load(handle))
