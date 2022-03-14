from typing import Optional


class AntiCaptchaError(Exception):
    response: Optional[dict] = None


class KeyDoesNotExist(AntiCaptchaError):
    pass


class NoSlotAvailable(AntiCaptchaError):
    pass


class ZeroCaptchaFilesize(AntiCaptchaError):
    pass


class TooBigCaptchaFilesize(AntiCaptchaError):
    pass


class ZeroBalance(AntiCaptchaError):
    pass


class IpNotAllowed(AntiCaptchaError):
    pass


class CaptchaUnsolvable(AntiCaptchaError):
    pass


class BadDuplicates(AntiCaptchaError):
    pass


class NoSuchMethod(AntiCaptchaError):
    pass


class ImageTypeNotSupported(AntiCaptchaError):
    pass


class NoSuchCapchaId(AntiCaptchaError):
    pass


class IpBlocked(AntiCaptchaError):
    pass


class TaskAbsent(AntiCaptchaError):
    pass


class TaskNotSupported(AntiCaptchaError):
    pass


class IncorrectSessionData(AntiCaptchaError):
    pass


class ProxyConnectRefused(AntiCaptchaError):
    pass


class ProxyConnectTimeout(AntiCaptchaError):
    pass


class ProxyReadTimeout(AntiCaptchaError):
    pass


class ProxyBanned(AntiCaptchaError):
    pass


class ProxyTransparent(AntiCaptchaError):
    pass


class RecaptchaTimeout(AntiCaptchaError):
    pass


class RecaptchaInvalidSitekey(AntiCaptchaError):
    pass


class RecaptchaInvalidDomain(AntiCaptchaError):
    pass


class RecaptchaOldBrowser(AntiCaptchaError):
    pass


class TokenExpired(AntiCaptchaError):
    pass


class ProxyHasNoImageSupport(AntiCaptchaError):
    pass


class ProxyIncompatibleHttpVersion(AntiCaptchaError):
    pass


class ProxyNotAuthorised(AntiCaptchaError):
    pass


class InvisibleRecaptcha(AntiCaptchaError):
    pass


class FailedLoadingWidget(AntiCaptchaError):
    pass


class VisibleRecaptcha(AntiCaptchaError):
    pass


class AllWorkersFiltered(AntiCaptchaError):
    pass


class AccountSuspended(AntiCaptchaError):
    pass


class TemplateNotFound(AntiCaptchaError):
    pass


class TaskCanceled(AntiCaptchaError):
    pass


error_by_id = {
    1: KeyDoesNotExist,
    2: NoSlotAvailable,
    3: ZeroCaptchaFilesize,
    4: TooBigCaptchaFilesize,
    10: ZeroBalance,
    11: IpNotAllowed,
    12: BadDuplicates,
    14: NoSuchMethod,
    15: ImageTypeNotSupported,
    16: NoSuchCapchaId,
    21: IpBlocked,
    22: TaskAbsent,
    23: TaskNotSupported,
    24: IncorrectSessionData,
    25: ProxyConnectRefused,
    26: ProxyConnectTimeout,
    27: ProxyReadTimeout,
    28: ProxyBanned,
    29: ProxyTransparent,
    30: RecaptchaTimeout,
    31: RecaptchaInvalidSitekey,
    32: RecaptchaInvalidDomain,
    33: RecaptchaOldBrowser,
    34: TokenExpired,
    35: ProxyHasNoImageSupport,
    36: ProxyIncompatibleHttpVersion,
    49: ProxyNotAuthorised,
    51: InvisibleRecaptcha,
    52: FailedLoadingWidget,
    53: VisibleRecaptcha,
    54: AllWorkersFiltered,
    55: AccountSuspended,
    56: TemplateNotFound,
    57: TaskCanceled
}
