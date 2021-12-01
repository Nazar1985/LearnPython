import asyncio
import collections
import socket


class ClientError(socket.error):
    """ Ошибка запроса """


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


class ClientServerProtocol(asyncio.Protocol):
    storage = collections.defaultdict(list)

    def __init__(self):
        super().__init__()

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

    def get(self, metric):
        response = str()
        if metric == '*':
            for key, values in ClientServerProtocol.storage.items():
                for timestamp, value in values:
                    response += f'{key} {value} {timestamp}\n'
            response += '\n'

        else:
            response_list = [(' '.join([metric, str(value), str(timestamp)]) +
                             '\n') for (timestamp, value) in ClientServerProtocol.storage[metric]]
            response = ''.join(response_list) + '\n'
        return response

    def put(self, key, value, timestamp):

        if key not in ClientServerProtocol.storage:
            ClientServerProtocol.storage[key] = [(timestamp, value)]
            if 's' in ClientServerProtocol.storage:
                ClientServerProtocol.storage.pop('s')
        else:
            dict_list = list(ClientServerProtocol.storage.get(key))
            timestamp_in_dict = [i for i in dict_list if i[0] == timestamp]
            if not timestamp_in_dict:
                dict_list.append((timestamp, value))
                dict_list.sort(key=lambda x: x[0])
                ClientServerProtocol.storage.update({key: dict_list})
            else:
                index_in_dict_list = dict_list.index(*timestamp_in_dict)
                ClientServerProtocol.storage.get(key)[index_in_dict_list] = (timestamp, value)

    def process_data(self, data):
        spl = data.rstrip('\n').split(' ')
        len_data = len(spl)
        command = spl[0]

        if command not in ('get', 'put'):
            response = 'error\nwrong command\n\n'
        else:
            response = 'ok\n'

        if len_data == 2 and command == 'get':
            metric = spl[1]
            response += self.get(metric)
        elif len_data == 4 and command == 'put':
            try:
                key = str(spl[1])
                value = float(spl[2])
                timestamp = int(spl[3])
                self.put(key, value, timestamp)
                response += '\n'
            except ValueError:
                response = 'error\nwrong command\n\n'
        else:
            response = 'error\nwrong command\n\n'

        return response
