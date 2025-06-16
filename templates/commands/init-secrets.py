@cli.command(name='init-secrets')
@click.argument('vars',required=False)
def init_secrets(vars):
    """Generuje .env.example i .gitignore."""
    import os
    defaults=['STRIPE_KEY=','GPT_KEY=']
    items=vars.split(',') if vars else defaults
    open('.env.example','w').write('\\n'.join(items)+'\\n')
    open('.gitignore','a').write('\\n.env\\n')
    click.echo('Utworzono .env.example i .gitignore')
