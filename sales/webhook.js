const Stripe = require('stripe');
const stripe = new Stripe(process.env.STRIPE_SECRET_KEY || 'sk_test_dummy');// sales/webhook.js
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
module.exports.handler = async (event) => {
  // TODO: obsłuż checkout.session.completed
  return { statusCode: 200, body: 'OK' };
};
