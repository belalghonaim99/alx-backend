import redis from 'redis';

import promisify from 'util';

const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
    });

client.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error.message}`);
    }

function setNewSchool(schoolName, value) {
    client
        .set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
    client
        .get(schoolName, (err, reply) => {
            console.log(reply);
        });
}


export { client, setNewSchool, displaySchoolValue };

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
