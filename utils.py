# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import inspect
import textwrap
import streamlit as st

def show_code(demo):
    """Display the source code of a function."""
    show_code = st.sidebar.checkbox("Show code", True)
    if show_code:
        st.markdown("## Code")
        sourcelines, _ = inspect.getsourcelines(demo)
        st.code(textwrap.dedent("".join(sourcelines)), language="python")

# Example function to demonstrate
def demo_function():
    st.write("🚀 Hello! This is a Streamlit demo function.")

# Streamlit UI
st.title("Streamlit Online Code Viewer")
st.write("Use the sidebar to show/hide the source code of the function.")

# Run the function and display its code
demo_function()
show_code(demo_function)
