import leveldb

db = leveldb.LevelDB('./db')

# single put
db.Put(b'hello', b'hello world')
print(db.Get(b'hello').decode('utf-8'))

# multiple put/delete applied atomically, and committed to disk
batch = leveldb.WriteBatch()
batch.Put(b'hello', b'world')
batch.Put(b'hello again', b'world')
batch.Delete(b'hello')

db.Write(batch, sync = True)