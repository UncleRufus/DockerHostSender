# Imports
import json
import requests

# TypeHints
from django.db.models import Model
from django.http import HttpResponse
from requests import Request
from typing import Any


class RequestManager:
    """Менеджер запросов"""

    def __init__(self, model: Model) -> None:
        """Base init"""

        self.model = model

    def get_list_record(self) -> HttpResponse:
        """Return list records"""

        return self.model.objects.all()

    def get_target_record(self, pk) -> HttpResponse:
        """Return current record"""

        return self.model.objects.get(pk=pk)

    def create_record(self, request) -> HttpResponse:
        """Create new record"""

        new_record = self.model.objects.create(
            cmd=self.make_local_request()['cmd'],
            exit_code=self.make_local_request()['exit_code'],
        )
        new_record.save()
        return new_record

    def make_local_request(self) -> dict[str, Any]:
        """Send local request to host"""

        try:
            local_request: Request = requests.get(
                'http://host.docker.internal:9999/get_pwd/',
                timeout=60,
                verify=False
            )

            parsed_request: dict[str, str] = json.loads(local_request.text)
            return parsed_request

        except Exception:
            parsed_request: dict[str, str] = {
                'cmd': 'Нет ответа от локального сервера',
                'exit_code': '404'
            }
            return parsed_request
