import sqlite3
import os
import hashlib

DB_FILE = 'myfiledb.db'


def create_connection(db_file):
  conn = sqlite3.connect(db_file)
  return conn


def create_table(conn):
  sql = '''CREATE TABLE IF NOT EXISTS files
             (id INTEGER PRIMARY KEY, filename TEXT, filehash TEXT, file BLOB)'''
  c = conn.cursor()
  c.execute(sql)


def insert_file(conn, file):
  sql = 'INSERT INTO files (filename, filehash, file) VALUES (?,?,?)'
  c = conn.cursor()

  with open(file, 'rb') as f:
    data = f.read()
    filehash = hashlib.md5(data).hexdigest()
    filename = os.path.basename(file)

  c.execute(sql, (filename, filehash, data))
  conn.commit()


def retrieve_file(conn, id):
  sql = 'SELECT * FROM files WHERE id=?'
  c = conn.cursor()
  c.execute(sql, (id, ))
  file_data = c.fetchone()

  file_blob = file_data[3]
  filename = file_data[1]

  with open('output/' + filename, 'wb') as f:
    f.write(file_blob)


def main():
  conn = create_connection(DB_FILE)
  create_table(conn)

  #simple file_saver storage
  file = 'path/to/file'
  insert_file(conn, file)
  retrieve_file(conn, 1)

  conn.close()


if __name__ == '__main__':
  main()
