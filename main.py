import streamlit as st
from extraction import extract_text_from_image, extract_text_from_pdf
from preprocessing import preprocess_text
from simplification import simplify_text

def main():
    st.title("Text Extraction, Preprocessing, and Simplification")

    st.header("Extract Text from Image or PDF")

    # Single button for choosing file type
    file_type = st.radio("Choose file type:", ("Image", "PDF"))

    if file_type == "Image":
        st.write("Upload an image file:")
        image_file = st.file_uploader("Choose an image file", type=["jpg", "png", "jpeg"])

        if image_file is not None:
            st.write("Extracted text from image:")
            extracted_text = extract_text_from_image(image_file)
            if extracted_text is not None:
                st.text_area("Extracted Text:", extracted_text)
                preprocessed_text = preprocess_text(extracted_text)
                st.write("Preprocessed Text:")
                st.text_area("Preprocessed Text:", preprocessed_text)
                if st.button("Simplify Text"):
                    simplified_text = simplify_text(preprocessed_text)
                    st.write("Simplified Text:")
                    st.text_area("Simplified Text:", simplified_text)

    elif file_type == "PDF":
        st.write("Upload a PDF file:")
        pdf_file = st.file_uploader("Choose a PDF file", type=["pdf"])

        if pdf_file is not None:
            st.write("Extracted text from PDF:")
            extracted_text = extract_text_from_pdf(pdf_file)
            if extracted_text is not None:
                st.text_area("Extracted Text:", extracted_text)
                preprocessed_text = preprocess_text(extracted_text)
                st.write("Preprocessed Text:")
                st.text_area("Preprocessed Text:", preprocessed_text)
                if st.button("Simplify Text"):
                    simplified_text = simplify_text(preprocessed_text)
                    st.write("Simplified Text:")
                    st.text_area("Simplified Text:", simplified_text)

if __name__ == "__main__":
    main()
