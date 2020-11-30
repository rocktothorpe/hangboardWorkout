#!/bin/bash

# purpose:
# this dank bash script is so that i dont
# have to look at a timer or keep track 
# of which exercise im on


updateTime () {
  i=0
  while [ $i -lt 60 ]
  do
    sleep ${1:-1};
    i=$(( $i + 1 ));
    echo $i
  done
}

  for i in $(seq 11); do
    case "$i" in
      1)
        EXERCISE="15 second hang, 3 pull ups on jugs."
        ;;
      2)
        EXERCISE="20 second hang on crimp. Two pull ups on large edge."
        ;;
      3)
        EXERCISE="20 second hang on large edge. 20 second bent arm hang on pocket."
        ;;
      4)
        EXERCISE="30 second hang on jug, 2 pull-ups."
        ;;
      5)
        EXERCISE="20 second hang, large edge, 4 pull ups large edge."
        ;;
      6)
        EXERCISE="3 offset pull ups on jug and crimp."
        ;;
      8)
        EXERCISE="15 knee raises on sloper, 10 second hang on large edge."
        ;;
      9)
        EXERCISE="20 second hang, large edge."
  			;;
  		10)
  			EXERCISE="15 second hang on pocket, 3 pull ups on jug."
  			;;
      11)
        EXERCISE="hang as long as possible, long edge."
        ;;
    esac

    echo "$EXERCISE";
  	updateTime;
    say "NEXT";
  done;





