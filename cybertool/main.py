import typer

import crypto

from cryptoTypes import EncodeType,encoders,decoders
from cryptoTypes import HashType,hashers



app = typer.Typer()


@app.command()
def hello(name: str):
    print(f"Hello {name}!")


@app.command()
def goodbye(name: str,formal:bool = False):
    if formal:
        print(f"Goodbye Mr/Ms {name}!")
    else:
        print(f"Goodbye {name}!")
    




@app.command()
def encode(type: EncodeType, text:str):
    print(encoders[type](text))

@app.command()
def decode(type: EncodeType, text:str):
    print(decoders[type](text))



@app.command()
def hash(type: HashType, text:str):
    print(hashers[type](text))









if __name__ == "__main__":
    app()