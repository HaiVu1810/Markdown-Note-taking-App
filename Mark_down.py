from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
import os
import language_tool_python
import markdown
import uuid
tool = language_tool_python.LanguageTool('en-US')
app=FastAPI()
uploaded_path="uploaded_file"
if not os.path.exists(uploaded_path):
    os.makedirs(uploaded_path)

def render_template(raw_html):
    full_html = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Giao diện Render đẹp</title>
        <link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura.css" type="text/css">
        <style>
            body {{ max-width: 900px; margin: 40px auto; padding: 0 20px; }}
            pre {{ background: #2d2d2d; color: #ccc; padding: 15px; border-radius: 5px; overflow-x: auto; }}
            code {{ font-family: 'Consolas', monospace; color: #e83e8c; }}
            h1 {{ border-bottom: 2px solid #eee; padding-bottom: 10px; }}
        </style>
    </head>
    <body>
        {raw_html}
    </body>
    </html>
    """
    return full_html
@app.post("/uploadfile/")
async def save_upload_file(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        content= await file.read()
        text=content.decode("utf-8")
        save_path=uploaded_path+"/"+file.filename
        with open(uploaded_path+"/"+file.filename,"w",encoding="utf-8") as f:
            f.write(text)
        if os.path.exists(save_path) or os.path.getsize(save_path) == 0: 
            return {"file uploaded success"}
        # matches=tool.check(text)
        # for match in matches:
        #     print(f"Error: {match.message}")
        #     print(f"Suggestion: {match.replacements}")
        #     print(f"Context: {match.context}\n")

@app.get("/listfile")
async def list_uploaded_file():
    list_file=os.listdir(uploaded_path)
    return {"File uploaded": list_file}


@app.get("/listfile/{file_id}")
async def list_uploaded_file(file_id: int):
    list_file=os.listdir(uploaded_path)
    if file_id < 0 or file_id >= len(list_file):
        return {"error": "ID không tồn tại"}
    else:
        return {"File item": list_file[file_id]}
@app.get("/checkgrammar/{file_id}")
async def check_grammaer(file_id: int):
    list_file=os.listdir(uploaded_path)
    if file_id < 0 or file_id >= len(list_file):
        return {"error": "ID không tồn tại"}
    else:
        file_to_do=list_file[file_id]
        with open(uploaded_path+"/"+file_to_do,"r",encoding="utf-8") as f:
            text=f.read()
            matches=tool.check(text)
            all_errors = []
            for match in matches:
                response={
                "Error": match.message,
                "Suggestion": match.replacements,
                "Context": match.context
                }
                all_errors.append(response)                
        return {"file": file_to_do, "total_errors": len(all_errors), "errors": all_errors}
@app.get("/render/{file_id}")
async def check_grammaer(file_id: int):
    Port_=os.getenv("_port_")
    list_file=os.listdir(uploaded_path)
    if file_id < 0 or file_id >= len(list_file):
        return {"error": "ID không tồn tại"}
    else:
        html_uid=str(uuid.uuid4())
        file_to_do=list_file[file_id]
        with open(os.path.join(uploaded_path, file_to_do), "r",encoding="utf-8") as f:            
            text=f.read()
            raw_html = markdown.markdown(text, extensions=['fenced_code', 'codehilite', 'tables'])
            full_html = render_template(raw_html)
        return HTMLResponse(content=full_html)