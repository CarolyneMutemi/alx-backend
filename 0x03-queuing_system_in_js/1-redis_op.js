/* eslint-disable no-console */
import redis, { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => console.log('Redis Client Error', err));
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


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');