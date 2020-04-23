type 'a str = Cons of 'a * ('a stream)
   and  
'a stream = unit -> 'a str

let head (s: 'a stream) = let Cons(a, _) = s() in a
let tail (s: 'a stream) = let Cons(_, tl)= s() in tl

let rec take (n:int) (s: 'a stream) : 'a list = 
  if n>0 then 
  (head s) :: (take (n-1) (tail s))
  else []

let rec map (f: 'a -> 'b) (s:'a stream) : 'b stream =
  fun () -> Cons (f (head s), map f (tail s))
                      
let rec zip f s1 s2 () = Cons (f (head s1) (head s2), zip f (tail s1) (tail s2))

let rec filter (s: 'a stream) (p: 'a -> bool) : 'a stream = 
   if p (head s)  then fun () -> Cons (head s, filter (tail s) p)
   else 
     (filter (tail s) p)

let rec sieve (s: int stream) : int stream =
     fun () -> Cons(head s, 
        sieve (filter (tail s) (fun x -> x mod (head s) <> 0)))

let rec nats (i: int) : int stream = fun () -> Cons (i, nats (i+1))

let primes : int stream = sieve (nats 2)

let even x= (x mod 2) = 0
let odd  x= (x mod 2) = 1

let rec fibs () = Cons (0,fun () -> Cons(1, zip (+) fibs (tail fibs)))
let rec ones = fun () -> Cons (1, ones)
let rec zeros = fun () -> Cons (0, zeros)

                            
                               (*************************************)
                               (*************************************)
                               (******* ASSIGNMENT STARTS HERE ******)
                               (*************************************)
                               (*************************************)

(*  define evens: int stream
 *  as the stream of all even natural 
 *  numbers
 *)
 let (evens : int stream) = filter (nats 0) even
(*need to maintain type of int stream, need to make list that increases by 2 with each addition*)     

(*  define odds: int stream
 *  as the stream of all odd natural 
 *  numbers
 *)
 let (odds : int stream) = filter (nats 1) odd

(*  define a function write_list_int: string -> int list -> unit
 *  that takes the name of a file, a list of integers and writes
 *  all the elements of the list in the file, from left to right, 
 *  one per line, and then returns unit.
 *  Remember to close any possible channel before ending.
 *)
 open Printf
 
 let rec write oc l =
       match l with 
       | [] -> ()
       | hd :: tl -> Printf.fprintf oc "%d\n" (hd);
           write (oc) (tl)
           
 let write_list_int (file : string) (l : int list) : unit =
     let oc = open_out file in
     write oc l;
     close_out oc
       
       
(*  define a function read_list_int_rev: string -> int list
 *  that takes the name of a text file (which contains one integer per line) 
 *  and returns a list of all the integers in reversed order. That is 
 *  if the file looks like this: 
 *  1
 *  2
 *  3
 *  the returned list has to be [3;2;1] .
 *  Finally, remember to close any input channel before ending.
 *) 
 let read file = 
     let lines = ref [] in
     let ic = open_in file in
         try
         while true; do
             lines := input_line ic :: !lines
             done; !lines
        with End_of_file ->
            close_in ic; 
            let lines = List.rev !lines in
            List.rev lines
     
 let read_list_int_rev (file : string) : int list =
     let stringlist = read file in 
         List.map (int_of_string) stringlist
        

(*  define a function check_even_sum: string -> int -> (int list * int list * bool) 
 *  that takes the name of a file and a positive integer n and writes in the file 
 *  the list of the first n even numbers using write_list_int. 
 *  Let's call the previous list leven. 
 *  It then reads back from the same file using read_list_int_rev 
 *  and returns the list of integers levenread.
 *  Finally, the function returns a tuple of three elements. The three elements
 *  are leven, levenread, and a boolean which is true if the sum of all the elements
 *  in leven is the same as the sum of all the elements in levenread and false otherwise.
 *)
   
let rec sum (l : int list) : int = 
    match l with  
    | [] -> 0
    | head :: tail -> head + sum tail   
    
 let check_even_sum (file : string) (n : int) : (int list * int list * bool) =
     let leven = take n evens in
         let _ = write_list_int file leven in
         let levenread = read_list_int_rev file in
         (leven, levenread, sum leven = sum levenread )
 
 (* create leven using take 10 evens, write leven to file,, 
 read back from the same file,, compare the sums of the two lists,, add these three to a tuple
 Create a function that returns leven,, use leven in another function,, *)
 

(*  define a function check_odd_rev: string -> int -> (int list * int list * bool) 
 *  that takes the name of a file and a positive integer n and writes in the file 
 *  the list of the firstn odd numbers using write_list_int. 
 *  Let's call the previous list lodd. 
 *  It then reads back from the same file using read_list_int_rev 
 *  and returns the list of integers loddread.
 *  Finally, the function returns a tuple of three elements. The three elements
 *  are lodd, loddread, and a boolean which is true if lodd is the same as loddread in
 *  reversed order and false otherwise.
 *)
     
 let check_odd_rev (file : string) (n : int) : (int list * int list * bool) =
  let lodd = take n odds in
         let _ = write_list_int file lodd in
         let loddread = read_list_int_rev file in
         (lodd, loddread, lodd = List.rev loddread )
         
                            
(* 
 *  define a function stream_zip: 'a stream -> 'b stream -> ('a * 'b) stream that
 *  takes two streams of elements and returns a stream of the paired elements.
 *  For instance given the streams of natural numbers greater than 0,  
 *  and the streams of primes, stream_zip should return a stream of pairs of integers 
 *  where each pairs is of the form (i, pi) where pi is the i-th prime number, for i>0.
*)

 let rec stream_zip (s1 : 'a stream) (s2 : 'b stream) : ('a * 'b) stream =
     fun () -> Cons ( ((head s1), (head s2)) , stream_zip (tail s1) (tail s2))

(* 
 *  define a function incremental_map : ('a -> 'a ) -> a' -> 'a stream
 *  that given a function f, and an element a of type 'a 
 *  produces the stream of elements a, (f a), (f (f a)), (f (f (f a))), (f (f (f (f a)))).... 
 *)
 
 let rec incremental_map (func: 'a -> 'a) (elem : 'a) : 'a stream = 
     fun () -> Cons (elem, incremental_map func (func elem))

(*
 *  Use incremental_map to define a stream of floats called exp_seq in which the i-th element is 
 *  the (i-1)-th element squared, starting from 2, i.e. 2, 4, 16, 256, 65536...
 *  This stream can be seen as the sequence of values of the mathematical sequence
 *  n-> exp(2, exp(2, n)), for n=0,1,2...
 *)
 
 let exp_seq = incremental_map (fun x -> x*.x) 2.

