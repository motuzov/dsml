from dockerspawner import dockerspawner


class DSMLDockerSpawner(dockerspawner.DockerSpawner):
    async def start(self):
        res = await dockerspawner.DockerSpawner.start(self)
        self.log.debug("DSMLDockerSpawner")
        return res
