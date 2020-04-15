import requests
import json
from secret import * # set authorization token, stored in a separate file listed in git.ignore
#token='now set securely from secret'
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
    data=json.loads(response.content)
    #response.headers has a 'next' item
    while False: #for now
        pass
    
def get_student_userids_in_course(courseid):
    api_endpoint = '/api/v1/courses/'+ courseid + '/enrollments'
    get_api_response(api_endpoint)            
    ids=[]
    for student in data:
        ids.append(student['user_id'])
    return ids

                       
a = get_student_userids_in_course(courseid)    