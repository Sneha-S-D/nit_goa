

from uagents import Agent, Bureau, Context, Model

class Message(Model):
    message: str

sneha = Agent(name="sneha", seed="sneha recovery phrase")
sarvesh = Agent(name="sarvesh", seed="sarvesh recovery phrase")

@sneha.on_interval(period=3.0)
async def send_message(ctx: Context):
    await ctx.send(sarvesh.address, Message(message="Choose a genre: \n1] Pop\n2] Rap\n3] Jazz\n4] Classical\n5] Sufi"))

@sneha.on_message(model=Message)
async def sneha_message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    genre_choice = int(msg.message.split(": ")[1]) 
    if genre_choice == 1:
        await ctx.send(sarvesh.address, Message(message="You chose Pop genre!"))
        
    elif genre_choice == 2:
        await ctx.send(sarvesh.address, Message(message="You chose Rap genre!"))
    elif genre_choice == 3:
        await ctx.send(sarvesh.address, Message(message="You chose Jazz genre!"))
    elif genre_choice == 4:
        await ctx.send(sarvesh.address, Message(message="You chose Classical genre!"))
    elif genre_choice == 5:
        await ctx.send(sarvesh.address, Message(message="You chose Sufi genre!"))
    else:
        await ctx.send(sarvesh.address, Message(message="Invalid genre choice!"))

@sarvesh.on_message(model=Message)
async def sarvesh_message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    genre_choice = int(input("Enter the number corresponding to the genre you choose: "))
    await ctx.send(sneha.address, Message(message=f"Chosen genre: {genre_choice}"))

bureau = Bureau()
bureau.add(sneha)
bureau.add(sarvesh)
if __name__ == "__main__":
    bureau.run()
