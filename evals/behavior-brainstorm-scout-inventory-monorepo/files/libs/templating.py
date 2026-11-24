"""Render a message template from a service's message_templates/ folder."""
from pathlib import Path
from string import Template


def render(service_dir, name, values):
    text = (Path(service_dir) / "message_templates" / name).read_text(encoding="utf-8")
    return Template(text).safe_substitute(values)
