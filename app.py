from flask import Flask, render_template_string

app = Flask(__name__)

# -------------------- HTML TEMPLATE --------------------
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
            overflow: hidden;
        }

        h1 {
            font-size: 3.2rem;
            margin-bottom: 10px;
            animation: fadeInDown 1.2s ease;
        }

        p {
            font-size: 1.3rem;
            opacity: .85;
            margin-bottom: 40px;
            max-width: 600px;
            animation: fadeIn 1.6s ease;
        }

        a.button {
            display: inline-block;
            padding: 12px 26px;
            font-size: 1rem;
            color: #fff;
            text-decoration: none;
            border-radius: 10px;
            background: #6200ea;
            transition: 0.2s;
            animation: fadeInUp 1.3s ease;
        }

        a.button:hover {
            background: #7b1fea;
            transform: scale(1.05);
        }

        footer {
            position: absolute;
            bottom: 8px;
            font-size: 14px;
            opacity: .5;
        }

        /* Animaciones */
        @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>

    <h1>{{ heading }}</h1>
    <p>{{ message }}</p>

    {% if button_text %}
    <a class="button" href="{{ button_link }}">{{ button_text }}</a>
    {% endif %}

    <footer>Servidor activo • Flassk</footer>

</body>
</html>
"""

# -------------------- RUTAS --------------------

@app.route("/")
def home():
    return render_template_string(
        html_base,
        title="juanpi tags",
        heading="Bienvenido al servidor",
        message="Este es un sitio montado con Flask en el servidor de juanpi.",
        button_text="Ir a Sobre mí",
        button_link="/about"
    )

@app.route("/about")
def about():
    return render_template_string(
        html_base,
        title="Sobre el sitio",
        heading="Acerca de este proyecto",
        message="Esta es una aplicación más elaborada de Flask con estilos animados y rutas organizadas.",
        button_text="Volver al Inicio",
        button_link="/"
    )

# -------------------- INICIO SERVIDOR --------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2407)