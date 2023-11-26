# Configuration file for jupyterhub.

c = get_config()  #noqa

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# specify that DockerSpawner should accept any image from user input
c.DockerSpawner.allowed_images = {
    'Jupyteo All-In-One': 'jupyter/scipy-notebook',
    'Jupyteo EO Processing': 'ts:tatest'
}

c.JupyterHub.admin_users = set(["dsml"])

#c.DockerSpawner.extra_create_kwargs.update({'gpus', '--all'})

#c.DockerSpawner.volume_mount_points
#c.DockerSpawner.mem_limit
#c.DockerSpawner.volumes = {'/home/user1/': {'bind': '/mnt/vol2', 'mode': 'rw'},
# '/var/www': {'bind': '/mnt/vol1', 'mode': 'ro'}}

#c.DockerSpawner.volumes = {
#    '/path/on/host': '/path/in/container'
#}


from jupyter_client.localinterfaces import public_ips

c.JupyterHub.hub_ip = public_ips()[0]
print(c.JupyterHub.hub_ip)
print('---------config-----------')
#notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
#notebook_dir = '/home/jovyan/work'
#c.DockerSpawner.notebook_dir = notebook_dir

# Mount the real user's Docker volume on the host to the notebook user's
# notebook directory in the container
#c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }
c.DockerSpawner.volumes = { 'work_v': '/home/jovyan/work/work_v'}
c.DockerSpawner.read_only_volumes = { 'work_v': '/home/jovyan/work/work_vro'}
# {username}
#c.JupyterHub.hub_ip = "0.0.0.0"
#c.DockerSpawner.allowed_images = "*"
#c.DockerSpawner.image = "jupyter/scipy-notebook"
c.DockerSpawner.image = "ts:tatest'"
c.DockerSpawner.mem_limit = '8G'
import docker

c.DockerSpawner.extra_host_config = {
    "device_requests": [
        docker.types.DeviceRequest(
            count=-1,
            capabilities=[["gpu"]],
        ),
    ],
}

#c.DockerSpawner.cmd = ["start.sh"]
#c.DockerSpawner.default_url = '/lab'
#c.DockerSpawner.notebook_dir = '/home/{username}'
c.DockerSpawner.environments = {
    'DSML_USER': '{username}'
}

