import {express} from 'express';
import { promisify  } from 'util';
import { createClient } from 'redis';
import {createqueue} from kue;

const app = express();
const client = createClient({name: 'reverse', host: 'localhost', port: 6379});
const queue = createqueue();

client.on('connect', () => {

    console.log('Redis client connected to the server');
}
client.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error.message}`);
});

queue.process('push_notification_code', (job, done) => {
    console.log(`Sending notification to ${job.data.phoneNumber}, with message: ${job.data.message}`);
    done();
}
queue.on('error', (error) => {
    console.error(`Notification job failed: ${error.message}`);
});

app.get('/jobs', async (req, res) => {
    const jobs = await promisify(client.get).bind(client)('push_notification_code');
    res.json(jobs);
}
app.listen(1245);



