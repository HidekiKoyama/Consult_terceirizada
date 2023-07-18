from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from conection import Connection
from query import Query
from create_rel import createExcel

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        conn = Connection(); query = Query(); create = createExcel()
        dados, cursor = conn.consulta(query.readDoc()) 
        create.createandsave(dados, cursor)
        print(f'Arquivo modificado: {event.src_path}')

def start_check():
    path = "C:/Users/User/Downloads/PORT/query"
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print("Seu programa está rodando!")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
