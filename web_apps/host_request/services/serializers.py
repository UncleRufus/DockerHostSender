# Imports
from rest_framework.serializers import ModelSerializer

# Models
from web_apps.host_request.models import RequestModel


class RequestSerializer(ModelSerializer):
    """Сериализатор запросов"""

    class Meta:
        model: RequestModel = RequestModel
        fields: tuple[str] = (
            'cmd',
            'exit_code',
        )
