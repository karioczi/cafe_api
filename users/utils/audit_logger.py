from models.audit import AuditLog
from .utils import get_client_ip

def log_user_action(user, action, request=None):
    ip = get_client_ip(request) if request else None
    user_agent = request.META.get('HTTP_USER_AGENT') if request else None
    AuditLog.objects.create(
        user=user, 
        action=action, 
        ip_address=ip,
        user_agent=user_agent
    )