import streamlit as st

st.set_page_config(page_title="Linguistic Fingerprinting PoC", layout="wide")

st.title("Instructions and Information Before Using the Proof of Concept")

st.markdown("""
As part of the initial development phase, a **proof of concept (PoC)** has been created to demonstrate the core functionality of the AI-based linguistic fingerprinting tool. The goal is to show that it is possible to analyze anonymous texts and match them to known language patterns using machine learning and language technology.

The PoC is based on a small, simulated environment featuring **three fictional individuals—Person A, Person B, and Person C**. Each of these individuals has their unique linguistic fingerprint, which is described in the PoC. These fingerprints are based on sample texts that reflect their writing style, tone, vocabulary, and syntactic preferences. Together, they make up the project’s preliminary linguistic fingerprint database.

> ⚠️ In a real-world application, this database would need to include thousands of individuals and far more data, such as material extracted from seized phones, chat logs, or anonymized text communications. The current setup is meant only to demonstrate the underlying mechanism.

To test the tool, users are invited to submit a conversation between **two unknown individuals** – referred to as **Person 1** and **Person 2**. The AI will analyze their respective linguistic fingerprints and compare them to the ones in the database (i.e., A, B, and C). The tool will then output the **closest matches** for each unknown person, along with a **similarity score in percentage**.

This allows investigators to move from a situation where they have **zero suspects** to a short list of **potential individuals** whose writing style closely resembles the unknown authors. These individuals can then be prioritized for follow-up, such as interviews or further analysis, within the scope of a broader investigation.

---

### 🗨️ Sample Conversation

**Person 1:** I compiled the results into a dashboard. Efficiency increased by 23%.  
**Person 2:** omg lol didn’t expect that haha. do we get cake now?  
**Person 1:** If we optimize the logic further, we could hit 30%.  
**Person 2:** that’d be sickkk. btw i’m out tmrw, dentist 😭

---

If you do not have your own text, we recommend starting with this sample; copy it and paste it into the PoC for analysis. The contrast between **Person 1’s** formal, technical tone and **Person 2’s** casual, expressive language makes it ideal for demonstrating how the model identifies distinct linguistic styles and links them to profiles in the database.

> 🔍 **Note:** The tool is intended to support investigative work—not to serve as legal evidence. Its purpose is to expand what is currently possible in digital investigations, especially in cases involving encrypted or anonymous communication where traditional methods fall short.
""")

st.markdown("---")

if st.button("Go to Analysis Tool"):
    st.switch_page("pages/analysis_tool.py")
