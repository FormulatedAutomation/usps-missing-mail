![FA Github Header](https://user-images.githubusercontent.com/2868/98735818-fabe8a80-2371-11eb-884a-e555e31aa348.png)

# USPS Missing Mail Bot

This bot logs into an e-commerce system, looks up a shipment 
based on that criteria and files a missing package claim with USPS.  In order to 
file the claim, the tracking number we need to be in an undelivered state.

![USPS-Playwright](https://user-images.githubusercontent.com/1809823/103577443-d7f8b000-4ea2-11eb-8b3d-b84e5a8e0f4b.gif)


# Local Installation

1.  Clone the repo
2.  Install the dependencies using `rcc`
3.  Create a `.env` with the following variables:

```
PLATFORM_URL='https://shopify.store.com/'
PLATFORM_USERNAME='your.username'
PLATFORM_PASSWORD='your.password'
RC_API_SECRET_HOST=''
RPA_SECRET_MANAGER='RPA.Robocloud.Secrets.FileSecrets'
RPA_SECRET_FILE='/path/to/vault.json'
PLATFORM_URL='https://path.to.your.store'
CONTACT_EMAIL='contact@email.com'
CONTACT_FIRST='Person'
CONTACT_LAST='Last'
ORIGIN_COMPANY='Company Name'
ORIGIN_STREET='123 W Main'
ORIGIN_ZIP='11231'
ORIGIN_CITY='New York'
ORIGIN_STATE='NY - New York'
ORIGIN_PHONE='123-123-1234'
```

# Running

The bot runs as an Assistant Bot on Robocorp or you can just run it with pure python as `python task.py`

Keep in mind, this bot expects to log into an e-commerce platform and search for the shipment and it's delivery address.  This will need to be customized to work with your e-commerce platform.  

# Questions

Reach out to us at hello@formulatedautomation.com