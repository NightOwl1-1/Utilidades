import webbrowser
import subprocess

urls = [
    "https://chat.openai.com",
    "https://www.youtube.com/watch?v=jfKfPfyJRdk",
    "https://github.com",
    "https://cursos.alura.com.br/dashboard"
]

programas = [
    "S:\Visual Studio Code\Microsoft VS Code\Code.exe"
]


for url in urls:
    webbrowser.open(url)

for programa in programas:
    subprocess.Popen(programa)