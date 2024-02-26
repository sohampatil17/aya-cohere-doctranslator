import streamlit as st 
import main
import os
import base64

cohere_api_key = ''

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center; font-size:70px;'> सहायकAI 📃\n</h1>", unsafe_allow_html=True)
st.text("")
st.text("")
col1, col2 = st.columns(2)

col1, col2, col3 = st.columns([1,2,1])

with col2:  # This is the central column
    uploaded_file = st.file_uploader("Choose PDF:", type="pdf")

# Proceed with the rest of the layout only if a file has been uploaded
if uploaded_file is not None:
    cohere_api_key = ''

    # Display the original PDF in the left column
    col1, col2 = st.columns(2)
    with col1:
        st.header("अंग्रेजी में")
        # To display the PDF we will use a little trick with base64 encoding and an iframe
        st.write("आपका दस्तावेज़:")
        base64_pdf = base64.b64encode(uploaded_file.getvalue()).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

    # Display the translated PDF in the right column
    with col2:
        st.header("हिंदी में")
        with st.spinner("आपके दस्तावेज़ का अनुवाद हो रहा है......"):
            with open("temp_file.pdf", "wb") as f:
                f.write(uploaded_file.getbuffer())
            translated_pdf_path = main.process_pdf("temp_file.pdf", cohere_api_key)
        
        if os.path.exists(translated_pdf_path):
            with open(translated_pdf_path, "rb") as f:
                st.write("अनुवादित दस्तावेज़:")
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>'
                st.markdown(pdf_display, unsafe_allow_html=True)
                f.seek(0)
                st.download_button("Download Translated PDF", f.read(), file_name="translated_output.pdf")

        # Clean up the temp file after use
        os.remove("temp_file.pdf")

# with col1:
#     st.header("अंग्रेजी दस्तावेज़")
#     uploaded_file = st.file_uploader("Choose PDF:", type="pdf")
#     if uploaded_file is not None:
#         st.write("Original document:")
#         base64_pdf = base64.b64encode(uploaded_file.read()).decode('utf-8')
#         pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
#         st.markdown(pdf_display, unsafe_allow_html=True)
        
# with col2:
#     st.header("हिंदी दस्तावेज़")
#     if uploaded_file is not None and cohere_api_key:
#         with st.spinner("Translating your document..."):
#             translated_pdf_path = main.process_pdf("temp_file.pdf", cohere_api_key)
#         if os.path.exists(translated_pdf_path):
#             st.write("Translated document:")
#             with open(translated_pdf_path, "rb") as f:
#                 base64_pdf = base64.b64encode(f.read()).decode('utf-8')
#                 pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
#                 st.markdown(pdf_display, unsafe_allow_html=True)
#                 st.download_button("Download Translated PDF", f.read(), file_name="translated_output.pdf")
        
