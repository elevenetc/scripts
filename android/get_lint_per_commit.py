import os
import shutil
import subprocess
import sys


def find_file(project_path, name):
    walk = os.walk(project_path)
    for root, dirs, files in walk:
        if name in files:
            file_path = os.path.join(root, name)
            return file_path

    raise Exception('Not found file {} in {}'.format(name, project_path))


def mkdir(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)


def run_and_get(cmd):
    result = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    ).stdout.readlines()

    result = [line.replace('\n', '') for line in result]

    return result


def gradlew_at(path, cmd):
    print 'gradlew {} ...'.format(cmd)
    return run_and_get('cd {}; ./gradlew {}'.format(path, cmd))


def git_at(path, cmd):
    print 'git {} ...'.format(cmd)
    return run_and_get('git --git-dir={} {}'.format(path + '.git', cmd))


def log(msg):
    print msg


class Commit:

    def __init__(self):
        self.hash = ''
        self.time = ''
        self.committer_email = ''
        pass

    def parse(self, raw):
        split = raw.split(' kkk ')
        self.hash = split[0]
        self.committer_email = split[1]
        self.time = split[2]


if __name__ == '__main__':
    if len(sys.argv) == 1:
        raise Exception('Project path is not defined')
    project_path = sys.argv[1]

    commits = []
    counter = 3

    mkdir('commits')

    raw_commits = git_at(project_path, 'log --pretty=format:"%H kkk %ae kkk %ct"')

    for raw in raw_commits:
        counter = counter - 1

        if counter == -1:
            break

        commit = Commit()
        commit.parse(raw)
        commits.append(commit)

        commit_dir = 'commits/{}'.format(commit.hash)
        commit_file_path = commit_dir + '/info.txt'

        mkdir(commit_dir)

        commit_file = open(commit_file_path, 'w+')
        commit_file.write(
            'email: {}\nhash: {}\ntime: {}'.format(commit.committer_email, commit.hash, commit.time)
        )
        commit_file.close()

        git_at(project_path, 'checkout {}'.format(commit.hash))

        gradlew_at(project_path, 'lint')

        lint_html = find_file(project_path, 'lint-results.html')
        lint_xml = find_file(project_path, 'lint-results.xml')

        shutil.copy(lint_html, commit_dir)
        shutil.copy(lint_xml, commit_dir)
