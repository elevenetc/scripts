import requests

def load_versions(app_id, hockey_token):
    url = 'https://rink.hockeyapp.net/api/2/apps/' + app_id + '/app_versions'
    headers = {'X-HockeyAppToken': hockey_token}
    response = requests.get(url, headers=headers)
    return response.content
