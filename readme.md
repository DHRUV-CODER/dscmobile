![Header](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=10&height=200&section=header&text=dscmobile)
# Display your Bot's status as Mobile

![img1](https://user-images.githubusercontent.com/60794694/165765114-fdf4d0bc-39b5-43e1-90f0-aa8cddb72ba1.JPG)

![img2](https://user-images.githubusercontent.com/60794694/165764912-46508cf8-0d76-4391-b391-d803e70e0e0d.JPG)

### Steps :
 - Clone the [repo](https://github.com/DHRUV-CODER/dscmobile/archive/refs/heads/main.zip) or `git clone https://github.com/DHRUV-CODER/dscmobile.git`
 - `pip3 install -r requirements.txt` or `pip install -r requirements.txt`
 - `python3 minified_dscmobile.py` or `py minified_dscmobile.py`
 - paste your bot's token and hit enter
 - **to close the session gracefully press `ctrl+c`**
 
 # Running on User's Account , `Against Discord TOS`
 
 - Get [User's Token](https://www.youtube.com/watch?v=WWHZoa0SxCc)
 - Switch to **online mode** 
 - Exit Discord , Close the app or the browser 
 - (`in cli`) paste the token and hit enter , after this you can reopen your app

> I highly recommend to not try on some users account as it may lead to Ban.
> I am not responsible for any kind of malicious activity , use at your own risk.

## Hey how does this thing work ?

I used websockets and followed Discord's [Docs](https://discord.com/developers/docs/topics/gateway) , modified the payload and ran it.

[Discord gateway Boilerplate code](https://github.com/Anurag-gg/discord-gateway) 

You can display your bot's status as mobile by setting `$browser` to `Discord Android` or `Discord iOS` in the identify payload.

```json
{
  "properties": {
    "$browser": "Discord Android"
  }
```
![Alt](https://repobeats.axiom.co/api/embed/0f0a6066974ab8538fc675159ba515d8fda8595e.svg "Repobeats analytics image")
