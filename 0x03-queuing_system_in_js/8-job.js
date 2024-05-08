import queue, job from kue;


export const createPushNotificationsJobs = (jobs, queue) => {
    jobs.forEach((job) => {
        const job = queue.create('push_notification_code_2', job);
    
        job.on('enqueue', () => {
            console.log(`Notification job created: ${job.id}`);
        });
    
        job.on('complete', () => {
            console.log(`Notification job ${job.id} completed`);
        });
    });
    }

    job.save();