# hangboardWorkout
Climbing workouts, automated so that you don't have to keep track of time or which exercise you're on.

To run hangboard.sh without music:
```
$ chmod 700 hangboard.sh
$ ./hangboard.sh
```

To run hangboard.sh with background send music:
```
$ chmod 700 hangboard.sh
$ ./hangboard.sh ./path/to/mp3
```
the music runs as a background process, and therefore may not terminate when the program does.
i am lazy so just go to activity monitor and look for afplay, then kill the process
