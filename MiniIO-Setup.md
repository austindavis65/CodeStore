# Introduction

MinIO is a high-performance, distributed object storage system that is compatible with the Amazon S3 API. It's built for cloud-native applications and is particularly well-suited for smaller-scale deployments or for teaching purposes due to its simplicity and ease of use.

- S3 Compatibility: This is its key feature. You can use the exact same S3 SDKs and tools they would for Amazon S3, making the transition seamless.
- Ease of Deployment: MinIO can be deployed as a single binary, making it very quick to get up and running.
- High Performance: It's optimized for high-speed read/write operations, which is great for building scalable applications.
- Erasure Coding: MinIO uses a technique called erasure coding to provide data redundancy and durability, similar to how RAID works but for a distributed system.
 
The most common way to install MinIO on a Linux server like Ubuntu is by downloading the standalone binary and setting it up as a systemd service. This method ensures it runs in the background and starts automatically on boot. 🚀

# Assignment Instructions
 
## Installation Steps - Using your FS10 VM (or the server you used as your ISCSI/NFS client)
 
- Download the MinIO Binary: Get the latest MinIO server binary for your system architecture.
 
  - wget https://dl.min.io/server/minio/release/linux-amd64/minioLinks to an external site.
 
- Make it Executable: Grant execution permissions to the downloaded file.
 
- Move to a System Path: Move the binary to a common location like /usr/local/bin so it can be run from any directory.
 
## Configuration and Service Setup
 
- Create a MinIO User and Group: For security, MinIO should run as a non-root user.
 
  - sudo useradd -r minio-user -s /sbin/nologin
 
- Confirm Data Directory: Use an ISCSI LUN directory as the location MinIO will store its object data. -- you set this up in the last assignment --
 
  - sudo mkdir -p /srv/iscsi/lun0/minio-data -- this was my iscsi location -- 
 
- Set Permissions: Give the new minio-user ownership of the data directory.
 
  - sudo chown minio-user:minio-user /srv/iscsi/lun0/minio-data
 
- Create a Configuration File: This file will define important variables like the root user and password, as well as the storage location.
 
  - sudo vi /etc/default/minio
 
  - Add the following content, replacing the user and password with your own secure credentials.

```
MINIO_ROOT_USER="minioadmin"

MINIO_ROOT_PASSWORD="strongpassword"

MINIO_VOLUMES="/srv/iscsi/lun0/minio-data"

MINIO_OPTS="--address :9000 --console-address :9001"
```

- Create a Systemd Service File: This allows you to manage MinIO like any other service (start, stop, enable on boot).

  - sudo vi /etc/systemd/system/minio.service

- Paste the following content:

``` 
[Unit]

Description=MinIO

Documentation=https://docs.min.io

Wants=network-online.target

After=network-online.target



[Service]

User=minio-user

Group=minio-user

EnvironmentFile=/etc/default/minio

ExecStart=/usr/local/bin/minio server $MINIO_VOLUMES $MINIO_OPTS



# Let systemd restart minio if it fails

Restart=always



[Install]

WantedBy=multi-user.target
```

 
- Start and Enable the Service: Reload the systemd daemon, then start and enable the MinIO service to run on startup.
 
  - sudo systemctl daemon-reload

  - sudo systemctl enable minio

  - sudo systemctl start minio

- Access MinIO: After the service starts, you can access the MinIO web console by navigating to http://<your-server-ip>:9001 in your web browser.
 

Here is a video from a similar tutorial on how to get started with MinIO: 

Homelab Series - Creating Self Hosted MinIO Object Storage ServerLinks to an external site.
https://www.youtube.com/watch?v=c4kEFZea7fg



# Tips & Examples
Troubleshooting tips:

Ensure minio is running:  

sudo ss -tulpn | grep minio
