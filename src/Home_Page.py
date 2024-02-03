import streamlit as st
import streamlit_authenticator as stauth
import pickle

from package.drone import drone, droneExtent
from package.dock import dock, dockExtent
from package.path import *

st.set_page_config(
	page_title="Robotics Labs",
)

import json
configPath = "conf/config.json"
config = json.load(open(configPath))
mainDirectory = config["mainDirectory"]
secretPath = config["secretPath"]
path_to_secret = getPath(mainDirectory,secretPath)

import yaml
from yaml.loader import SafeLoader
with open(path_to_secret) as file:
	secret = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
	secret["credentials"],
	secret["cookie"]["name"],
	secret["cookie"]["key"],
	secret["cookie"]["expiry_days"]
	)

authenticator.login()

if st.session_state["authentication_status"] == False:
	st.error("username or password is incorrect")
if st.session_state["authentication_status"] == None:
	st.warning("Please enter username and password")
if st.session_state["authentication_status"]:
	st.title("Login Successful")
	dockExtent.read()
	droneExtent.read()
	st.session_state["dockExtent"] = dockExtent
	st.session_state["droneExtent"] = droneExtent
	authenticator.logout()
