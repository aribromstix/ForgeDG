@cli.command(name='dockerize')
@click.option('--base',default='python:3.12-slim')
@click.option('--port',default=8080)
def dockerize(base,port):
    """Tworzy Dockerfile i docker-compose."""
    import os
    content=f"FROM {base}\nWORKDIR /app\nCOPY . /app\nRUN pip install -e .\nCMD [\"forge\",\"hello\"]\n"
    open('Dockerfile','w').write(content)
    dc="version: '3'\nservices:\n  app:\n    build: .\n    ports:\n      - \"{port}:{port}\"\n"
    open('docker-compose.yml','w').write(dc)
    click.echo('Dockerfile i docker-compose wygenerowane.')
