from django.conf import settings

from pinax.apps.account.models import Account, AnonymousAccount


def account(request):
    if getattr(request, 'user', False) and request.user.is_authenticated():
        try:
            account = Account._default_manager.get(user=request.user)
        except Account.DoesNotExist:
            account = AnonymousAccount(request)
    else:
        account = AnonymousAccount(request)
    return {
        "account": account,
        "CONTACT_EMAIL": getattr(settings, "CONTACT_EMAIL", "support@example.com")
    }
