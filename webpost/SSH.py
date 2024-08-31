import paramiko


def ssh_tranfer(server, password, src, destination):
    transport = paramiko.Transport((server, 22))
    transport.connect(username='root', password=password)

    sftp = paramiko.SFTPClient.from_transport(transport)

    sftp.put(src, destination)

    transport.close()