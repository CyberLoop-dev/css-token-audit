import unittest
from main import audit_css

class CssAuditTests(unittest.TestCase):
    def test_reports_all_token_categories(self):
        report = audit_css(":root{--brand:red;--unused:blue;--brand:green}.x{color:var(--brand);background:var(--missing)}")
        self.assertEqual(report["duplicates"], ["--brand"])
        self.assertEqual(report["undefined"], ["--missing"])
        self.assertEqual(report["unused"], ["--unused"])

if __name__ == "__main__":
    unittest.main()
