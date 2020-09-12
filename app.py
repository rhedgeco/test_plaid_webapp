from plaid import Client

from backend.link_token import LinkToken
from general_falcon_webserver import WebApp

client = Client(client_id='5e2e3527dd6924001167e8e8', secret='0b89f518880456b6f60020f481b3d7', environment='sandbox')

app = WebApp()

app.add_route('link', LinkToken(client))

app.launch_webserver()
