def is_app_created(app_name, branch, apps):
    for app in apps:
        if app.title == get_title(app_name, branch):
            return app
    return None


def get_title(app_name, branch):
    return app_name + ' - ' + branch


def is_valid_name(branch_name):
    if branch_name.find('*') != -1:
        return False

    if branch_name.find('HEAD') != -1:
        return False

    if branch_name.find('remotes/origin/') != 0:
        return False

    return True