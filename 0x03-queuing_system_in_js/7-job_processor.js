import createqueue , job from kue;

const blackList = ['4153518780', '4153518781'];

const queue = createqueue();

const sendNotification = (phoneNumber, message, job, done) => {
    if (blackList.includes(phoneNumber)) {
        return done(Error(`Phone number ${phoneNumber} is blacklisted`));
    }
    job.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
}

queue.process('push_notification_code_2', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

queue.on('error', (error) => {
    console.error(`Notification job failed: ${error.message}`);
});