// sales/webhook.js
const Stripe = require('stripe');
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY || 'sk_test_dummy');

module.exports.handler = async (event) => {
  // TODO: obsłuż checkout.session.completed
  return { statusCode: 200, body: 'OK' };
};
