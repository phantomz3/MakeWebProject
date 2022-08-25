import os

userinput = input("Enter The Project Name: ")
pathinput = input("Enter The Project Path: ")
print(userinput)

directory = userinput
parent_dir = pathinput

if pathinput == "desktop":
        parent_dir = "E:\Windows Libraries\Windows Desktop"
else:
        parent_dir = pathinput
        
path = os.path.join(parent_dir, directory)
os.mkdir(path)

css = "css"
path_css = os.path.join(parent_dir, directory, css)
os.mkdir(path_css)

img = "img"
path_img = os.path.join(parent_dir, directory, img)
os.mkdir(path_img)

idea = "idea"
path_idea = os.path.join(parent_dir, directory, idea)
os.mkdir(path_idea)

js = "js"
path_js = os.path.join(parent_dir, directory, js)
os.mkdir(path_js)

file_html = 'index.html'
file_css = 'style.css'
file_js = 'script.js'

with open(os.path.join(path, file_html), 'w') as fp:
        print("Html File Builded!")
        fp.write("<!DOCTYPE html>\n")
        fp.write("<html>\n")
        fp.write("<head>\n")
        fp.write("<title>Document</title>\n")
        fp.write("<link rel=\"stylesheet\" href=\"css\style.css\">\n")
        fp.write("</head>\n")
        fp.write("<body>\n")
        fp.write("<h1>This is a Heading</h1>\n")
        fp.write("<p>This is a paragraph.</p>\n")
        # make a button
        fp.write("<button onclick=\"Clicked()\">Click Me</button>\n")
        fp.write("<p id=\"demo\"></p>\n")
        fp.write("<script src=\"js\script.js\"></script>\n")
        fp.write("</body>\n")
        fp.write("</html>\n")
        fp.close()

with open(os.path.join(path_css, file_css), 'w') as fp:
        print("Css File Builded!!")
        fp.write("body {\n")
        fp.write("    background-color: rgb(245, 236, 178);\n")
        fp.write("}\n")
        fp.write("\n")
        fp.write("h1 {\n")
        fp.write("    color: red;\n")
        fp.write("    font-size: 3.5em;")
        fp.write("}\n")
        fp.write("\n")
        fp.write("p {\n")
        fp.write("    color: orangered;\n")
        fp.write("    font-size: 2em;")
        fp.write("}")

with open(os.path.join(path_js, file_js), 'w') as fp:
        print("Js File Builded!")
        fp.write("function Clicked() {\n")
        fp.write("var x = document.getElementById(\"demo\");\n")
        fp.write("x.innerHTML = \"Button Pressed\" };\n")
