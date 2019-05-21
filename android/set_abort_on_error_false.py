import os
import sys


def is_app_build_gradle(file_path):
    gradle_file = open(file_path)
    file_content = gradle_file.read()

    if file_content.__contains__('android') and file_content.__contains__('signingConfigs'):
        return True
    else:
        return False


def find_build_gradle(project_path):
    name = 'build.gradle'
    walk = os.walk(project_path)
    for root, dirs, files in walk:
        if name in files:
            file_path = os.path.join(root, name)

            if is_app_build_gradle(file_path):
                return file_path

    raise Exception('Not found app build.gradle in ' + project_path)


def write_abort_on_error_false(file_path):
    gradle_file = open(file_path)
    file_content = gradle_file.read()

    if file_content.__contains__('abortOnError false'):
        print 'already false'
        return

    file_content = file_content.replace('android {', 'android { lintOptions {abortOnError false}')
    to_write = open(file_path, "w")
    to_write.write(file_content)
    to_write.close()


if __name__ == '__main__':

    if len(sys.argv) == 1:
        raise Exception('Android project path is not defined')

    project_path = sys.argv[1]
    gradle_file_path = find_build_gradle(project_path)
    write_abort_on_error_false(gradle_file_path)
    print 'success'
