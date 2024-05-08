/* eslint-disable no-console */
import redis, { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => { console.log('Redis client connected to the server'); });

function setNewSchool(schoolName, value){
    client.set(schoolName, value, redis.print)
}

function displaySchoolValue(schoolName){
    client.get(schoolName, (err, reply) => {
        if (err) console.error(err);
        else{
            console.log(reply)
        }
    })
}

export default client;

promisify(displaySchoolValue)


displaySchoolValue('Holberton')
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');