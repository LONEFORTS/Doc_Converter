# QuickDocs main controller

from worker import send_to_go

def detect_type(filename):
    if filename.endswith(".pdf"):
        return "PDF"
    elif filename.endswith(".docx"):
        return "DOCX"
    elif filename.endswith(".png") or filename.endswith(".jpg"):
        return "IMAGE"
    else:
        return "UNKNOWN"

def convert(filename):
    file_type = detect_type(filename)
    print("Python: Detected", file_type)

    result = send_to_go(file_type)
    return result

if __name__ == "__main__":
    output = convert("example.pdf")
    print("Final Result:", output)