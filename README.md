# Pyttribution.io
[![PyPI](https://img.shields.io/pypi/dm/pyttributionio.svg)](https://pypi.python.org/pypi/pyttributionio)     
     
A Python wrapper around the Attribution.io API

## Installation

```
pip install pyttributionio
```

## Usage

Create an instance of the `PyttributionIo()` class while passing your API credentials:

```
pyttributionio = PyttributionIo(
    api_key=[YOUR_API_KEY],
    api_secret=[YOUR_API_SECRET],
)
```

After creating an instance of the class, there are two types of API's one can use.

#### Private API
There's the private one which can be used to retrieve information about any customer within
your Attribution.io account.
There are six options to choose from, they are increasing in returned information quantity:
- `pyttributionio.fetch_customer_info_base(client_id)`:     
Returns just the base information set of the chosen customer
- `pyttributionio.fetch_customer_info_pageviews(client_id)`:     
Returns just the base information set as well as all the pageviews of the chosen customer
- `pyttributionio.fetch_customer_info_touchpoints(client_id)`:     
Returns just the base information set as well as all the touchpoints of the chosen customer
- `pyttributionio.fetch_customer_info_events(client_id)`:     
Returns just the base information set as well as all the events of the chosen customer
- `pyttributionio.fetch_customer_info_identities(client_id)`:     
Returns just the base information set as well as all the identities of the chosen customer
- `pyttributionio.fetch_customer_info_full(client_id)`:     
Returns just the base information set as well as all information from before combined of the chosen customer

As `client_id` one needs to pass an identity used earlier to identify a customer. It can be anything, an integer-based ID, email address etc.


#### Public API
Next to the private API, I also implemented the public API, so that part that the JavaScript snippet is normally POSTing to.

You have two options to programmatically use the public API with this wrapper:
- Triggering identities:    
```
pyttributionio.trigger_identity(
    attributionio_id,
    client_id[optional],
    user_agent[optional],
)
```     

- Triggering events:     
```
pyttributionio.trigger_event(
    attributionio_id,
    event_key,
    client_id[optional],
    user_agent[optional],
    last_url[optional],
)
```     

You need to pass the ID from the cookie which the Attribution.io JavaScript snippet creates for each visitor of your sites as the `attributionio_id`.
The key/name of the cookie in the browser is: `AttrioP_[YOUR_API_KEY]`         
With events you also need to pass an `event_key` which you need to set within the Dashboard of Attribution.io.     
     
Optionally you can pass a custom `client_id` which can be an integer-based ID, an email address etc.
If you don't pass it the wrapper will generate a random identity for you, otherwise events will not be counted.
Additionally, you can pass a user-agent of the customer and the last URL he or she visited on one of your sites.


License
-------

[MIT](LICENSE.txt)
