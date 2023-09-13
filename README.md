# netsuite_oauth_python
A python library implements OAuth1 to enable users to connect to Netsuite's REST API.

## Usage
<pre><code>url = 'https://1234567.restlets.api.netsuite.com/app/site/hosting/restlet.nl?script=1234&deploy=1&params=value'
consumerKey = '123456789012345678901234567890123456789012345678901234567890abcd'
consumerSecret = '123456789012345678901234567890123456789012345678901234567890abcd'
tokenId = '123456789012345678901234567890123456789012345678901234567890abcd'
tokenSecret = '123456789012345678901234567890123456789012345678901234567890abcd'
account = '1234567'
print(NetsuiteOauth(url, consumerKey, consumerSecret, tokenId, tokenSecret, account).get().content)</code></pre>

## Maintainers

[@karthous](https://github.com/karthous)

## Disclaimer

This is not an official product of Oracle or Netsuite.
Use at your own risk.
By using this software, you agree **not** to:

1. Violates any laws.
2. Produces any harm to a person or persons.
3. Disseminates (spreads) any personal information that would be meant for harm.
4. Spreads misinformation.
5. Target vulnerable groups.
