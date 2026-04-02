import os
import uvicorn
from Mark_down import app
import argparse
def main():
    parser = argparse.ArgumentParser(description='Caching Server')
    parser.add_argument('--port', type=int, help='Port to run the caching server on')
    args = parser.parse_args()

    os.environ["_port_"]=str(args.port)
    uvicorn.run("Mark_down:app", host="localhost", port=args.port , reload=True)   
    print(uvicorn.Server)
if __name__ == "__main__":
    main()