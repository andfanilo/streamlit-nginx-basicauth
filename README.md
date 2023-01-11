# Quick & Dirty Streamlit + NGinx Basic Auth test

Reverse-proxy NGinx doing Basic Authentication, passing Auth user through Websocket headers and Streamlit extracting auth login from websocket headers to customize page per user logging in.

https://user-images.githubusercontent.com/5351877/211841786-0b2fe620-1e56-427a-8225-9f8919ecb956.mp4

## Run

```sh
docker-compose up --build
```

Credentials: user1/user1, user2/user2, user3/user3
