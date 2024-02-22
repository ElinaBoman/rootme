

/* For accepting payment with Stripe: https://stripe.com/docs/payments/accept-a-payment */
  
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
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

// Handle form submit
var form = document.getElementById('payment-form');
form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
            billing_details: {
                name: $trim(form.user_name.value),
                phone:$trim(form.mobile_number.value),
                email:$trim(form.email.value),
                adress: {
                    line1: $trim(form.street_address1.value),
                    line2:$trim(form.street_address2.value),
                    city: $trim(form.city.value),
                    country: $trim(form.country.value),
                    state: $trim(form.state.value),
                }
            }
        },
        shipping: {
                name: $trim(form.user_name.value),
                phone:$trim(form.mobile_number.value),
                adress: {
                    line1: $trim(form.street_address1.value),
                    line2:$trim(form.street_address2.value),
                    city: $trim(form.city.value),
                    country: $trim(form.country.value),
                    postal_code: $trim(form.postal_code.value),
                    state: $trim(form.state.value),
                }
        }, 
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            $('#payment-form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});


