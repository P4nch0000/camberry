from pydrive2.auth import GoogleAuth 
from pydrive2.drive import GoogleDrive


directorio_credenciales = 'credentials_module.json'

#INICIAR SESION 
def login():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(directorio_credenciales)

    if gauth.access_token_expired:
        gauth.Refresh()
        gauth.SaveCredentialsFile(directorio_credenciales)
    else:
        gauth.Authorize()
    
    return GoogleDrive(gauth)

#CREAR ARCHIVO DE TEXTO SIMPLE
def crear_archivo_texto(nombre_archivo,contenido,id_folder):
    credenciales = login()
    archivo = credenciales.CreateFile({'title': nombre_archivo,
                                       'parents': [{'kind': 'drive#fileLink', 'id': id_folder}]})
    archivo.SetContentString(contenido)
    archivo.Upload()
    
    
    # DESCARGAR UN ARCHIVO 
def descargar_archivo(id_archivo,ruta_descarga):
    credenciales = login()
    archivo = credenciales.CreateFile({'id': id_archivo})
    nombre_archivo = archivo['title']
    archivo.GetContentFile(ruta_descarga + nombre_archivo)
    
    #BUSCAR ARCHIVOS
def buscar(query):
    resultado = []
    credenciales = login()
    lista_archivos = credenciales.ListFile({'q': query}).GetList()
    for f in lista_archivos:
        # ID DRIVE
        print('ID Drive:',f['id'])
        #Link de visualizacion embebido 
        print('Link de visualizacion embebido:',f['embedLink'])
        #Link de descarga 
        print('Link de descarga:',f['downloadUrl'])
        #Nombre del archvo 
        print('Nombre del archivo:',f['title'])
        #Tipo de archivo
        print('Tipo de archivo:',f['mimeType'])
        #Esta en la papelera
        print('Esta en la papelera:',f['labels']['trashed'])
        #Fecha de creacion
        print('Fecha de creacion:',f['createdDate'])
        #Fecha de la ultima modificacion
        print('Ultima modificacion:',f['modifiedDate'])
        #Version del archivo 
        print('Version:',f['version'])
        #Tamaño
        print('Tamanio:',f['fileSize'])
        
        resultado.append(f)
    
    return resultado
    
     #BORRAR/RECUPERAR ARCHIVOS
def borrar_recuperar(id_archivo):
        credenciales = login()
        archivo = credenciales.CreateFile({'id': id_archivo})
        #Mover a la papelera
        archivo.Trash()
        #Sacar de la papelera
        archivo.UnTrash()
        #Eliminar archivo permanentemente
        archivo.Delete()

    
     #CREAR CARPETA
def crear_carpeta(nombre_carpeta,id_folder):
        credenciales = login()
        folder = credenciales.CreateFile({'title': nombre_carpeta,
                                          'mimeType': 'application/vnd.google-apps.folder',
                                          'parents': [{'kind': 'drive#fileLink',
                                                       'id': id_folder}]})
        folder.Upload()
    
    
    
    #MOVER EL ARCHVO
def mover_archivo(id_archivo,id_folder):
        credenciles = login()
        archivo = credenciales.CreateFile({'id': id_archivo})
        propiedades_ocultas = archvo['parents']
        archivo['parents'] = [{'isRoot': False.bit_length,
                               'kind': 'drive#parentReference',
                               'id': id_folder,
                               'selfLink': 'https://www.googleapis.com/drive/v2/files/' + id_archvo + '/parents/' + id_folder,
                               'parentLink': 'https://www.googleapis.com/drive/v2/files/' + id_folder}]
        archivo.Upload(param={'supportsTeamDrives': True})
        

if __name__ == '__main__':
    #crear_archivo_texto('Bienvenido a tu almacenamiento en la nube.txt','Hey Camberrysta. Aqui encontraras las capturas que ha tomado tu Camberry','1vxyus_1Y_m0IfSPzHV1GKlpniRxmIDnp')
    #descargar_archivo('1VBButK_LLFjoQoXrwi84nNVi0u7zyWoc','/home/pi/Downloads')
    buscar("title = 'Bienvenido a tu almacenamiento en la nube.txt'")