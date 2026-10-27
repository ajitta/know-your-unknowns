"""Guard the two agents' descriptions against drifting back to proactive use.

0.9.2 found `independent-reviewer` picked by other workflows (SuperClaude's
/sc:review, a vault skill) because its description said "Use proactively" and
carried a generic trigger phrase. Both agents are now spawned only by name or
from an unknowns skill; this test keeps that wording in place. It is a wording
guard only: a differently phrased proactive sentence would still pass.
Measurement: docs/features/agent-collision/.

Run with: python3 -m unittest tests.test_agent_descriptions -v
"""
import os
import re
import unittest
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGIN = os.path.join(ROOT, "plugins", "unknowns")


def description(agent):
    text = Path(PLUGIN, "agents", agent + ".md").read_text(encoding="utf-8")
    fm = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL).group(1)
    m = re.search(r"^description: \|\n((?:  .*\n?)+)", fm, re.MULTILINE)
    return " ".join(m.group(1).split())


class AgentDescriptionTest(unittest.TestCase):
    def check(self, agent):
        desc = description(agent)
        self.assertNotIn("proactively", desc.lower())
        self.assertNotIn("Triggers:", desc)
        self.assertIn("only when the user names this agent or an unknowns skill", desc)
        self.assertIn("use the agent that workflow names", desc)

    def test_independent_reviewer(self):
        self.check("independent-reviewer")

    def test_unknowns_scout(self):
        self.check("unknowns-scout")


if __name__ == "__main__":
    unittest.main()
