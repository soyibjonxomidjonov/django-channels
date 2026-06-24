import asyncio
import redis.asyncio as redis


async def main():
    r = redis.Redis(host="127.0.0.1", port=6379)
    result = await r.ping()
    print("PING natijasi:", result)
    await r.aclose()


if __name__ == "__main__":
    asyncio.run(main())