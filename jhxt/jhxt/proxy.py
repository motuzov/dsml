from jupyterhub import proxy

DAGSTER_PORT = "3000/tcp"


class MultirouteCHP(proxy.ConfigurableHTTPProxy):
    async def add_user(self, user, server_name="", client=None):
        self.log.debug("MultirouteCHP")
        spawner = user.spawners[server_name]
        resp = await spawner.docker("inspect_container", spawner.container_id)
        self.log.debug(resp["NetworkSettings"]["Ports"])
        dagster_server_host_ip = resp["NetworkSettings"]["Ports"]["3000/tcp"][0]
        proto = "https" if user.spawners.internal_ssl else "http"
        dagster_host = f"{proto}://{dagster_server_host_ip['HostIp']}:{dagster_server_host_ip['HostPort']}"
        body = {"target": dagster_host}
        self.log.debug(spawner.proxy_spec)
        path = self._routespec_to_chp_path(f"{spawner.proxy_spec}dag")
        await self.api_request(path, method="POST", body=body)
        await proxy.ConfigurableHTTPProxy.add_user(self, user, server_name, client)
