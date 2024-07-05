from flask import Blueprint, request, jsonify
from models import mysql  # Pastikan modul 'mysql' sudah di-import dengan benar

bp = Blueprint('tiket', __name__)

# Menambahkan tiket baru
@bp.route('/tiket', methods=['POST'])
def tambah_tiket():
    data = request.get_json()
    nama = data['nama']
    tanggal = data['tanggal']
    jumlah_tiket = data['jumlah_tiket']
    total = data['total']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO tiket (nama, DATE, jumlah_tiket, total) VALUES (%s, %s, %s, %s)",
                (nama, tanggal, jumlah_tiket, total))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Tiket berhasil ditambahkan'})

# Mendapatkan semua tiket
@bp.route('/tiket', methods=['GET'])
def get_semua_tiket():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, nama, DATE, jumlah_tiket, total FROM tiket")
    tikets = cur.fetchall()
    cur.close()

    return jsonify([{
        "id": tiket[0],
        "nama": tiket[1],
        "tanggal": tiket[2],
        "jumlah_tiket": tiket[3],
        "total": tiket[4]
    } for tiket in tikets])

# Menghapus tiket berdasarkan ID
@bp.route('/tiket/<int:id>', methods=['DELETE'])
def hapus_tiket(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tiket WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Tiket berhasil dihapus'})

# Mengupdate tiket berdasarkan ID
@bp.route('/tiket/<int:id>', methods=['PUT'])
def update_tiket(id):
    data = request.get_json()
    nama = data.get('nama')
    tanggal = data.get('tanggal')
    jumlah_tiket = data.get('jumlah_tiket')
    harga_per_tiket = 10000  # Ganti dengan harga per tiket di tempat wisata yang sesuai

    total = jumlah_tiket * harga_per_tiket

    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE tiket
        SET nama = %s, DATE = %s, jumlah_tiket = %s, total = %s
        WHERE id = %s
    """, (nama, tanggal, jumlah_tiket, total, id))
    mysql.connection.commit()
    cur.close()

    return jsonify({'message': 'Tiket berhasil diupdate'})
