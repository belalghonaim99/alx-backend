import sinson from 'sinon';

import { Job } from './7-job';
import { createPushNotificationsJobs } from './8-job';

describe('createPushNotificationsJobs', () => { 
    it('logs each job as it is created', () => {
        const consoleSpy = sinon.spy(console, 'log');
        const jobs = [
            { phoneNumber: '4153518780', message: 'This is the code 1234 to verify your account' },
            { phoneNumber: '4153518781', message: 'This is the code 4562 to verify your account' }
        ];
        createPushNotificationsJobs(jobs);
        expect(consoleSpy.calledWith('Notification job created:')).to.be.true;
        consoleSpy.restore();
    });
});

