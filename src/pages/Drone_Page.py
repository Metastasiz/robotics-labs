import streamlit as st

from package.drone import drone, droneExtent
from package.dock import dock, dockExtent
from package.utils import *

import json
configPath = "conf/config.json"
config = json.load(open(configPath))
logoPath = config["logoPath"]

droneExtent.read()
dockExtent.read()

st.set_page_config(
	page_title="Robotics Labs",
)

def callback_button_logo():
	st.image(logoPath)


if st.session_state["authentication_status"] == False:
	st.error("username or password is incorrect")
if st.session_state["authentication_status"] == None:
	st.warning("Please enter username and password")
if st.session_state["authentication_status"]:
	st.title("Drone Page")
	st.write("There is some limitation with the framework working with database, please click apply twice")
	for i, inst in enumerate(droneExtent.getExtent().values()):
		form_key = "f_"+str(i)
		with st.form(form_key):
			st.write(inst)
			st.write(inst.getFakeStatus())
			on = st.toggle("Debug: Online Status",value=inst.getFakeStatus()==fakeStatus.online)
			if on:
				inst.setFakeStatus(fakeStatus.online)
			else:
				inst.setFakeStatus(fakeStatus.offline)
			if inst.getFakeStatus()==fakeStatus.online:
				st.link_button("Operate", "https://youtu.be/kcfs1-ryKWE?si=O_gNW-MCBvm9hIUQ")
			else:
				st.link_button("Operate", "https://letmegooglethat.com/?q=how+to+turn+on+a+drone")
			#bt = st.button("Operate Drone",key="bt_"+str(i), on_click=callback_button_logo)

			with st.expander("See Description"):
				dockOption = [inst.getID() for inst in dockExtent.getExtent().values()]
				st.session_state[inst.getID()] = inst.getLinkDict()[dock]

				ms_key = "ms_" + str(i)
				st.session_state[ms_key] = st.multiselect("Dock List",options=dockOption,default=st.session_state[inst.getID()])

			if st.form_submit_button("Apply"):
				inst.addLinkById(dock,st.session_state[ms_key])
				idList = inst.getLinkDict()[dock]
				diffList = list(set(idList) - set(st.session_state[ms_key]))
				inst.removeLinkById(dock,diffList)
				droneExtent.write()
				dockExtent.write()
				
