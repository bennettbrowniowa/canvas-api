import requests
import json
token='10577~CIeTyXGQoM6VdBWhCQqhV2uxHsZOnA3Qs8O5Cyy1ZIdbBidIHG7qiTNkPYHcetuk'
baseurl='https://iowacityschools.instructure.com'
courseid='32536' #applied tech
courseid2='32512' #CS tech

def get_student_userids_in_course(courseid):
    api_endpoint_url = baseurl + \
                       '/api/v1/courses/'+ \
                       courseid+ \
                       '/enrollments'
    auth = {'Authorization': 'Bearer '+token}
    response = requests.get(api_endpoint_url, headers=auth)
    data=json.loads(response.content)
    ids=[]
    for student in data:
        ids.append(student['user_id'])
    return ids

a = get_student_userids_in_course(courseid)    