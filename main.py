import paramiko
from scp import SCPClient
server_type="windows"
if server_type.lower() == "linux":
   ssh_client = paramiko.SSHClient()
   ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   ssh_client.connect(hostname=hostname, port=int(port), username=username, password=password)
   ftp_client = ssh_client.open_sftp()
   all_files_in_path = ftp_client.listdir(path=remotefilepath)
   files = all_files_in_path  # fil
   for file in files:
       ftp_client.get(file_remote, file_local) # download file in local
       ftp_client.put(file_local,remoteloc) # chnage the remote location and put any other folder
       ftp_client.remove(file_remote) # remove the file
else:
    ssh_windows = paramiko.SSHClient()
    ssh_windows.load_system_host_keys()
    ssh_windows.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_windows.connect(hostname=hostname, port=int(port), username=username, password=password)
    dirremotefilepath = remotefilepath.replace("*.*", "").replace("/","\\")
    (stdin, stdout, stderr) = ssh_windows.exec_command("dir /b /a-d "+ dirremotefilepath)
    files = stdout.read().decode("utf-8").split("\r\n")
    scp = SCPClient(ssh_windows.get_transport())
    allfiles = [x for x in files if x != ''] # all files fetch
    for file in allfiles:
        file_remote = remotefilepath.replace("*.*", "").replace("/", "\\") + file
        file_local = LOCAL_FILE + file
        scp.get(getfileremote + file, file_local) # download file in local
        scp.put(file_local, client_bk + renamenamefile)# chnage the remote location and put any other folder
        ssh_windows.exec_command('del ' + file_remote) ## remove the file

