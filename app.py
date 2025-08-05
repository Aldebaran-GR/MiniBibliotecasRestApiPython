"""
Mini Bibliotecas REST API - Aplicación Flask
"""

from flask import Flask, jsonify, request
from database.db_connection import get_db_connection

# Crear la instancia de la aplicación Flask
app = Flask(__name__)

# Endpoint para obtener todos los libros con sus autores y editoriales
@app.route('/libros', methods=['GET'])
def get_libros():
    # Conectar a la base de datos
    connection = get_db_connection()
    if connection is None:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500
    
    # Crear un cursor para ejecutar consultas
    cursor = connection.cursor()

    #Consulta SQL que una las tablas libro, autor y editorial
    query = """
        SELECT 
            libro.titulo, 
            libro.anio_publicacion, 
            autor.nombre AS autor, 
            autor.apellido AS apellido, 
            editorial.nombre AS editorial
        FROM libro
        JOIN autor ON libro.autor_id = autor.autor_id
        JOIN editorial ON libro.editorial_id = editorial.editorial_id;
    """

    # Ejecutar la consulta
    cursor.execute(query)

    libros = []

    for row in cursor.fetchall():
        libro = {
            "titulo": row[0],
            "anio_publicacion": row[1],
            "autor": f"{row[2]} {row[3]}",
            "editorial": row[4]
        }
        libros.append(libro)

    cursor.close()
    connection.close()

    return jsonify(libros)

# Endpoint para agregar un nuevo libro
@app.route('/libros', methods=['POST'])
def add_libro():
    nuevo_libro = request.get_json()

    if not nuevo_libro or 'titulo' not in nuevo_libro or 'autor_id' not in nuevo_libro or 'editorial_id' not in nuevo_libro:
        return jsonify({"error": "Datos incompletos"}), 400

    connection = get_db_connection()
    if connection is None:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500

    cursor = connection.cursor()

    # Consulta SQL para insertar un nuevo libro
    query = """
        INSERT INTO libro (titulo, anio_publicacion, autor_id, editorial_id)
        VALUES (%s, %s, %s, %s);
    """

    try:
        cursor.execute(
            query, 
            (nuevo_libro['titulo'], 
            nuevo_libro['anio_publicacion'], 
            nuevo_libro['autor_id'], 
            nuevo_libro['editorial_id']))
        connection.commit()
    except Exception as e:
        connection.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

    return jsonify({"message": "Libro agregado exitosamente"}), 201

if __name__ == '__main__':
    app.run(debug=True)