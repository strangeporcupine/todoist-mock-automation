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

        if resp.text:
            return json.loads(resp.text)
        else:
            return resp

    def _get(self, endpoint, args=None, payload=None, **kwargs):
        if args:
            kwargs.update(args)
        return self._request('GET', endpoint, payload, kwargs)

    def _post(self, endpoint, args=None, payload=None, **kwargs):
        if args:
            kwargs.update(args)
        return self._request('POST', endpoint, payload, kwargs)

    def _delete(self, endpoint, args=None, payload=None, **kwargs):
        if args:
            kwargs.update(args)
        return self._request('DELETE', endpoint, payload, kwargs)

    def create_project(self, name, parent=None, color=None):
        data = {
            'name': name,
            'parent': parent,
            'color': color
        }
        return self._post('projects', payload=data)

    def get_tasks_by_project(self, project_id=None):
        return self._get('tasks', project_id=project_id)

    def get_task(self, task_id):
        return self._get('tasks/{}'.format(task_id))

    def reopen_task(self, task_id):
        # Bug with API found when using usual header with additional information.
        # Tasks gets reopened but api returns response 400, custom request used instead.
        return requests.post(self.BASE_URL + "tasks/{0}/reopen".format(task_id),
                             headers={"Authorization": "Bearer {}".format(self.token)})

    def get_all_projects(self):
        return self._get('projects')

    def delete_project_by_id(self, project_id):
        return self._delete('projects/{}'.format(project_id))

    def delete_project_by_name(self, project_name):
        projects = self.get_all_projects()
        for proj in projects:
            if project_name == proj['name']:
                self.delete_project_by_id(proj['id'])
