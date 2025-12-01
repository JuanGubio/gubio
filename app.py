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
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Segoe UI', sans-serif;
            background: radial-gradient(circle at top, #1c1c1c, #0a0a0a 70%);
            color: white;
            overflow: hidden;
        }

        /* Animación suave de brillo */
        @keyframes glow-animation {
            0%   { box-shadow: 0 0 12px rgba(0,200,255,0.25); }
            50%  { box-shadow: 0 0 22px rgba(0,200,255,0.45); }
            100% { box-shadow: 0 0 12px rgba(0,200,255,0.25); }
        }

        .card {
            background: rgba(255,255,255,0.06);
            -webkit-backdrop-filter: blur(12px);
            backdrop-filter: blur(12px);
            padding: 40px 50px;
            border-radius: 22px;
            border: 1px solid rgba(255,255,255,0.1);
            text-align: center;
            animation: glow-animation 4s infinite;
        }

        h1 {
            font-size: 2.7rem;
            margin-bottom: 10px;
            font-weight: 600;
        }

        p {
            font-size: 1.25rem;
            opacity: 0.85;
            margin-bottom: 40px;
        }

        a.button {
            padding: 14px 30px;
            background: linear-gradient(90deg, #009dff, #00eaff);
            border-radius: 12px;
            color: black;
            font-weight: bold;
            text-decoration: none;
            transition: 0.25s;
        }

        a.button:hover {
            filter: brightness(1.25);
            transform: scale(1.05);
        }

        footer {
            position: absolute;
            bottom: 20px;
            font-size: 0.9rem;
            opacity: 0.35;
        }
    </style>
</head>
<body>

<div class="card">
    <h1>{{ heading }}</h1>
    <p>{{ message }}</p>

    {% if button_text %}
    <a class="button" href="{{ button_link }}">{{ button_text }}</a>
    {% endif %}
</div>

<footer>Servidor activo • Flask</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(
        html_base,
        title="Juanpi Tags",
        heading="Bienvenido a Juanpi el mas pro Tags",
        message="Servidor Flask desplegado con Docker + CI/CD.",
        button_text="Ver información",
        button_link="/about"
    )

@app.route("/about")
def about():
    return render_template_string(
        html_base,
        title="Sobre la app yavirac",
        heading="Acerca de este proyecto nfeudhfiuefh yaviraccc",
        message="Proyecto automatizado con GitHub Actions, Docker Buildx y Traefik.",
        button_text="Volver al inicio",
        button_link="/"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2407)
