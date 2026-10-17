from django.test import TestCase, Client
from django.urls import reverse
from aboutCCE.models import AuditedStatements


class AuditedStatementsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.stmt_cce = AuditedStatements.objects.create(
            name="Audited Statement 2023-24",
            file="AuditedStatements/Audited__2023-24.pdf",
            institution="Christ College of Engineering",
            order=1,
        )
        self.stmt_ccil = AuditedStatements.objects.create(
            name="Audited FS 23-24",
            file="AuditedStatements/Audited_FS_23-24.pdf",
            institution="Christ Centre for Innovation",
            order=1,
        )

    def test_model_str(self):
        self.assertEqual(str(self.stmt_cce), "Audited Statement 2023-24 (Christ College of Engineering)")
        self.assertEqual(str(self.stmt_ccil), "Audited FS 23-24 (Christ Centre for Innovation)")

    def test_audited_statements_page_renders_tabs(self):
        response = self.client.get(reverse('Audited_Statements'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Christ College of Engineering")
        self.assertContains(response, "Christ Centre for Innovation")
        self.assertContains(response, "Audited Statement 2023-24")
        self.assertContains(response, "Audited FS 23-24")
        self.assertIn("cce_data", response.context)
        self.assertIn("ccil_data", response.context)
        self.assertGreaterEqual(len(response.context["cce_data"]), 1)
        self.assertGreaterEqual(len(response.context["ccil_data"]), 1)
