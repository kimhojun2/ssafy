from rest_framework.decorators import permission_classes
from .permissions import DevicePermission

device_permission_required = permission_classes((DevicePermission,))