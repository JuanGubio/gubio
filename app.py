from flask import Flask, render_template_string

app = Flask(__name__)

html_base = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(120deg, #0f0f0f, #1a1a1a, #111);
            color: white;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            text-align: center;
        }
        h1 { font-size: 3rem; margin-bottom: 10px; }
        p  { font-size: 1.3rem; opacity: .8; margin-bottom: 40px; }
        a.button {
            padding: 12px 26px;
            background: #6200ea;
            color: white;
            border-radius: 10px;
            text-decoration: none;
        }
        a.button:hover { background: #7b1fea; }
    </style>
</head>
<body>

<h1>{{ heading }}</h1>
<p>{{ message }}</p>

{% if button_text %}
<a class="button" href="{{ button_link }}">{{ button_text }}</a>
{% endif %}

<footer style="margin-top:40px; opacity:.4;">Servidor activo • Flask</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        html_base,
        title="juanpi tags",
        heading="Bienvenido al servidor",
        message="Este es un sitio montado con Flask en Docker.",
        button_text="Ir a Sobre mí",
        button_link="/about"
    )

@app.route("/about")
def about():
    return render_template_string(
        html_base,
        title="Sobre el sitio",
        heading="Acerca de este proyecto",
        message="App Flask funcionando con CI/CD y Docker Swarm.",
        button_text="Volver al inicio",
        button_link="/"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2407)
