# Imports
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

# Models
from .models import RequestModel

# Managers
from .services.managers import RequestManager

# Serializers
from .services.serializers import RequestSerializer


class RequestViewSet(ViewSet):
    """Базовый класс обработки запросов"""

    serializer_class: RequestSerializer = RequestSerializer
    records: RequestManager = RequestManager(model=RequestModel)

    def list(self, request) -> Response:
        """Возвращает список команд и БД"""

        queryset = self.records.get_list_record()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk) -> Response:
        """Возвращает конкретную запись из БД"""

        queryset = self.records.get_target_record(pk=pk)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs) -> Response:
        """Создает запись команды в БД"""

        queryset = self.records.create_record(request=request)
        serilizer = self.serializer_class(queryset)
        return Response(serilizer.data)