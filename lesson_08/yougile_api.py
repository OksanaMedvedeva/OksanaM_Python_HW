import requests


class YougileAPI:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def create_project(self, title, users):
        url = f"{self.base_url}/projects"
        payload = {
            "title": title,
            "users": users
        }
        response = requests.post(url,
                                 headers=self.headers,
                                 json=payload)
        return response

    def update_project(self,
                       project_id,
                       title=None,
                       users=None,
                       deleted=False):
        url = f"{self.base_url}/projects/{project_id}"
        payload = {}
        if title is not None:
            payload["title"] = title
        if users is not None:
            payload["users"] = users
        if deleted is not None:
            payload["deleted"] = deleted

        response = requests.put(url,
                                headers=self.headers,
                                json=payload)
        return response

    def get_project(self, project_id):
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        return response
