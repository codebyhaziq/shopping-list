import streamlit as st

st.set_page_config(page_title="Shopping List Manager")

# Initialize session state
if "shopping_list" not in st.session_state:
    st.session_state.shopping_list = []

if "item_input" not in st.session_state:
    st.session_state.item_input = ""

# Title with your name
st.title("🛒 Shopping List Manager - Built by Haziq")

# Use a form to allow Enter key submission
with st.form("item_form", clear_on_submit=True):
    item = st.text_input("Enter an item", key="item_input")
    submitted = st.form_submit_button("Add Item")

    if submitted:
        if not item.strip():
            st.warning("Please enter an item.")
        elif item in st.session_state.shopping_list:
            st.info(f"{item} is already in your list.")
        else:
            st.session_state.shopping_list.append(item)
            st.success(f"{item} added successfully.")

# Delete section (outside form)
st.subheader("Manage Items")

delete_item = st.text_input("Enter item to delete", key="delete_input")

if st.button("Delete Item"):
    if not delete_item.strip():
        st.warning("Please enter an item to delete.")
    elif delete_item in st.session_state.shopping_list:
        st.session_state.shopping_list.remove(delete_item)
        st.success(f"{delete_item} removed successfully.")
    else:
        st.error(f"{delete_item} not found in list.")

# Display list
st.subheader("Your Shopping List")

if not st.session_state.shopping_list:
    st.write("Your shopping list is empty.")
else:
    for i, item in enumerate(st.session_state.shopping_list, start=1):
        st.write(f"{i}. {item}")

# Clear all button
if st.button("Clear List"):
    st.session_state.shopping_list = []
    st.success("Shopping list cleared.")
