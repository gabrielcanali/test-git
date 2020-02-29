import discord
import asyncio
import random
import os

cliente_discord = discord.Client()

@cliente_discord.event
async def on_ready():
    print('LIGOU')

@cliente_discord.event
async def on_message(texto):
    if (texto.author.id == 'Id'): return
    if texto.content.startswith('Bot'): #Se uma frase tiver Bot no inico
        frase = texto.content[3:].strip() #Tira 'Bot' da frase
        if frase.lower().startswith('dado'): #ATira dado de 1 a 6
                        numr = random.randint(1,6)
                        print('oe')
                        await cliente_discord.send(texto.channel,str(numr))
                        return
        if frase.endswith('?'):
                        resposta = random.choice(['Não respondo a isso','Sim','As vezes','Não','Claro','NUNCA!','Um dia talvez','A resposta está dentro de ti','Mais ou menos','Uma Bosta','Podia ser pior'])
                        await cliente_discord.send(texto.channel,resposta)
                        return
cliente_discord.run('Token')
