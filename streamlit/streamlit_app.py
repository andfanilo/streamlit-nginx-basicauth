import base64
import streamlit as st

from streamlit.web.server.websocket_headers import _get_websocket_headers

st.title("Hello world :tada:")

headers = _get_websocket_headers()

# Receiving "Basic <user:pass as base64 encoded>"
encoded_user_passwd = headers["Authorization"].split(" ")[1]
user, password = base64.b64decode(encoded_user_passwd).decode().split(":")

st.header(f"Hello {user}, nice to see you")

with st.expander("⚙️ Advanced: Headers"):
    st.json(headers)
