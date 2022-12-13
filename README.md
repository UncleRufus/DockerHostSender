<h2>DockerHostSender</h2>
<br>
Репозиторий с примером выполнения скриптов на хосте при запросе из контейнера.
<br>
<p>
<b>Базовые зависимости для хоста:</b>
<ul>
<li>python 3.10</li>
<li>curl</li>
</ul>
</p>
<p>
<b>Структура проекта:</b>

Директория Local scripts сожержит локальный сервер и скрипт который будет выполянться на стороне хоста.

```
├── dto.py
├── local_server.py
└── local_script.py
```
<hr>
Директория web_apps / web_core сожержит обычный DRF (Django REST Framework) проект. Функция отправки запроса на локальный сервер описана в модуле web_apps/services/managers.py

```
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
```

</p>

<p>
Перед запуском контейнера необходимо запустить скрипт local_scripts/local_server.py, после чего запустить контейнер с использованием docker-compose up --build. После запуска контейнера достаточно отправить запрос по адресу http://127.0.0.1/request
</p>
