import docker
from docker.models.images import Image
from docker.models.containers import _create_container_args


if __name__ == '__main__':
    image='ts:tatest'
    if isinstance(image, Image):
        image = image.id
    device_request = {
            'Driver': '',
            'Capabilities': [['gpu']],
            'Count': -1,  # enable all gpus
            }
    
    client = docker.from_env()
    # create_kwargs
    kwargs = {} 
    kwargs['image'] = image
    kwargs['volumes'] = {'work_v': {'bind': '/home/jovyan/work', 'mode': 'rw'}}
    kwargs['command'] = "start.sh jupyter lab --LabApp.token=''"
    kwargs['version'] = client.containers.client.api._version
    create_kwargs = _create_container_args(kwargs)
    create_kwargs['host_config']['DeviceRequests'] = [device_request]
    client.api.create_container(**create_kwargs)

