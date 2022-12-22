import uvicorn
import argparse
from webserver import create_app

app = create_app()

parser = argparse.ArgumentParser()
parser.add_argument("--address", "-a",
                    type=str, required=False, 
                    help="IP address to listen on", 
                    default="127.0.0.1")
parser.add_argument("--port",
                    type=int, required=False, 
                    help="Port to connect to", 
                    default=5000)
args = parser.parse_args()


if __name__ == "__main__":
    uvicorn.run("main:app", host=args.address, port=args.port, reload=True)