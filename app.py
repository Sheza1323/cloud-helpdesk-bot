import streamlit as st

# Cloud App Title
st.set_page_config(page_title="Cloud Help Desk", page_icon="🤖")
st.title("🤖 Cloud IT Help Desk Assistant")
st.write("Welcome to the college cloud computing demo bot!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! How can the IT Help Desk assist you today?"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if user_input := st.chat_input("Type your IT problem here (e.g., WiFi issues, Password reset)..."):
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Simple Help Desk Cloud Logic
    user_input_lower = user_input.lower()
    if "wifi" in user_input_lower or "internet" in user_input_lower:
        response = "🔧 **WiFi Fix:** Please disconnect, wait 10 seconds, and reconnect to 'College-Student-WiFi'. If that fails, a support ticket has been auto-created."
    elif "password" in user_input_lower or "login" in user_input_lower:
        response = "🔑 **Password Reset:** You can reset your password at the student portal. I have logged this request in our directory service."
    else:
        response = "🎫 **Ticket Logged:** I didn't recognize that exact issue, but I have successfully created an urgent IT support ticket for you. A technician will contact you."

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})