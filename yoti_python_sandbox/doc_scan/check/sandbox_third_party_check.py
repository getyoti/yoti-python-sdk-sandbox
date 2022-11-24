from yoti_python_sandbox.doc_scan.check.sandbox_check import SandboxCheckBuilder
from yoti_python_sandbox.doc_scan.check.sandbox_check_report import SandboxCheckReport
from yoti_python_sandbox.doc_scan.check.sandbox_check_result import SandboxCheckResult
from .sandbox_check import SandboxCheck


class SandboxThirdPartyCheck(SandboxCheck):
    def __init__(self, result, manual_check):
        SandboxCheck.__init__(self, result)
        self.__manual_check = manual_check

    @property
    def type(self):
        return "THIRD_PARTY_IDENTITY"

    @property
    def manual_check(self):
        return self.__manual_check

    def to_json(self):
        parent = SandboxCheck.to_json(self)
        parent["type"] = self.type
        parent["manual_check"] = self.manual_check

        return parent


class SandboxThirdPartyCheckBuilder(SandboxCheckBuilder):
    def __init__(self):
        SandboxCheckBuilder.__init__(self)
        self.__manual_check = None

    def with_manual_check(self, manual_check):
        self.__manual_check = manual_check

        return self

    def build(self):
        report = SandboxCheckReport(self.recommendation, self.breakdown)
        result = SandboxCheckResult(report)

        return SandboxThirdPartyCheck(result, self.__manual_check)
