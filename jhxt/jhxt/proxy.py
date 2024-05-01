from jupyterhub import proxy


class MultirouteCHP(proxy.ConfigurableHTTPProxy):
    async def add_user(self, user, server_name="", client=None):
        self.log.debug("MultirouteCHP")
        await proxy.ConfigurableHTTPProxy.add_user(self, user, server_name, client)
