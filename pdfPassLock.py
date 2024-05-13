# pip install PyPDF2 を実行している前提のコードです


import PyPDF2

def encrypt_pdf(input_path, output_path, password):
    with open(input_path, 'rb') as file:
        pdf = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()

        for page_num in range(len(pdf.pages)):
            pdf_writer.add_page(pdf.pages[page_num])

        pdf_writer.encrypt(password)

        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)



if __name__ == '__main__':
    input_path = '' #パスワードをかけたいファイルを入力
    output_path = (input_path + '_passadded')
    password = '' #希望のパスワードを記入

    encrypt_pdf(input_path, output_path, password)
