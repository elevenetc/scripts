import subprocess as sb


def assemble(build_type):
    branch_cmd = sb.Popen(('./gradlew assemble' + build_type.capitalize()).split(), stdout=sb.PIPE)
    branch_cmd.stdout.readlines()