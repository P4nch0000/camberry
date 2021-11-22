from pydrive2.auth import GoogleAuth 
from pydrive2.drive import GoogleDrive

directorio_credenciales = ' /home/pi/Documents/Camberry/credentials_module.json'


#INICIAR SESION 
def login():
    GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = directorio_credenciales
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(directorio_credenciales)

    if gauth.credentials is None:
        gauth.LocalWebserverAuth(port_numbers=[8092])
    elif gauth.access_token_expired:
        gatuh.Refresh()
    else:
        gauth.Authorize()
        
    gauth.SaveCredentialsFile(directorio_credenciales)
    credenciales = GoogleDrive(gauth)
    return credenciales


#ENLISTAR PERMISOS ACTUALES
def enlistar_permisos_actuales(id_drive):
    drive = login()
    file1 = drive.CreateFile({'id': id_drive})
    permissions = file1.GetPermissions()
    lista_de_permisos = file1['permissions']

    for permiso in lista_de_permisos:
        print('ID PERMISO: {}'.format(permiso['id': id_drive]))
        print('ROLE: {}'.format(permiso['role']))
        print('TYPE: {}'.format(permiso['type']))

        #EMAIL
        if permiso.get('emailAddress'):
            print('EMAIL: {}'.format(permiso['emailAddress']))

        
        #NOMBRE 
        if permiso.get('name'):
            print('NAME: {}'.format(permiso['name']))


    print('===============================================')


#INSERTAR/ OTORGAR PERMISOS
def insertar_permisos(id_drive,type,value,role):
    drive = login()
    file1 = drive.CreateFile({'id':id_drive})
    #VALUE (EMAIL AL QUE SE LE ATORGA PERMISOS
    permission = file1.InsertPermission({'type':type,'value':value,'role':role})
    
    
#ELIMINAR PERMIOS
def eliminar_permisos(id_drive,permission_id = None,email = None):
    drive = login()
    file1 = drive.CreateFile({'id': id_drive})
    permissions = file1.GetPermissions()
    if permission_id:
        file1.DeletePermission(permission_id)
    elif email:
        for permiso in permissions:
            if permiso.get('emailAddress'):
                if permiso.get('emailAddress') == email:
                    file1.Deletepermission(permiso['id'])


if __name__ == "__main__":
    
    id_drive = '1vxyus_1Y_m0IfSPzHV1GKlpniRxmIDnp'
    type = 'user'
    value = 'jimenezfabian250@gmail.com'
    role = 'reader'
    enlistar_permisos_actuales(id_drive)
    insertar_permisos(id_dtrive,type,value,role)