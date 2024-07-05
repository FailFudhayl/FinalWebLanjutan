from flask import Blueprint, request, jsonify
from models import mysql

bp = Blueprint('komentar', __name__)

# Menambahkan komentar baru
@bp.route('/komentar', methods=['POST'])
def tambah_komentar():
    data = request.get_json()
    print('Received POST request with data:', data)
    nama = data['nama']
    komentar = data['komentar']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO komentar (nama, komentar) VALUES (%s, %s)", (nama, komentar))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Komentar berhasil ditambahkan'})

# Mendapatkan semua komentar
@bp.route('/komentar', methods=['GET'])
def get_semua_komentar():
    print('Received GET request')
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, nama, komentar FROM komentar")
    komentars = cur.fetchall()
    cur.close()

    return jsonify([{
        "id": komentar[0],
        "nama": komentar[1],
        "komentar": komentar[2]
    } for komentar in komentars])

# Menghapus komentar berdasarkan ID
@bp.route('/komentar/<int:id>', methods=['DELETE'])
def hapus_komentar(id):
    print(f'Received DELETE request for id: {id}')
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM komentar WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Komentar berhasil dihapus'})
