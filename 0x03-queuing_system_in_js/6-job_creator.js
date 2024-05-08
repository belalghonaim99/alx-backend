import createquee from kue;

const queue = createquee({name: push_notification_code});

const job = queue.create(push_notification_code, {
    phoneNumber: '',
    message: '';

});

job.on ('enqueue', () => {
    console.log(`Notification job created: ${job.id}`);
}
job.on('complete', () => {
    console.log('Notification job completed');
}


job.on('failed', () => {
    console.log('Notification job failed');
});


job.save();


