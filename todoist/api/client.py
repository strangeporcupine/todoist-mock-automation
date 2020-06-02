import json
import uuid

import requests


class TodoistAPI:

    BASE_URL = 'https://api.todoist.com/rest/v1/'
    REQUEST_TIMEOUT = 30

    def __init__(self, token):
        self.token = token
        self._session = requests.Session()

    def _request_header(self):
        return {
            'Content-Type': 'application/json',
            'X-Request-Id': str(uuid.uuid4()),
            'Authorization': 'Bearer {}'.format(self.token)
        }

    def _request(self, method, endpoint, payload, params):
        args = dict(params=params)
        args['timeout'] = self.REQUEST_TIMEOUT
        if payload:
            args['data'] = json.dumps(payload)

        resp = self._session.request(method,
                                     self.BASE_URL+endpoint,
                                     headers=self._request_header(),
                                     **args)
        print(resp)
        return json.loads(resp.text)

    def _get(self, endpoint, args=None, payload=None, **kwargs):
        if args:
            kwargs.update(args)
        return self._request('GET', endpoint, payload, kwargs)

    def _post(self, endpoint, args=None, payload=None, **kwargs):
        if args:
            kwargs.update(args)
        return self._request('POST', endpoint, payload, kwargs)

    def create_project(self, name, parent=None, color=None):
        data = {
            'name': name,
            'parent': parent,
            'color': color
        }
        return self._post('projects', payload=data)

    def get_tasks(self):
        # TODO: method needed for assignment
        return

    def open_task(self):
        # TODO: method needed for assignment
        return
