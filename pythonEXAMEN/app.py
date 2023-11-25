from flask import render_template, request, flash, redirect, url_for, Flask

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

usuarios = {
    "juan": "admin",
    "pepe": "user"
}
@app.route('/')
def index():
    return render_template('main.html')
@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/submit_calculo_compras', methods=['POST'])
def submit_calculo_compras():
    try:
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad_tarros = int(request.form['cantidadTarros'])
        costo_por_tarro = 9000
        costo_total_sin_descuento = cantidad_tarros * costo_por_tarro

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0
        costo_total_con_descuento = costo_total_sin_descuento * (1 - descuento)
        return render_template('resultado_calculo_compras.html',
                               nombre=nombre,
                               edad=edad,
                               cantidad_tarros=cantidad_tarros,
                               costo_total_sin_descuento=costo_total_sin_descuento,
                               costo_total_con_descuento=costo_total_con_descuento,
                               descuento=descuento)
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        username = request.form.get('username')  # Utiliza get() para evitar KeyError
        password = request.form.get('password')

        if username and password:
            if username in usuarios and password == usuarios.get(username):
                if username == 'juan':
                    flash('¡Bienvenido administrador juan!', 'success')
                elif username == 'pepe':
                    flash('¡Bienvenido usuario pepe!', 'success')


            else:
                flash('Credenciales incorrectas. Por favor, inténtalo de nuevo.', 'danger')
        else:
            flash('Completa todos los campos del formulario.', 'danger')

    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)