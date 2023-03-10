def about():
    import json
    # with open('templates/about.html') as template:
    #     return template.read()
    dict_ = {'username': 'John Snow', 'image': 'http://image.jpg', 'bool': True, 'None': None}
    return json.dumps(dict_)
    
def contacts():
    with open('templates/contacts.html') as template:
        return template.read()

def images():
    with open('templates/images.html') as template:
        return template.read()

def video():
    with open('templates/video.html') as template:
        return template.read()
    
def profile():
    with open('templates/profile.html') as template:
        return template.read()