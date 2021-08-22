##old--
##import pip
##from subprocess import call
##for dist in pip.get_installed_distributions():
##    call("C:/Python34/Scripts/pip install --upgrade " + dist.project_name, shell=True)
##input()

import pkg_resources
from subprocess import call

#dists = [d for d in pkg_resources.working_set]

##for dist in pkg_resources.working_set:
##    call("pip install --upgrade " + dist.project_name, shell=True)


##import pkg_resources
##from subprocess import call
input("For start press return")

packages = [dist.project_name for dist in pkg_resources.working_set]
call("pip install --upgrade " + ' '.join(packages), shell=True)

input("\nUpgrade complete\n")
