@cli.command(name='init-progress')
def init_progress():
    """Utwórz pusty progress.yaml."""
    import os,yaml
    if os.path.exists('progress.yaml'): click.echo('Już masz progress.yaml'); return
    yaml.safe_dump([],open('progress.yaml','w'))
    click.echo('Utworzono progress.yaml')
