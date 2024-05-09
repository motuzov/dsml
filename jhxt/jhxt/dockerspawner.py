from dockerspawner import dockerspawner


class DSMLDockerSpawner(dockerspawner.DockerSpawner):
    async def start(self):
        res = await dockerspawner.DockerSpawner.start(self)
        self.log.debug("DSMLDockerSpawner")
        return res

    def _volumes_to_binds(self, volumes, binds, mode="rw"):
        self.log.debug(f"DSMLDockerSpawner volume_binds ->> {self.user.name}")
        return dockerspawner.DockerSpawner._volumes_to_binds(
            self, volumes, binds, mode="rw"
        )
