@cli.command(name='init-legal')
def init_legal():
    """Tworzy NDA i EULA w docs/."""
    import os
    os.makedirs('docs',exist_ok=True)
    open('docs/NDA.md','w').write('# NDA\\nUmowa o zachowaniu poufności...')
    open('docs/EULA.md','w').write('# EULA\\nUmowa licencyjna...')
    click.echo('Utworzono NDA i EULA')
