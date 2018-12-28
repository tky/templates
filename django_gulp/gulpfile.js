'use strict';

const gulp = require('gulp');
const child = require('child_process');

var server = null;

gulp.task('server:spawn', () => {
  if (server && server !== 'null') {
    server.kill();
  }

  server = child.spawn('python', ['manage.py', 'runserver'], { stdio: 'inherit' });

  server.on('close', (code) => {
    if (code !== 0) {
      console.error('Django runserver exited with error code: ' + code);
    } else {
      console.log('Django runserver exited normally.');
    }
  });

});
gulp.task('default', ['server:spawn'])
