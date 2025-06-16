import os
import json
import datetime
import subprocess
import click

@click.group()
def cli():
    pass

@cli.command()
def hello():
    click.echo("Hello, ForgeDG!")

@cli.command()
@click.argument('nazwa')
@click.option('--features', default='', help="Lista funkcji, np. login,api,db")
def nowy_projekt(nazwa, features):
    """Tworzy nowy projekt i wykonuje initial commit."""
    root = os.getcwd()
    proj_path = os.path.join(root, nazwa)
    # 1. Foldery
    for sub in ['src', 'tests', 'docs']:
        os.makedirs(os.path.join(proj_path, sub), exist_ok=True)
    # 2. Inicjalizacja Git
    subprocess.run(['git', 'init'], cwd=proj_path, stdout=subprocess.DEVNULL)
    # 3. Zapis metadata.json
    feature_list = [f.strip() for f in features.split(',')] if features else []
    meta = {
        "name": nazwa,
        "created": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "status": "in-progress",
        "features": feature_list,
        "metrics": {"users": 0, "errors": 0, "lastBuild": None}
    }
    with open(os.path.join(proj_path, 'metadata.json'), 'w') as f:
        json.dump(meta, f, indent=2)
    # 4. Pierwszy commit
    subprocess.run(['git', 'add', '.'], cwd=proj_path)
    subprocess.run(['git', 'commit', '-m', 'Initial commit'], cwd=proj_path, stdout=subprocess.DEVNULL)
    click.echo(f"Projekt '{nazwa}' utworzony z funkcjami {feature_list}. Initial commit gotowy w {proj_path}")

if __name__ == "__main__":
    cli()
