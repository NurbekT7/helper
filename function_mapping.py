def pdf_render():
    return "Its pdf renderer"

def xls_render():
    return "Its xls renderer"

def docx_render():
    return "Its docs renderer"


render_map = {
    "pdf": pdf_render,
    "xls": xls_render,
    "docx": docx_render,
}

i = input("Do it: ")

render_func = render_map.get(i)

print(render_func())