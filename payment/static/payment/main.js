console.log("Sanity check!");

fetch("config/")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);
  document.querySelector("#submitBtn").addEventListener("click", () => {
    fetch("create-checkout-session/")
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
  });
});