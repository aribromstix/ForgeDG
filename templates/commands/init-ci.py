@cli.command(name='init-ci')
@click.option('--provider', default='github', type=click.Choice(['github','gitlab']))
def init_ci(provider):
    """Generuje plik CI workflow."""
    import os
    root = os.getcwd()
    if provider=='github':
        path=os.path.join(root,'.github/workflows'); os.makedirs(path,exist_ok=True)
        content="name: CI\non: [push]\njobs:\n  build-and-test:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v2\n      - name: Setup Python\n        uses: actions/setup-python@v2\n        with:\n          python-version: '3.x'\n      - name: Install deps\n        run: |\n          pip install -r requirements.txt\n          pip install -e .\n      - name: Run tests\n        run: pytest -q tests --junitxml=results.xml -c /dev/null\n"
        open(os.path.join(path,'ci.yml'),'w').write(content)
    else:
        path=os.path.join(root,'.gitlab'); os.makedirs(path,exist_ok=True)
        content="stages:\n  - test\n\ntest:\n  image: python:3\n  script:\n    - pip install -r requirements.txt\n    - pip install -e .\n    - pytest -q tests --junitxml=results.xml -c /dev/null\n  only:\n    - branches\n"
        open(os.path.join(path,'ci.yml'),'w').write(content)
    click.echo('CI pipeline wygenerowany.')
