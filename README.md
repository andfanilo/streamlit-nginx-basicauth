# Quick & Dirty Streamlit + NGinx Basic Auth test

Reverse-proxy NGinx doing Basic Authentication, passing Auth user through Websocket headers and Streamlit extracting auth login from websocket headers to customize page per user logging in.

![](./demo.mp4)

## Run

```sh
docker-compose up --build
```

Credentials: user1/user1, user2/user2, user3/user3
