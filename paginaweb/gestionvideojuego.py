from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

class Videojuego:
    def __init__(self, titulo, genero, precio, disponible):
        self.titulo = titulo
        self.genero = genero
        self.precio = precio
        self.disponible = disponible

class Cliente:
    def __init__(self, nombre="Anonimo"):
        self.nombre = nombre
        self.juegos_rentados = []

class Tienda:
    def __init__(self):
        self.videojuegos = []

    def add_juego(self, juego):
        self.videojuegos.append(juego)

    def rentar_juego(self, titulo, cliente):
        for juego_tienda in self.videojuegos:
            if juego_tienda.titulo == titulo and juego_tienda.disponible > 0:
                juego_tienda.disponible -= 1
                cliente.juegos_rentados.append(juego_tienda)
                print(f"{cliente.nombre} ha rentado '{juego_tienda.titulo}'")
                return True
        print("Lo sentimos, el juego no está disponible para renta.")
        return False

tienda_juegos = Tienda()

# Crear juegos
juegos = [
    ("Grand theft auto 5", "Acción", 49.99, 10),
    ("Resident Evil 4 Remake", "Survival Horror", 59.99, 15),
    ("DeadSpace Remake", "Survival Horror", 59.99, 10),
    ("Bloodborne", "Acción", 40.00, 5),
    ("DarkSouls 3", "Acción", 40.00, 5),
    ("The Last of Us Part I", "Aventura", 50.00, 5),
    ("The Last of Us Part II", "Aventura", 59.99, 10),
    ("Elden Ring", "Acción", 59.99, 15),
    ("Call of Duty: Black Ops Cold War", "Shooter", 59.99, 20),
    ("Call of Duty: Modern Warfare (2019)", "Shooter", 49.99, 15),
    ("Call of Duty: Modern Warfare 2", "Shooter", 59.99, 10),
    ("Battlefield 4", "Shooter", 20.00, 5),
    ("Call of Duty: Black Ops III", "Shooter", 30.00, 5),
    ("God of War: Ragnarok", "Acción, Aventura", 59.99, 15),
    ("Resident Evil 2 Remake", "Survival Horror", 20.00, 10),
    ("Resident Evil 3 Remake", "Survival Horror", 25.00, 10)
]

for titulo, genero, precio, disponible in juegos:
    tienda_juegos.add_juego(Videojuego(titulo, genero, precio, disponible))

cliente1 = Cliente()

@app.route('/')
def index():
    return render_template('index.html', tienda=tienda_juegos)

@app.route('/rentar/<titulo>')
def rentar(titulo):
    if tienda_juegos.rentar_juego(titulo, cliente1):
        return redirect(url_for('index'))
    else:
        return "Lo sentimos, el juego no está disponible para renta."

if __name__ == '__main__':
    app.run(debug=True)
