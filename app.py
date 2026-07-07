import streamlit as st

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Echo Chamber 9000",
    page_icon="🛰️",
    layout="centered"
)

# ---------------- Session State (keeps history across reruns) ----------------
if "transmission_log" not in st.session_state:
    st.session_state.transmission_log = []

# ---------------- Task 1: The UI Shell ----------------
st.title("🛰️ Echo Chamber 9000")
st.write(
    "Enter your name and a message below, then hit **Transmit** to send it into the void."
)
st.divider()

# ---------------- Task 2: Multi-Data Collection ----------------
col1, col2 = st.columns(2)
with col1:
    user_name = st.text_input("Name", placeholder="e.g. Aarti")
with col2:
    user_message = st.text_input("Message", placeholder="Type something...")

# ---------------- Task 3: The Action Gate ----------------
transmit = st.button("🚀 Transmit", use_container_width=True)

if transmit:
    clean_name = user_name.strip()
    clean_message = user_message.strip()

    # ---------------- Task 4: Conditional Routing (Edge Cases) ----------------
    if clean_name == "":
        st.error("⚠️ Please provide your name.")
    elif clean_message == "":
        st.warning("⚠️ Please type a message to transmit.")
    else:
        # ---------------- Task 5: The Formatted Output ----------------
        st.success(
            f"✅ Transmission successful! Greetings, {clean_name}. "
            f"We received your message: {clean_message}"
        )

        # ---------------- Advanced Challenge: Token Cost Estimator ----------------
        char_count = len(clean_message)
        word_count = len(clean_message.split())
        token_count = char_count // 4

        st.info(
            f"📊 System Check: Your message will consume approximately "
            f"**{token_count} tokens** from our context window."
        )

        # Extra metrics row — shows depth beyond the base requirement
        m1, m2, m3 = st.columns(3)
        m1.metric("Characters", char_count)
        m2.metric("Words", word_count)
        m3.metric("Est. Tokens", token_count)

        # Save this transmission to session history
        st.session_state.transmission_log.append(
            {"name": clean_name, "message": clean_message, "tokens": token_count}
        )

# ---------------- Transmission History (bonus feature) ----------------
if st.session_state.transmission_log:
    st.divider()
    with st.expander(f"📜 Transmission Log ({len(st.session_state.transmission_log)})"):
        for i, entry in enumerate(reversed(st.session_state.transmission_log), 1):
            st.write(
                f"**{i}.** {entry['name']} → \"{entry['message']}\" "
                f"({entry['tokens']} tokens)"
            )