from yoti_python_sandbox.doc_scan.check.sandbox_check_report import SandboxCheckReport
from yoti_python_sandbox.doc_scan.check.sandbox_check_result import SandboxCheckResult
from yoti_python_sandbox.doc_scan.check.sandbox_document_check import (
    SandboxCheck,
)
from yoti_python_sandbox.doc_scan.check.sandbox_document_check import (
    SandboxCheckBuilder,
)


class SandboxThirdPartyIdentityCheck(SandboxCheck):
    @staticmethod
    def builder():
        return SandboxThirdPartyIdentityCheckBuilder()


class SandboxThirdPartyIdentityCheckBuilder(SandboxCheckBuilder):
    def build(self):
        report = SandboxCheckReport(self.recommendation, self.breakdown)
        result = SandboxCheckResult(report)
        return SandboxThirdPartyIdentityCheck(result)
