(define 
   (problem fetch-coffee)
   (:domain coffee-robot)
   (:objects robotRoom livingRoom kitchen bedroom hall - room
	     d1 d2 d3 d4 - door
	     rob - robot
  )	

   (:init 

   (at rob robotRoom)
	(connects d1 robotRoom hall)
	(connects d1 hall robotRoom)
	(isClosed d1)

   ;; Rest of inital condition  
   ;;

   (connects d2 bedroom hall)
   (connects d2 hall bedroom)
   (isClosed d2)

   (connects d3 livingRoom hall)
   (connects d3 hall livingRoom)
   (isClosed d3)

   (connects d4 kitchen livingRoom)
   (connects d4 livingRoom kitchen)
   (isClosed d4)

   (coffeeInRoom kitchen)
   (emptyHand rob)
   ) 

   ;; The goal state goes here

(:goal 
       (and 
  (connects d1 robotRoom hall)
  (connects d1 hall robotRoom)
  (isClosed d1)

  (connects d2 bedroom hall)
  (connects d2 hall bedroom)
  (isClosed d2)

  (connects d3 livingRoom hall)
  (connects d3 hall livingRoom)
  (isClosed d3)

  (connects d4 kitchen livingRoom)
  (connects d4 livingRoom kitchen)
  (isClosed d4)
  (coffeeInRoom bedroom)
  (emptyHand rob)
  (at rob robotRoom)
  )

))
