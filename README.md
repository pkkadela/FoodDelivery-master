# FoodDelivery

This is a food ordering and payment site developed using `django`. It allows the user to select the desired food items from the available list and then checkout and pay using credit card. For payments, it uses stripe.

Before running the code, go to [Stripe](www.stripe.com) and make an account. Then go to the developers section and generate API keys. Then go to the `settings.py` file and replace the placeholders for API keys at the last with your API keys. With this you are good to go.

To run the code, open terminal and `cd` to this directory and then run
```
python manage.py runserver
```
