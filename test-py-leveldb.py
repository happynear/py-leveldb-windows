import leveldb

db = leveldb.LevelDB('./db')

# single put
db.Put('hello', 'hello world')
print db.Get('hello')

# multiple put/delete applied atomically, and committed to disk
batch = leveldb.WriteBatch()
batch.Put('hello', 'world')
batch.Put('hello again', 'world')
batch.Delete('hello')

db.Write(batch, sync = True)