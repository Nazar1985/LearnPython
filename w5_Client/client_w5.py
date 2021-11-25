import socket
import time


class ClientError(socket.error):
    """ Ошибка клиента """


class Client:
    """Класс клиент для отправки запросов"""
    def __init__(self, addr, port, timeout=None):
        self.socket = socket.create_connection((addr, port), timeout)
        self._data = dict()

    def __del__(self):
        self.socket.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()

    def put(self, metric: str, value, timestamp=None):
        """Метод для отправки метрик на сервер"""
        message = bytes(f"put {metric} {value} {timestamp if timestamp else int(time.time())}\n", encoding='utf8')
        self.socket.sendall(message)
        response = self.socket.recv(1024).decode()
        if response == 'ok\n\n':
            pass
        else:
            raise ClientError

    def get(self, metric):
        """Метод для получения метрик с сервера
        * - все метрики
        <metric> - название метрики
        return: словарь с метриками {<metric.unit: str>: [<timestamp: int>, <value: float>]}"""
        message = bytes(f"get {metric}\n", encoding='utf8')
        self.socket.sendall(message)
        response = self.socket.recv(1024).decode()
        response = response.split('\n')
        if response[0] == 'error':
            raise ClientError
        elif len(response) > 1 and response[0] == 'ok' and response[1] != '\n':
            for r in response[1:-2]:
                if len(r.split(' ')) == 3:
                    metric, value, timestamp = r.split(' ')
                    try:
                        metric = str(metric)
                        value = float(value)
                        timestamp = int(timestamp)
                    except ValueError:
                        raise ClientError
                    if metric not in self._data.keys():
                        self._data[metric] = [(timestamp, value)]
                    elif timestamp in list(self._data.values())[0][0]:
                        self._data.get(metric)[0] = (timestamp, value)
                    else:
                        list_s = list(self._data.get(metric))
                        list_s.append((timestamp, value))
                        list_s.sort(key=lambda x: x[0])
                        self._data.update({metric: list_s})
                else:
                    raise ClientError
        elif len(response) > 1 and response[0] == 'ok' and response[1] == '\n':
            pass
        else:
            raise ClientError
        return self._data

# client = Client('127.0.0.1', 8888, 15)
# print(client.get("*"))
