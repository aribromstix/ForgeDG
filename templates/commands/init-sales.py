@cli.command(name='init-sales')
@click.option('--env-file', default='.env', help='Ścieżka do pliku z kluczami Stripe')
def init_sales(env_file):
    """Generuje szkielet webhooka Stripe."""
    import os
    os.makedirs('sales', exist_ok=True)
    handler = os.path.join('sales','webhook.js')
    content = """\
// sales/webhook.js
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
module.exports.handler = async (event) => {
  // TODO: obsłuż checkout.session.completed
  return { statusCode: 200, body: 'OK' };
};
"""
    with open(handler, 'w') as f:
        f.write(content)
    click.echo('Stworzono szkielet webhook: ' + handler)
