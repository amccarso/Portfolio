
(define (domain coffee-robot)
   (:requirements :typing)
   (:types room door robot)
   (:predicates	
		(adj ?r1 ?r2 - room)
		(connects ?d - door ?r1 ?r2 - room)
		(isOpen ?d - door)
		(isClosed ?d - door)
		(coffeeInRoom ?r - room)
		(holdCoffee ?rob - robot)
		(emptyHand ?rob - robot)
		(at ?rob - robot ?r - room)
		)		

;; Notice how opening a door that connects two rooms 
;; adds the adjacency predicates in the effect	

(:action open
	:parameters (?d - door ?r1 ?r2 - room ?rob - robot)
	:precondition (and (isClosed ?d) (connects ?d ?r1 ?r2) (at ?rob ?r1) (emptyHand ?rob) )
	:effect (and (isOpen ?d) (adj ?r1 ?r2) (adj ?r2 ?r1)  (not (isClosed ?d))) 
)


(:action close
	:parameters (?d - door ?r1 ?r2 - room ?rob - robot)
	:precondition (and (isOpen ?d) (adj ?r1 ?r2) (adj ?r2 ?r1) (connects ?d ?r1 ?r2) (at ?rob ?r1) (emptyHand ?rob) )
	:effect (and (isClosed ?d) (not (adj ?r1 ?r2)) (not (adj ?r2 ?r1)) 
	(not (isOpen ?d)) )
)

(:action move
	:parameters (?d - door ?r1 ?r2 - room ?rob - robot)
	:precondition (and (at ?rob ?r1) (isOpen ?d) (adj ?r1 ?r2) (adj ?r2 ?r1) (connects ?d ?r1 ?r2) )  
	:effect (and (at ?rob ?r2) (not (at ?rob ?r1)) )  
)


(:action grabCoffee
	:parameters (?rob - robot ?r - room)
	:precondition (and (at ?rob ?r) (coffeeInRoom ?r) (emptyHand ?rob) )
	:effect (and (at ?rob ?r) (coffeeInRoom ?r) (not (emptyHand ?rob))
	(holdCoffee ?rob) )
)

(:action dropOffCoffee
	:parameters (?rob - robot ?r - room)
	:precondition (and (at ?rob ?r) (coffeeInRoom ?r) 
	 (holdCoffee ?rob) )
	:effect (and (emptyHand ?rob) (not (holdCoffee ?rob)) )
)

)

