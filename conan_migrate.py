# Original code taken from https://docs.conan.io/en/latest/uploading_packages/artifactory_ce.html

import os
import subprocess


def run(cmd):
    ret = os.system(cmd)
    if ret != 0:
        raise Exception("Command failed: %s" % cmd)

# Assuming local = conan server and artifactory remotes
output = subprocess.check_output("conan search -r=local --raw")
packages = output.splitlines()

for package in packages:
    print("Downloading %s" % package)
    run("conan download %s -r=local" % package)

run("conan upload \"*\" --all --confirm -r=artifactory")
