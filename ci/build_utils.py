import subprocess as sb

import logger


def assemble(build_type):
    logger.log('assemble apk: ' + build_type)
    branch_cmd = sb.Popen(('./gradlew assemble' + build_type.capitalize()).split(), stdout=sb.PIPE)
    branch_cmd.stdout.readlines()
