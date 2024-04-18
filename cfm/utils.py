import paramiko

def upload_to_cpanel_sftp(local_file_path, remote_file_path, sftp_host, sftp_port, sftp_user, sftp_pass):
    try:
        # Connect to the SFTP server
        transport = paramiko.Transport((sftp_host, sftp_port))
        transport.connect(username=sftp_user, password=sftp_pass)
        sftp = paramiko.SFTPClient.from_transport(transport)

        # Upload the local file to the remote path
        sftp.put(local_file_path, remote_file_path)

        # Close the SFTP connection
        sftp.close()
        transport.close()

        return True
    except Exception as e:
        print(f"SFTP Error: {e}")
        return False