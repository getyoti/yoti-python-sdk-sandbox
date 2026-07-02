from yoti_python_sdk.doc_scan import constants

from yoti_python_sandbox.doc_scan.check.sandbox_check import SandboxCheckBuilder
from yoti_python_sandbox.doc_scan.check.sandbox_check_report import SandboxCheckReport
from yoti_python_sandbox.doc_scan.check.sandbox_check_result import SandboxCheckResult
from yoti_python_sandbox.doc_scan.check.sandbox_liveness_check import (
    SandboxLivenessCheck,
)


class SandboxZoomLivenessCheck(SandboxLivenessCheck):
    def __init__(self, result, handled_check_limit=None):
        SandboxLivenessCheck.__init__(self, result, constants.ZOOM, handled_check_limit)


class SandboxZoomLivenessCheckBuilder(SandboxCheckBuilder):
    def build(self):
        report = SandboxCheckReport(self.recommendation, self.breakdown)
        result = SandboxCheckResult(report)
        return SandboxZoomLivenessCheck(result, self.handled_check_limit)
