

/* For accepting payment with Stripe: https://stripe.com/docs/payments/accept-a-payment */
  
var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

/* CSS for Stripe from here: https://stripe.com/docs/stripe-js */

var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = elements.create('card', {style:style});
card.mount('#card-element');

// Handle realtime validations errors on the card element
card.addEventListener('change', function (e){
    var errorDiv = document.getElementById('card-errors');
    if (e.error) {
        var html = `
        <span class='icon' role='alert'>
            <i class='fas fa-times'></i>
        </span>
        <span>${e.error.message}</span>`;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = "";
    }
})