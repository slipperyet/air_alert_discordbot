import disnake
from disnake.ext import commands
import os
import asyncio
import time
from datetime import datetime
from dotenv import load_dotenv
from alerts_in_ua import Client as AlertsClient

load_dotenv()


class Alert(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Cog loaded: {self.qualified_name}')
        alerts_client = AlertsClient(token=os.getenv("API_KEY"))
        active_alerts = alerts_client.get_active_alerts()
        previous_alerts = set()
        channel = self.bot.get_channel(int(os.getenv("CHANNEL_ID"))) 

        while True:
            active_alerts = alerts_client.get_active_alerts()
            current_alerts = {alert.id: alert for alert in active_alerts}
    
            for alert_id, alert in current_alerts.items():
                if alert_id not in previous_alerts:
                        # Новая тревога
                    message = disnake.Embed(title="Новая тревога",
                                            description=f"{alert.location_title}",
                                            color=disnake.Colour.red(),
                                            timestamp=datetime.now())
                    await channel.send(embed=message)

            await asyncio.sleep(60)



def setup(bot: commands.Bot):
    bot.add_cog(Alert(bot))