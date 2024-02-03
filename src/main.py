import subprocess

from package.path import *

import json
configPath = "conf/config.json"
config = json.load(open(configPath))
mainDirectory = config["mainDirectory"]
homepagePath = config["homepagePath"]
path_to_homepage = getPath(mainDirectory,homepagePath)

subprocess.run(["streamlit","run",path_to_homepage])

#login credentials are in the  proj/data/.secret.yaml