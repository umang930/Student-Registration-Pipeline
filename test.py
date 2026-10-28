
import unittest
from pathlib import Path

class TestStudentRegistration(unittest.TestCase):

    def test_html_file_exists(self):
        self.assertTrue(Path("index.html").exists())

    def test_css_file_exists(self):
        self.assertTrue(Path("style.css").exists())

    def test_javascript_file_exists(self):
        self.assertTrue(Path("script.js").exists())

    def test_registration_form(self):
        html = Path("index.html").read_text(encoding="utf-8")
        self.assertIn('id="registrationForm"', html)
        self.assertIn('id="name"', html)
        self.assertIn('id="email"', html)
        self.assertIn('id="roll"', html)
        self.assertIn('id="course"', html)

if __name__ == "__main__":
    unittest.main()
