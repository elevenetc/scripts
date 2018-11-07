#! /usr/bin/env python
import os
import shutil
import sys


def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            if not os.path.exists(d) or os.stat(s).st_mtime - os.stat(d).st_mtime > 1:
                shutil.copy2(s, d)


if __name__ == '__main__':

    argsLen = len(sys.argv)
    print('copying report: ' + str(sys.argv))

    if argsLen < 5:
        raise Exception('Error: no arguments for copy-report.py. Passed arguments: ' + str(
            sys.argv) + '\nRequired: name, buildId, srcReportDir and dstReportsDir')
    else:

        name = sys.argv[1]
        buildId = sys.argv[2]
        srcReportDir = sys.argv[3]
        dstReportsDir = sys.argv[4]

        if not os.path.exists(srcReportDir):
            raise Exception('Reports directory does not exists:' + srcReportDir)

        latestDir = dstReportsDir + '/' + name + '/latest'
        currentBuildDir = dstReportsDir + '/' + name + '/' + buildId

        if os.path.exists(latestDir):
            shutil.rmtree(latestDir)

        copytree(srcReportDir, currentBuildDir)
        copytree(srcReportDir, latestDir)

        print(currentBuildDir)
