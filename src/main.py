from fastapi import FastAPI
import redis


app = FastAPI()

rc = redis.Redis(host='redis', port=6379)



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hits")
async def read_root():
    rc.incr('hits')	
    value = rc.get('hits')
    return {"Number of refresh": value}




