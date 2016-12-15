import subprocess as sb


def get_branch_name():
    branch_name_cmd = sb.Popen('git rev-parse --symbolic-full-name --abbrev-ref HEAD'.split(), stdout=sb.PIPE)
    return branch_name_cmd.stdout.readlines()[0].replace('\n', '')
