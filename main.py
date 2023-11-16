from flask import Flask, render_template, request
import PyPDF2

app = Flask(__name__)

def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(pdf_reader.numPages):
            text += pdf_reader.getPage(page_num).extractText()
        return text

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file:
            file_path = f"uploads/{uploaded_file.filename}"
            uploaded_file.save(file_path)
            extracted_text = extract_text_from_pdf(file_path)
            return render_template('result.html', text=extracted_text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
