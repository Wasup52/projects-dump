import PyPDF2


def extract_pdf_text(f):
    lines = []
    reader = PyPDF2.PdfFileReader(f)
    for i in range(0, 2):
        page = reader.getPage(i)
        line = page.extractText()
        line = line.encode("utf-8")
        # print(line)
        # for line in line:

        #     keep = line.count("FACT")
        #     if keep != 0:
        #         line = line.strip("\n")
        #         line = line.split(" ")
        #         for string in line:
        #             if string.count(",") != 0:
        #                 text += [string]
        #             else:
        #                 pass
        #     else:
        #         pass
        print(line)
        lines += [line]
    text = lines[0] + lines[1]
    return text


with open(""Relevé de compte\\RELEVES_0099607640_20210121.pdf", "rb") as f:
    text = extract_pdf_text(f)

with open("test.txt", "wb") as f:
    f.writelines(text)

print(text)
