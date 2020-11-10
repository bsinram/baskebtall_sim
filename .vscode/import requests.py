
import requests
auth_token = 'YXBpQGFwaS5jb206d2VsY29tZQ=='
headers = {"Authorization": f"Basic {auth_token}"}
maint_requests = requests.get('https://bos.gofmx.com/api/v1/maintenance-requests', headers=headers).json()


# print(first_request)
for request in maint_requests:
    request_id = request['id']
    request_name = request['name']
    print(request_id, request_name)