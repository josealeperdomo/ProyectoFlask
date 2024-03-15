from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
mysql = MySQL(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'libreria'

#METODO GET

@app.route('/autores')
def mostrar_autores():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM autores')
    columnas = [ columna[0] for columna in cursor.description]
    autores = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    res = jsonify(autores)
    res.headers.add('Access-Control-Allow-Origin','*')
    return res

@app.route('/usuarios')
def mostrar_usuarios():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM usuarios')
    columnas = [ columna[0] for columna in cursor.description]
    usuarios = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    res = jsonify(usuarios)
    res.headers.add('Access-Control-Allow-Origin','*')
    return res

@app.route('/generos')
def mostrar_generos():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM generos')
    columnas = [ columna[0] for columna in cursor.description]
    generos = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    res = jsonify(generos)
    res.headers.add('Access-Control-Allow-Origin','*')
    return res

@app.route('/editoriales')
def mostrar_editoriales():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM editoriales')
    columnas = [ columna[0] for columna in cursor.description]
    editoriales = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    res = jsonify(editoriales)
    res.headers.add('Access-Control-Allow-Origin','*')
    return res

@app.route('/libros')
def mostrar_libros():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM libros')
    columnas = [ columna[0] for columna in cursor.description]
    libros = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    res = jsonify(libros)
    res.headers.add('Access-Control-Allow-Origin','*')
    return res

@app.route('/resenas')
def mostrar_resenas():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM resenas')
    columnas = [ columna[0] for columna in cursor.description]
    resenas = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    res = jsonify(resenas)
    res.headers.add('Access-Control-Allow-Origin','*')
    return res




#METODO POST

@app.route('/autores', methods=['POST'])
def agregar_autor():
    nombre = request.json['nombre']

    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO autores (nombre) VALUES (%s)', (nombre,))
    mysql.connection.commit()
    cursor.close()
    res = jsonify({'mensaje':'autor agregado con exito'})
    return res

@app.route('/usuarios', methods=['POST'])
def agregar_usuario():
    nombre = request.json['nombre']

    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO usuarios (nombre) VALUES (%s)', (nombre,))
    mysql.connection.commit()
    cursor.close()
    res = jsonify({'mensaje':'usuario agregado con exito'})
    return res

@app.route('/generos', methods=['POST'])
def agregar_genero():
    nombre = request.json['nombre']

    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO generos (nombre) VALUES (%s)', (nombre,))
    mysql.connection.commit()
    cursor.close()
    res = jsonify({'mensaje':'genero agregado con exito'})
    return res

@app.route('/editoriales', methods=['POST'])
def agregar_editorial():
    nombre = request.json['nombre']

    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO editoriales (nombre) VALUES (%s)', (nombre,))
    mysql.connection.commit()
    cursor.close()
    res = jsonify({'mensaje':'editorial agregado con exito'})
    return res

@app.route('/libros', methods=['POST'])
def agregar_libro():
    titulo = request.json['titulo']
    ano_de_publicacion = request.json['ano_de_publicacion']
    autor_id = request.json['autor_id']
    genero_id = request.json['genero_id']
    editorial_id = request.json['editorial_id']
    imagen = request.json['imagen']


    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO libros (titulo,ano_de_publicacion,autor_id,genero_id,editorial_id,imagen) VALUES (%s,%s,%s,%s,%s,%s)', (titulo,ano_de_publicacion,autor_id,genero_id,editorial_id,imagen))
    mysql.connection.commit()
    cursor.close()
    res = jsonify({'mensaje':'libro agregado con exito'})
    res.headers.add('Access-Control-Allow-Origin','*')
    return res

@app.route('/resenas', methods=['POST'])
def agregar_resena():
    contenido = request.json['contenido']
    libro_id = request.json['libro_id']
    usuario_id = request.json['usuario_id']

    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO resenas (contenido,libro_id,usuario_id) VALUES (%s,%s,%s)', (contenido,libro_id,usuario_id))
    mysql.connection.commit()
    cursor.close()
    res = jsonify({'mensaje':'resena agregado con exito'})
    return res



#metodo patch

@app.route('/autores/<autor_id>', methods=['PATCH'])
def modificar_autor(autor_id):
    nombre = request.json['nombre']

    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE autores SET nombre = %s WHERE id = %s', (nombre,autor_id))
    mysql.connection.commit()
    cursor.close()
    res = jsonify({'mensaje':'autor actualizado con exito'})
    return res

@app.route('/usuarios/<user_id>', methods=['PATCH'])
def modificar_usuario(user_id):
    nombre = request.json['nombre']

    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE usuarios SET nombre = %s WHERE id = %s', (nombre,user_id))
    mysql.connection.commit()
    cursor.close()
    res = jsonify({'mensaje':'usuario actualizado con exito'})
    return res

@app.route('/generos/<genero_id>', methods=['PATCH'])
def modificar_genero(genero_id):
    nombre = request.json['nombre']

    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE generos SET nombre = %s WHERE id = %s', (nombre,genero_id))
    mysql.connection.commit()
    cursor.close()
    res = jsonify({'mensaje':'genero actualizado con exito'})
    return res

@app.route('/editoriales/<editorial_id>', methods=['PATCH'])
def modificar_editorial(editorial_id):
    nombre = request.json['nombre']

    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE editoriales SET nombre = %s WHERE id = %s', (nombre,editorial_id))
    mysql.connection.commit()
    cursor.close()
    res = jsonify({'mensaje':'editorial actualizado con exito'})
    return res


@app.route('/libros/<libro_id>', methods=['PATCH'])
def modificar_libro(libro_id):
    datos_actualizados = request.json

    if not datos_actualizados:
        return({'error':'No se enviaron los datos'})

    cursor = mysql.connection.cursor()

    update_query = 'UPDATE libros SET '
    update_data = []

    for campo, valor in datos_actualizados.items():
        if campo in ["titulo","ano_de_publicacion","autor_id","genero_id","editorial_id"]:
            update_query += f"{campo} = %s, "
            update_data.append(valor)

        if not update_data:
            return jsonify({'error':'los datos estan vacios'})
    
    update_query = update_query.rstrip(', ')
    update_query += 'WHERE id = %s'
    update_data.append(libro_id)
    cursor.execute(update_query, tuple(update_data))
    mysql.connection.commit()
    cursor.close()

    return jsonify({'mensaje': 'El libro se ha actualizado'})

@app.route('/resenas/<resena_id>', methods=['PATCH'])
def modificar_resena(resena_id):
    datos_actualizados = request.json

    if not datos_actualizados:
        return({'error':'No se enviaron los datos'})

    cursor = mysql.connection.cursor()

    update_query = 'UPDATE resenas SET '
    update_data = []

    for campo, valor in datos_actualizados.items():
        if campo in ["contenido","libro_id","usuario_id"]:
            update_query += f"{campo} = %s, "
            update_data.append(valor)

        if not update_data:
            return jsonify({'error':'los datos estan vacios'})
    
    update_query = update_query.rstrip(', ')
    update_query += 'WHERE id = %s'
    update_data.append(resena_id)
    cursor.execute(update_query, tuple(update_data))
    mysql.connection.commit()
    cursor.close()

    return jsonify({'mensaje': 'La resena se ha actualizado'})

#metodo delete

@app.route('/autores/<user_id>', methods=['DELETE'])
def eliminar_autor(autor_id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM autores WHERE id = %s', (autor_id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'respuesta':'El autor ha sido eliminado'})

@app.route('/usuarios/<user_id>', methods=['DELETE'])
def eliminar_usuario(user_id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id = %s', (user_id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'respuesta':'El usuario ha sido eliminado'})

@app.route('/generos/<genero_id>', methods=['DELETE'])
def eliminar_genero(genero_id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM generos WHERE id = %s', (genero_id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'respuesta':'El genero ha sido eliminado'})

@app.route('/editoriales/<editorial_id>', methods=['DELETE'])
def eliminar_editorial(editorial_id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM editoriales WHERE id = %s', (editorial_id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'respuesta':'El editorial ha sido eliminado'})

@app.route('/libros/<libro_id>', methods=['DELETE'])
def eliminar_libro(libro_id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM libros WHERE id = %s', (libro_id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'respuesta':'El libro ha sido eliminado'})

@app.route('/resenas/<resena_id>', methods=['DELETE'])
def eliminar_resena(resena_id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM resenas WHERE id = %s', (resena_id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'respuesta':'El resena ha sido eliminado'})

#ruta especial

@app.route('/rutadetallada')
def mostrar_info():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT libros.id, libros.titulo AS titulo_del_libro, libros.imagen AS imagen, autores.nombre AS autor, generos.nombre AS genero, resenas.contenido AS resena, usuarios.nombre AS escritor_de_resena FROM libros INNER JOIN autores ON autores.id = libros.autor_id INNER JOIN generos ON generos.id = libros.genero_id LEFT JOIN resenas ON libros.id = resenas.libro_id LEFT JOIN usuarios ON usuarios.id = resenas.usuario_id;')
    columnas = [ columna[0] for columna in cursor.description]
    info = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    res = jsonify(info)
    res.headers.add('Access-Control-Allow-Origin','*')
    return res

#ruta especial con condicion
@app.route('/rutadetallada/<libro_id>')
def mostrar_info_especifica(libro_id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT libros.id, libros.titulo AS titulo_del_libro, libros.imagen AS imagen, autores.nombre AS autor, generos.nombre AS genero, resenas.contenido AS resena, usuarios.nombre AS escritor_de_resena FROM libros INNER JOIN autores ON autores.id = libros.autor_id INNER JOIN generos ON generos.id = libros.genero_id LEFT JOIN resenas ON libros.id = resenas.libro_id LEFT JOIN usuarios ON usuarios.id = resenas.usuario_id WHERE libros.id = %s;', (libro_id,))
    columnas = [ columna[0] for columna in cursor.description]
    info = [dict(zip(columnas, fila)) for fila in cursor.fetchall()]
    cursor.close()
    res = jsonify(info)
    res.headers.add('Access-Control-Allow-Origin','*')
    return res

if __name__ == '__main__':
    app.run(debug=True, port=7500)