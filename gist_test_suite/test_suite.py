import requests
import jsonpath
import json
import sys
sys.path.append('../')
from utilities import Utilities

### Folder structure
output_files,input_files=Utilities().folder_structure()

### Credentials
token=Utilities().token_type()
url=Utilities().url
user=Utilities().user

### Test Case: Gists accessibility
def test_GistsAccessibility():
    response=requests.get(url +"/gists", auth=(user,token))
    json_response = json.loads(response.text)
    file = open('{}\GistsAccessibility.json'.format(output_files), 'w')
    file.write(json.dumps(json_response, indent=2))
    assert response.status_code==200

### Test Case: List public gists
def test_ListPublicGists():
    response=requests.get(url +"/gists/public", auth=(user,token))
    json_response=json.loads(response.text)
    file = open('{}\ListPublicGists.json'.format(output_files), 'w')
    file.write(json.dumps(json_response, indent=2))
    assert response.status_code==200

### Test Case: List gists for a user
def test_ListUserGists():
    response=requests.get(url +"/users/"+user+"/gists", auth=(user,token))
    json_response = json.loads(response.text)
    file = open('{}\ListUserGists.json'.format(output_files), 'w')
    file.write(json.dumps(json_response, indent=2))
    assert response.status_code==200

### Test Case: List gists for the authenticated user
def test_ListAuthenticatedGists():
    response=requests.get(url +"/gists", auth=(user,token))
    json_response = json.loads(response.text)
    file = open('{}\ListAuthenticatedGists.json'.format(output_files), 'w')
    file.write(json.dumps(json_response, indent=2))
    assert response.status_code==200

### Test Case: Creating a Gist
def test_CreateGist():
    file=open(input_files+'\PublicGist.json', 'r')
    json_input=file.read()
    json_request=json.loads(json_input)
    response=requests.post(url +"/gists",json_request,auth=(user,token))
    json_response=json.loads(response.text)
    file = open('{}\CreateGist.json'.format(output_files), 'w')
    file.write(json.dumps(json_response, indent=2))
    assert response.status_code==201

### Test Case: Reading a Gist
def test_ReadingGist():
    file=open('{}\CreateGist.json'.format(output_files), 'r')
    json_input=file.read()
    json_request=json.loads(json_input)
    gist_id=jsonpath.jsonpath(json_request,'id')
    response = requests.get(url + "/gists/" + gist_id[0], auth=(user, token))
    json_response=json.loads(response.text)
    file = open('{}\ReadingGist.json'.format(output_files), 'w')
    file.write(json.dumps(json_response, indent=2))
    assert response.status_code==200

### Test Case: Deleting a Gist
def test_DeleteGist():
    file=open('{}\CreateGist.json'.format(output_files), 'r')
    json_input=file.read()
    json_request=json.loads(json_input)
    gist_id=jsonpath.jsonpath(json_request,'id')
    response = requests.delete(url + "/gists/" + gist_id[0], auth=(user, token))
    assert response.status_code==204

### Test Case: Rate limiting quotas
def test_RateLimitingQuotas():
    response=requests.get(url +"/rate_limit", auth=(user,token))
    json_response = json.loads(response.text)
    file = open('{}\RateLimitingQuotas.json'.format(output_files), 'a+')
    file.write(json.dumps(json_response, indent=2))
    rate = jsonpath.jsonpath(json_response, 'rate')
    limit=rate[0]
    assert limit["limit"] == 5000



