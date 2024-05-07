import redis from 'redis';
import client from "./2-redis_op_async";

const schoolsInCity = {
    'Portland': 50,
    'Seattle': 80,
    'New York': 20,
    'Bogota': 20,
    'Cali': 40,
    'Paris': 2
  }

for (const city in schoolsInCity){
    client.hset('HolbertonSchools', city, schoolsInCity[city], redis.print)
}

client.hgetall('HolbertonSchools', (err, result) => {
    if (err) console.error(err);
    else {
        console.log(result)
    }
})