import createquee from kue;

const queue = createquee;

const sendNotification = (phoneNumber, message) => {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}


queue.process('push_notification_code', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message);
    done();
});

queue.on('error', (error) => {
    console.error(`Notification job failed: ${error.message}`);
});

