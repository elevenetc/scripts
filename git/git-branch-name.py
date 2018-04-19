import subprocess as sb

if __name__ == '__main__':
    branch_name_cmd = sb.Popen('git rev-parse --symbolic-full-name --abbrev-ref HEAD'.split(), stdout=sb.PIPE)
    print branch_name_cmd.stdout.readlines()[0].replace('\n', '')
