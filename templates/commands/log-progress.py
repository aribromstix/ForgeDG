@cli.command(name='log-progress')
@click.argument('etap')
def log_progress(etap):
    """Dodaj wpis do progress.yaml."""
    import os,yaml,datetime
    if not os.path.exists('progress.yaml'): click.echo('Brak progress.yaml'); return
    data=yaml.safe_load(open('progress.yaml')) or []
    entry={'data':str(datetime.date.today()),'etap':etap,
           'status':click.prompt('Status',default='success'),
           'uwagi':click.prompt('Uwagi',default='')}
    data.append(entry)
    yaml.safe_dump(data,open('progress.yaml','w'))
    click.echo('Zapisano wpis')
