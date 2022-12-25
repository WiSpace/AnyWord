import argparse, os, requests, configparser

parser = argparse.ArgumentParser(
    prog="AnyWord LIB",
    description = "package maneger for anyword"
)
parser.add_argument('-i', '--install')
parser.add_argument('-u', '--upload')
parser.add_argument('-c', '--create')

args = parser.parse_args()

path, _ = os.path.split(__file__)

if args.install:
    files = requests.get("https://awlib.wsm001.repl.co/lib/%s/files" % args.install).json()

    for file in files:
        content = requests.get("https://awlib.wsm001.repl.co/download", json={"path":file})

        with open(os.path.join(path, "lib", os.path.basename(file)), "wb") as f:
            f.write(content.content)
elif args.create:
    config = configparser.ConfigParser()
    config.read(args.create)

    requests.post("https://awlib.wsm001.repl.co/create", json={
            "name": config["settings"]["name"],
            "desc": config["create"]["description"],
            "password": config["settings"]["password"]
        }
    )
elif args.upload:
    config = configparser.ConfigParser()
    config.read(args.upload)

    for (dirpath, dirnames, filenames) in os.walk(config["upload"]["folder"]):
        for file in filenames:
            files = {"file":open(os.path.join(config["upload"]["folder"], file), "rb")}
            
            requests.post("https://awlib.wsm001.repl.co/upload", 
                headers={
                    "lib": config["settings"]["name"],
                    "passwd": config["settings"]["password"]
                },
            files=files)
else:
    parser.print_help()
