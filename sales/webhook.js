// sales/webhook.js
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
module.exports.handler = async (event) => {
  // TODO: obsłuż checkout.session.completed
  return { statusCode: 200, body: 'OK' };
};
