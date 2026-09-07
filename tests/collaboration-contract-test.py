#!/usr/bin/env python3
"""Static contract consistency checks; not a simulation of actual agent behavior."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
AGENTS = (ROOT / 'AGENTS.md').read_text()
README = (ROOT / 'README.md').read_text()
SCENARIOS = (ROOT / 'docs/01-collaboration-behavior-scenarios.md').read_text()

class CollaborationContract(unittest.TestCase):
    def test_version_alignment(self):
        self.assertIn('**Contract version:** 3.2.0', AGENTS)
        self.assertIn('**Contract version:** `3.2.0`', README)

    def test_required_boundaries(self):
        for text in (
            'Track the objective, requested activity, and execution permission separately.',
            'Discussion is not\n  execution permission',
            'Rollback is a separate consequential action.',
            'A whole-mission\n  halt stops the mission',
            'Apply steering only within the actor',
            'unavailable evidence remains unknown',
            'Old tasks, transcripts, suggestions, and queued\n  jobs do not override',
            'For discussion-only\nwork, use the conversational completion rule',
            'an already-approved remote/branch\n   (not discussion, advice, or research',
        ):
            with self.subTest(boundary=text):
                self.assertIn(text, AGENTS)

    def test_conflicting_legacy_rules_removed(self):
        for text in (
            'Prefix `DISCUSS:` changes prose style only.',
            'stop immediately,\n  undo, acknowledge',
            'Stop immediately and undo; do not debate or finish',
            'resume all still-authorized work unless',
            'Prefer implementation over deliberation,',
            '`DISCUSS:` changes prose only, never progress',
        ):
            with self.subTest(legacy=text):
                self.assertNotIn(text, AGENTS + README)

    def test_scenario_matrix_is_complete_and_honest(self):
        rows = [line for line in SCENARIOS.splitlines() if re.match(r'\| C\d{2} \|', line)]
        self.assertEqual([line.split('|')[1].strip() for line in rows],
                         [f'C{i:02}' for i in range(1, 21)])
        for row in rows:
            self.assertEqual(len(row.split('|')), 6)
            self.assertTrue(all(cell.strip() for cell in row.split('|')[1:-1]))
        self.assertIn('No model-behavior rehearsal is claimed', SCENARIOS)
        self.assertIn('actual model behavior requires\nrehearsal', README)

    def test_local_markdown_links_exist(self):
        for text in (README, AGENTS):
            for link in re.findall(r'\]\(([^)]+)\)', text):
                path = link.split('#')[0]
                if path.startswith('./'):
                    with self.subTest(path=path):
                        self.assertTrue((ROOT / path).exists())

if __name__ == '__main__':
    unittest.main(verbosity=2)
