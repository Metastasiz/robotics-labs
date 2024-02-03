import streamlit as st

from package.drone import drone, droneExtent
from package.dock import dock, dockExtent
from time import sleep

droneExtent.read()
dockExtent.read()

st.set_page_config(
	page_title="Robotics Labs",
)

if st.session_state["authentication_status"] == False:
	st.error("username or password is incorrect")
if st.session_state["authentication_status"] == None:
	st.warning("Please enter username and password")
if st.session_state["authentication_status"]:
	st.title("Dock Page")
	st.write("There is some limitation with the framework working with database, please click apply twice")
	for i, inst in enumerate(dockExtent.getExtent().values()):
		form_key = "f_"+str(i)
		with st.form(form_key):
			st.write(inst)
			with st.expander("See Description"):
				droneOption = [inst.getID() for inst in droneExtent.getExtent().values()]
				st.session_state[inst.getID()] = inst.getLinkDict()[drone]

				ms_key = "ms_" + str(i)
				st.session_state[ms_key] = st.multiselect("Drone List",options=droneOption,default=st.session_state[inst.getID()])

				if st.form_submit_button("Apply"):
					inst.addLinkById(drone,st.session_state[ms_key])
					idList = inst.getLinkDict()[drone]
					diffList = list(set(idList) - set(st.session_state[ms_key]))
					inst.removeLinkById(drone,diffList)
					droneExtent.write()
					dockExtent.write()
			
			
