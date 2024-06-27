import streamlit as st
import docx2txt
import PyPDF2
import io
import textstat
import pandas as pd

def extract_text_from_docx(file):
    return docx2txt.process(file)

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def extract_text(file):
    file_extension = file.name.split(".")[-1].lower()
    if file_extension == "docx":
        return extract_text_from_docx(file)
    elif file_extension == "pdf":
        return extract_text_from_pdf(file)
    else:
        return None

def analyze_readability(text):
    return {
        "Flesch Reading Ease": textstat.flesch_reading_ease(text),
        "Flesch-Kincaid Grade": textstat.flesch_kincaid_grade(text),
        "SMOG Index": textstat.smog_index(text),
        "Coleman-Liau Index": textstat.coleman_liau_index(text),
        "Automated Readability Index": textstat.automated_readability_index(text),
        "Dale-Chall Readability Score": textstat.dale_chall_readability_score(text),
        "Linsear Write Formula": textstat.linsear_write_formula(text),
        "Gunning Fog": textstat.gunning_fog(text),
    }

st.title("Document Readability Analyzer for NECF and VIC Categories")

categories = ["NECF", "VIC"]
uploaded_files = {category: [] for category in categories}

for category in categories:
    st.subheader(f"{category} Documents")
    uploaded_files[category] = st.file_uploader(f"Upload {category} documents", type=["docx", "pdf"], accept_multiple_files=True, key=category)

if st.button("Analyze Readability"):
    all_results = []

    for category in categories:
        if uploaded_files[category]:
            st.subheader(f"{category} Results")
            
            for file in uploaded_files[category]:
                text = extract_text(file)
                if text:
                    scores = analyze_readability(text)
                    results = {"Category": category, "Document": file.name}
                    results.update(scores)
                    all_results.append(results)
                    
                    st.write(f"Document: {file.name}")
                    for metric, score in scores.items():
                        st.write(f"{metric}: {score:.2f}")
                    st.write("---")
                else:
                    st.write(f"Error: Unable to extract text from {file.name}")
        else:
            st.write(f"No files uploaded for {category}")
    
    if all_results:
        df = pd.DataFrame(all_results)
        st.subheader("Summary Table")
        st.dataframe(df)
        
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download results as CSV",
            data=csv,
            file_name="readability_results.csv",
            mime="text/csv",
        )
    
    st.subheader("Interpretation Guide")
    st.write("Flesch Reading Ease:")
    st.write("- 90-100: Very Easy")
    st.write("- 80-89: Easy")
    st.write("- 70-79: Fairly Easy")
    st.write("- 60-69: Standard")
    st.write("- 50-59: Fairly Difficult")
    st.write("- 30-49: Difficult")
    st.write("- 0-29: Very Confusing")
    
    st.write("\nFlesch-Kincaid Grade Level:")
    st.write("Corresponds to the U.S. grade level of education needed to understand the text.")

    st.write("\nOther scores generally indicate the readability level, with lower scores suggesting easier readability.")
