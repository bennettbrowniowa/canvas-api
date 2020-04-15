import requests
import json

from api_token import * # set authorization token, stored in a separate file listed in git.ignore
#token is now set using another file which can be kept more securely than this code.
#Create a file api_token.py continaing the following line of code, uncommented:
#token='10577~jhfjdashfjkdhafljhdajkhflsjkdhafjahlruthSDGgdfijdf'

baseurl='https://iowacityschools.instructure.com'
courseid='32536' #applied tech
courseid2='32512' #CS tech

def get_api_response(api_endpoint):
    api_endpoint_url = baseurl + \
                       '/api/v1/courses/'+ \
                       courseid+ \
                       '/enrollments'
    auth = {'Authorization': 'Bearer '+token}
    response = requests.get(api_endpoint_url, headers=auth)
    first_response_json=json.loads(response.content)
    #response.headers has a 'next' item
    data = paginate(first_response_json, response.headers)
    return data

import copy #There has to be a better way to do this
def paginate(first_response_json, response_header_json):
    #return the first response JSON, with all the following pages 
    #of the server's paginated response linked in the ['links'].split(';').['next']
    aggregate_response_json = copy.copy(first_response_json)#list.copy() doesn't exist until Python 3.3
    while 'Link' in response_header_json: #while theres a link and a next
        for link in response_header_json['Link'].split(','):
            if 'next' in link:
                link=link[1:link.find('>')]
                auth = {'Authorization': 'Bearer '+token}
                response = requests.get(link, headers=auth)
                response_json = json.loads(response.content)
                response_header_json = response.headers
                aggregate_response_json += response_json
                print response_header_json['Link']
            else:    
                response_header_json=''
    return aggregate_response_json    

def get_people_in_course(courseid):
    api_endpoint = '/api/v1/courses/'+ courseid + '/enrollments'
    data = get_api_response(api_endpoint)            
    user_ids = []
    names = [] 
    roles = []
    for student in data:
        user_ids.append(student['user_id'])
        names.append(student['user']['name'])
        roles.append(student['role'])       
    return user_ids, names, roles
                           
#a = get_people_in_course(courseid)
user_ids, names, roles = get_people_in_course(courseid)