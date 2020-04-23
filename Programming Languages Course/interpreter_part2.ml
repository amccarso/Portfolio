(* Interpreter part 2 solution for CSE305S18 *)

let explode s =
  let rec exp i l =
    if i < 0 then l else exp (i - 1) (s.[i] :: l) in
  exp (String.length s - 1) []

let implode cl = String.concat "" (List.map (String.make 1) cl)


type stackVal = 
INT of int 
| STR of string 
| BOOL of bool 
| NAME of string
| ERROR 
| UNIT
| CLOSURE of ( (stackVal * stackVal) list *  command list * string)
| INOUT of ( (stackVal * stackVal) list * command list * string)

and command = 
  ADD | SUB | MUL | DIV | REM | SWAP | POP | NEG | PUSH of stackVal | QUIT (* Part 1 (arithmetic) *)
  | AND | OR | NOT | IF | EQUAL | LESSTHAN | CAT | BIND | LET | END (* Part 2 (scopes, variables, and logic)*)
  | CALL | FUNCTION of (string * string) | IOFUNC of (string * string) | FUNEND

let rec toString(x : stackVal) : string = 
  match x with
      INT(i) -> if i < 0 then "-"^string_of_int(-i) else string_of_int(i)
    | STR(s)  -> s
    | BOOL(b) -> ":"^string_of_bool(b)^":"
    | NAME(n) -> n
    | ERROR   -> ":error:"
    | UNIT    -> ":unit:"
    | CLOSURE(env, code, arg) -> ":unit:"
    | INOUT(env, code, arg) -> ":unit:"



	
let comtoString (x) = 
  match x with
    ADD         -> "ADD"
  | SUB         -> "SUB"
  | MUL         -> "MUL"
  | DIV         -> "DIV"
  | REM         -> "REM"
  | SWAP        -> "SWAP"
  | POP         -> "POP"
  | NEG         -> "NEG"
  | PUSH(s)     -> "PUSH " ^ toString(s)
  | QUIT        -> "QUIT"
  | IF          -> "IF"
  | EQUAL       -> "EQUAL"
  | LESSTHAN    -> "LESSTHAN"
  | CAT         -> "CAT"
  | BIND        -> "BIND"
  | LET         -> "LET"
  | END         -> "END"
  | AND         -> "AND"
  | OR          -> "OR"
  | NOT         -> "NOT"
  | CALL        -> "CALL"
  | FUNCTION(word, arg)    -> "FUNCTION " ^ word ^ " " ^ arg
  | IOFUNC(word, arg)      -> "IOFUNC " ^ word ^ " " ^ arg
  | FUNEND      -> "FUNEND"
  
(*************************************************************************************************)
(* BIND LOOKUP *)
(*************************************************************************************************)

let rec eval ((a : stackVal),(b : (stackVal * stackVal) list list)) : stackVal =
  match (a,b) with
    (NAME(x), environment) ->
    (
    match environment with
      ((NAME(y), value)::bs)::bss -> if y = x then value else eval(NAME(x), bs::bss)
    | ((inletid, _)::bs)::bss  -> ERROR
    | []::bss -> eval(NAME(x),bss)
    | [] -> ERROR
    )
    | _ -> ERROR

(*************************************************************************************************)
(* PARSING INPUT *)
(*************************************************************************************************)

let digits = explode "0123456789"
let alpha = explode "_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
let alphanum = alpha @ digits


let stripQuotes(s : string) : string = 
  let stripHead (chs : char list) : char list =
      match chs with
        '\"'::xs -> xs
      | z         -> z
    in
    let rec stripTail (chs : char list) : char list =
      match chs with
        '\"'::[] -> []
      | c::cs     -> c::stripTail(cs)
      | []        -> []
  in
    implode(stripTail(stripHead(explode s)))


let rec checkCh ((set : char list), (ch : char)) : bool = 
  match set with
    s::rest -> if s = ch then true else checkCh (rest, ch)
  | []    -> false

let rec checkChs ((set : char list), (chs : char list)) : bool = 
  match chs with
    c::cs -> if checkCh(set, c) then checkChs(set, cs) else false
  | []    -> true

let rec stripLeadingWhitespace s = 
  match s with
    ' '::x::xs  -> if checkCh(alphanum, x) then 
	                  implode(x::xs) 
				    else stripLeadingWhitespace(x::xs)
  | '\t'::x::xs -> if checkCh(alphanum, x) then 
                      implode(x::xs) 
					else stripLeadingWhitespace(x::xs)
  | x -> implode s

let parseInt str sign : stackVal =
  if checkChs(digits, explode str) then
    INT((int_of_string str) * sign)
  else ERROR
  (*handle _ -> ERROR*)

let parseName str : stackVal = 
  match (explode str) with
    x::xs -> if checkCh(alpha, x) then
	           if checkChs(alphanum, xs) then 
			       NAME(str) 
			     else ERROR
			   else ERROR
   | _    -> ERROR
   
let parseBoolError (s : string) : stackVal = match explode(s) with
      (':')::('t')::cs -> BOOL(true)
    | (':')::('f')::cs -> BOOL(false)
    | (':')::('e')::cs -> ERROR
    | _              -> ERROR
    
let parseLiteral(s : string) : stackVal = 
    match explode(s) with
        '-'::cs -> (parseInt (implode cs) (-1))
        | '\"'::cs -> STR(stripQuotes s)
        | ':'::cs  -> parseBoolError s
        | c::cs -> if checkCh(digits, c) then parseInt s 1 else parseName(s)
        | _ -> ERROR


(*************************************************************************************************)
(* PARSE STRINGS INTO command LIST *)
(*************************************************************************************************)
let rec parsecommands (l : string list) : (command list) = 
  match l with
    |[] -> []
    | s::rest ->
        let tokens = String.split_on_char ' ' s (* creates a string list from the line of input, where each element was separated by a space *)
        in
        match tokens with
          "push"::xs     -> PUSH(parseLiteral (String.sub s 5 ((String.length(s) - 5))))::(parsecommands rest)
        | "add"::xs      -> ADD:: (parsecommands rest)
        | "sub"::xs      -> SUB::parsecommands rest
        | "mul"::xs      -> MUL::parsecommands rest
        | "div"::xs      -> DIV::parsecommands rest
        | "rem"::xs      -> REM::parsecommands rest
        | "swap"::xs     -> SWAP::parsecommands rest
        | "pop"::xs      -> POP::parsecommands rest 
        | ":false:"::xs  -> PUSH(BOOL false)::parsecommands rest
        | ":true:"::xs   -> PUSH(BOOL true)::parsecommands rest
        | ":error:"::xs  -> PUSH (ERROR) :: parsecommands rest
        | "neg"::xs      -> NEG::parsecommands rest
        | "and"::xs      -> AND::parsecommands rest
        | "or"::xs       -> OR::parsecommands rest
        | "not"::xs      -> NOT::parsecommands rest
        | "if"::xs       -> IF::parsecommands rest
        | "equal"::xs    -> EQUAL::parsecommands rest
        | "lessThan"::xs -> LESSTHAN::parsecommands rest
        | "bind"::xs     -> BIND::parsecommands rest
        | "let"::xs      -> LET::parsecommands rest
        | "end"::xs      -> END::parsecommands rest
        | "quit"::xs     -> QUIT::parsecommands rest
        | "cat"::xs      -> CAT::parsecommands rest
        | "fun"::xs      -> FUNCTION(List.nth (String.split_on_char ' ' (String.sub s 5 ((String.length(s) - 5)))) 0, List.nth (String.split_on_char ' ' (String.sub s 5 ((String.length(s) - 5)))) 1)::parsecommands rest
        | "inOutFun"::xs -> IOFUNC(List.nth (String.split_on_char ' ' (String.sub s 5 ((String.length(s) - 5)))) 0, List.nth (String.split_on_char ' ' (String.sub s 5 ((String.length(s) - 5)))) 1)::parsecommands rest
        | "call"::xs     -> CALL::parsecommands rest
        | ""::xs         -> parsecommands rest
        | "funEnd"::xs   -> FUNEND::parsecommands rest
        | x::xs          -> PUSH (ERROR) :: parsecommands rest
        | _ -> []
    
(*************************************************************************************************) 
(* PART 1 - ARITHMETIC & STACK MANIPULATION FUNCTIONS *)
(*************************************************************************************************) 
let callPop (stk : stackVal list) =
  match stk with
    (s::t) -> t
  | _  -> ERROR::stk

let callSwap (stk : stackVal list) =
  match stk with
    (s1::s2::stk) -> s2::s1::stk
    | _             -> ERROR::stk
                                     
let callAdd (stk,bindings) = 
  match (stk,bindings) with
    (INT(x)::INT(y)::stk, bindings) -> INT(x+y)::stk
  | (INT(x)::NAME(y)::stk, bindings) ->
   (
      match eval(NAME y, bindings) with
        INT z -> INT(x+z)::stk
        | _    -> ERROR::INT(x)::NAME(y)::stk
        )
  | (NAME(x)::INT(y)::stk, bindings) ->
   (
      match eval(NAME x, bindings) with
        INT z -> INT(y+z)::stk
        | _    -> ERROR::NAME(x)::INT(y)::stk
        )
  | (NAME(x)::NAME(y)::stk, bindings) ->
   (
      match (eval(NAME x, bindings), eval(NAME(y), bindings)) with
        (INT z, INT z') -> INT(z+z')::stk
        | _               -> ERROR::NAME(x)::NAME(y)::stk
        )
  | (stk, bindings) -> ERROR::stk

let callSub (stk,bindings) = 
  match (stk,bindings) with
    (INT(x)::INT(y)::stk, bindings) -> INT(y-x)::stk
  | (INT(x)::NAME(y)::stk, bindings) -> 
  (
      match eval(NAME y, bindings) with
        INT z -> INT(z-x)::stk
        | _    -> ERROR::INT(x)::NAME(y)::stk
        )

  | (NAME(x)::INT(y)::stk, bindings) -> (
      match eval(NAME x, bindings) with
        INT z -> INT(y-z)::stk
        | _    -> ERROR::NAME(x)::INT(y)::stk)
  | (NAME(x)::NAME(y)::stk, bindings) -> 
  (
      match (eval(NAME x, bindings), eval(NAME y, bindings)) with
        (INT z, INT z') -> INT(z'-z)::stk
        | _               -> ERROR::NAME(x)::NAME(y)::stk
        )
  | (stk, bindings) -> ERROR::stk

let callMul (stk,bindings) = 
  match (stk,bindings) with
    (INT(x)::INT(y)::stk, bindings) -> INT(x*y)::stk
  |  (INT(x)::NAME(y)::stk, bindings) -> (
      match eval(NAME y, bindings) with
        INT z -> INT(x*z)::stk
        | _    -> ERROR::INT(x)::NAME(y)::stk)
  |  (NAME(x)::INT(y)::stk, bindings) -> (
      match eval(NAME x, bindings) with
        INT z -> INT(y*z)::stk
        | _    -> ERROR::NAME(x)::INT(y)::stk)
  |  (NAME(x)::NAME(y)::stk, bindings) -> (
      match (eval(NAME x, bindings), eval(NAME y, bindings)) with
        (INT z, INT z') -> INT(z*z')::stk
        | _               -> ERROR::NAME(x)::NAME(y)::stk)
  |  (stk, bindings) -> ERROR::stk
       
let callDiv (stk,bindings) = 
  match (stk,bindings) with
    (INT(0)::stk, bindings) -> ERROR::INT(0)::stk
  |  (INT(x)::INT(y)::stk, bindings) -> INT(y / x)::stk
  |  (INT(x)::NAME(y)::stk, bindings) -> 
  (
      match eval(NAME y, bindings) with
        INT z -> INT(z / x)::stk
        | _    -> ERROR::INT(x)::NAME(y)::stk
        )
  |  (NAME(x)::INT(y)::stk, bindings) -> (
      match eval(NAME x, bindings) with
          INT 0 -> ERROR::NAME(x)::INT(y)::stk
        | INT z -> INT(y / z)::stk
        | _    -> ERROR::NAME(x)::INT(y)::stk)
  |  (NAME(x)::NAME(y)::stk, bindings) -> (
      match (eval(NAME x, bindings), eval(NAME y, bindings)) with
          (INT 0, INT z') -> ERROR::NAME(x)::NAME(y)::stk
        | (INT z, INT z') -> INT(z' / z)::stk
        | _               -> ERROR::NAME(x)::NAME(y)::stk)
  |  (stk, bindings) -> ERROR::stk    

let callRem (stk,bindings) = 
  match (stk,bindings) with
    (INT(0)::stk, bindings) -> ERROR::INT(0)::stk
  |  (INT(x)::INT(y)::stk, bindings) -> INT(y mod x)::stk
  |  (INT(x)::NAME(y)::stk, bindings) -> (
      match eval(NAME y, bindings) with
        INT(z) -> INT(z mod x)::stk
        | _    -> ERROR::INT(x)::NAME(y)::stk)
  |  (NAME(x)::INT(y)::stk, bindings) -> (
      match eval(NAME x, bindings) with
          INT 0 -> ERROR::NAME(x)::INT(y)::stk
        | INT z -> INT(y mod z)::stk
        | _      -> ERROR::NAME(x)::INT(y)::stk)
  |  (NAME(x)::NAME(y)::stk, bindings) -> (
      match (eval(NAME x, bindings), eval(NAME y, bindings)) with
          (INT 0, INT z') -> ERROR::NAME(x)::NAME(y)::stk
        | (INT z, INT z') -> INT(z' mod z)::stk
        | _                 -> ERROR::NAME(x)::NAME(y)::stk)
  | (stk, bindings) -> ERROR::stk
       
let callNeg (stk,bindings) = 
  match (stk,bindings) with
    (INT(x)::stk, bindings) -> INT(-x)::stk
  |  (NAME(x)::stk, bindings) -> (match eval(NAME(x), bindings) with
        INT z -> INT(-z)::stk
        | _    -> ERROR::NAME(x)::stk)
  |  (stk, bindings) -> ERROR::stk

(*************************************************************************************************)
(* PART 2 - LOGICAL/STRING FUNCTIONS, VARIABLES & SCOPING *)
(*************************************************************************************************)

let callAnd (stk,bindings) = 
  match (stk,bindings) with
    (BOOL(x)::BOOL(y)::stk, bindings) -> BOOL(x && y)::stk
  |  (BOOL(x)::NAME(y)::stk, bindings) -> (
      match eval(NAME y, bindings) with
        BOOL z -> BOOL(x && z)::stk
        | _    -> ERROR::BOOL(x)::NAME(y)::stk)
  |  (NAME(x)::BOOL(y)::stk, bindings) -> (
      match eval(NAME x, bindings) with
        BOOL z -> BOOL(y && z)::stk
        | _    -> ERROR::NAME(x)::BOOL(y)::stk)
  |  (NAME(x)::NAME(y)::stk, bindings) -> (
      match (eval(NAME x, bindings), eval(NAME y, bindings)) with
        (BOOL z, BOOL z') -> BOOL(z && z')::stk
        | _               -> ERROR::NAME(x)::NAME(y)::stk)
  |  (stk, bindings) -> ERROR::stk
 
let callOr (stk,bindings) = 
  match (stk,bindings) with
    (BOOL(x)::BOOL(y)::stk, bindings) -> BOOL(x || y)::stk
  |  (BOOL(x)::NAME(y)::stk, bindings) -> (
      match eval(NAME y, bindings) with
        BOOL z -> BOOL(x || z)::stk
        | _    -> ERROR::BOOL(x)::NAME(y)::stk)
  |  (NAME(x)::BOOL(y)::stk, bindings) -> (
      match eval(NAME x, bindings) with
        BOOL z -> BOOL(y || z)::stk
        | _    -> ERROR::NAME(x)::BOOL(y)::stk)
  |  (NAME(x)::NAME(y)::stk, bindings) -> (
      match (eval(NAME x, bindings), eval(NAME y, bindings)) with
        (BOOL z, BOOL z') -> BOOL(z || z')::stk
        | _               -> ERROR::NAME(x)::NAME(y)::stk)
  |  (stk, bindings) -> ERROR::stk
 
let callEqual (stk,bindings) = 
  match (stk,bindings) with
    (INT(x)::INT(y)::stk, bindings) -> BOOL(x=y)::stk
  |  (INT(x)::NAME(y)::stk, bindings) -> (
      match eval(NAME y, bindings) with
        INT z -> BOOL(x=z)::stk
        | _   -> ERROR::INT(x)::NAME(y)::stk)
  |  (NAME(x)::INT(y)::stk, bindings) -> (
      match eval(NAME x, bindings) with
        INT z -> BOOL(y=z)::stk
        | _   -> ERROR::NAME(x)::INT(y)::stk)
  |  (NAME(x)::NAME(y)::stk, bindings) -> (match (eval(NAME(x), bindings), eval(NAME(y), bindings)) with
        (INT z, INT z') -> BOOL(z=z')::stk
        | _             -> ERROR::NAME(x)::NAME(y)::stk)
  |  (stk, bindings) -> ERROR::stk
  
let callLessThan (stk,bindings) = 
  match (stk,bindings) with
    (INT(x)::INT(y)::stk, bindings) -> BOOL(y < x)::stk
  |  (INT(x)::NAME(y)::stk, bindings) -> (
      match eval(NAME y, bindings) with
        INT z  -> BOOL(z < x)::stk
        | _    -> ERROR::INT(x)::NAME(y)::stk)
  |  (NAME(x)::INT(y)::stk, bindings) -> (
      match eval(NAME x, bindings) with
        INT z  -> BOOL(y < z)::stk
        | _    -> ERROR::NAME(x)::INT(y)::stk)
  |  (NAME(x)::NAME(y)::stk, bindings) -> (
      match (eval(NAME x, bindings), eval(NAME y, bindings)) with
        (INT z, INT z') -> BOOL(z' < z)::stk
        | _             -> ERROR::NAME(x)::NAME(y)::stk)
  |  (stk, bindings) -> ERROR::stk

let callIf (stk,bindings) = 
  match (stk,bindings) with
    (x::y::BOOL(z)::stk, bindings) -> (
      match z with
        true  -> x::stk
      | false -> y::stk)
  |  (x::y::NAME(z)::stk, bindings) -> (
      match eval(NAME z, bindings) with
        BOOL true  -> x::stk
      | BOOL false -> y::stk
      | _           -> ERROR::x::y::NAME(z)::stk)
  |  (stk, bindings) -> ERROR::stk

let callNot (stk,bindings) = 
  match (stk,bindings) with
    (BOOL(x)::stk, bindings) -> BOOL(not x)::stk
  |  (NAME(x)::stk, bindings) -> (
      match eval(NAME x, bindings) with
        BOOL z -> BOOL(not z)::stk
        | _    -> ERROR::NAME(x)::stk)
  |  (stk, bindings) -> ERROR::stk
  
let callCat (stk,bindings) = 
  match (stk,bindings) with
    (STR(s2)::STR(s1)::stk, bindings) -> STR(s1^s2)::stk
  |  (NAME(x)::STR(s1)::stk, bindings) -> (
      match eval(NAME x, bindings) with
            STR s2 -> STR(s1^s2)::stk
          | _ -> ERROR::NAME(x)::STR(s1)::stk)
  |  (STR(s2)::NAME(x)::stk, bindings) -> (
      match eval(NAME x, bindings) with
            STR s1 -> STR(s1^s2)::stk
          | _ -> ERROR::STR(s2)::NAME(x)::stk)
  |  (NAME(y)::NAME(x)::stk, bindings) -> (
      match (eval(NAME x, bindings), eval(NAME y, bindings)) with
        (STR s1, STR s2) -> STR(s1^s2)::stk
      | _ -> ERROR::NAME(y)::NAME(x)::stk)
  |  (stk, bindings) -> ERROR::stk
  
let callBind (stk,bindings) = 
  match (stk,bindings) with
    (ERROR::stk, currentScope::bindings) -> (ERROR::ERROR::stk, currentScope::bindings)
  | (NAME(x)::NAME(y)::stk, currentScope::bindings) -> (
      match eval(NAME x, currentScope::bindings) with
          ERROR -> (ERROR::NAME(x)::NAME(y)::stk, currentScope::bindings)
        | z     -> (UNIT::stk, ((NAME y, z)::currentScope)::bindings))
  | (x::NAME(y)::stk, currentScope::bindings) -> (UNIT::stk, ((NAME y, x)::currentScope)::bindings)
  | (stk, bindings) -> (ERROR::stk, bindings)

let callEnd (c, stk, bindings) = 
  match (c, stk, bindings) with
    (c, (s::stack1)::stack2::stacks, old::restBinds) -> (c, (s::stack2)::stacks, restBinds)
  | (c, stack::stacks, old::restBinds) -> (c, stacks, restBinds)
  | (c,s,b) -> (c,s,b)
  
(*************************************************************************************************)
(* PART 3 - FUNCTIONS, INOUT, CALL *)
(*************************************************************************************************)


let rec getCode (code, comms) =
    match comms with
    FUNEND::comms -> code
    | c::comms -> getCode((c::code), comms)
    | [] -> []
    
let callFunction (stk, bindings, comms, name, arg) = 
    let env = (match bindings with
                binds::bindings -> binds
                | [] -> []) in
        let code = getCode([], comms) in
            let closure = (NAME name, CLOSURE (env, code, arg)) in 
                let _ = (match bindings with
                binds::bindings -> (closure::binds)::bindings
                | [] -> (closure::[])::bindings) in UNIT::stk
    
    
(* call to eval: eval name env
pop vals from stack then evaluate
assign arg to param
append closure env to stack
create new stack
get code and execute function
if funName is id or identity
    append argument to the stack
if function is IOFunc
    create function to replace name of param with arg
execute commands in code until return is reached
if function is IOFunc then change it's value in binds
*)

let rec parseCode (code, stk, env) =
    match code with
    c::code -> 0
    
let call (stk, bindings) = 
    match  (stk, bindings) with
    (arg::name::stk) -> (let argu = (eval arg env) in 
            let func = (eval name env) in
            let func = (match func with
                env::code::arg -> env::code::argu
                | [] -> []) in
            let bindings = func::bindings in
            let stack = [[]] in
            )
    | x::stk -> ERROR::x::stk
    
let callInOut (stk, bindings, comms, name, arg) = 
    let env = (match bindings with
                binds::bindings -> binds
                | [] -> []) in
        let code = getCode([], comms) in
            let closure = (NAME name, INOUT (env, code, arg)) in 
                let _ = (match bindings with
                binds::bindings -> (closure::binds)::bindings
                | [] -> (closure::[])::bindings) in UNIT::stk
 


(*************************************************************************************************)
(* DRIVER FUNCTIONS *)
(*************************************************************************************************)
  
let rec interpret ((com : command list),(stk: stackVal list list), (bindings: (stackVal * stackVal) list list)): stackVal list =
  match (com,stk,bindings) with
  (c::comms , stack::stacks , bindings )  -> 
  (
    match c with
    PUSH(x)  -> interpret(comms, (x::stack)::stacks, bindings)
  | ADD      -> interpret(comms, callAdd(stack, bindings)::stacks, bindings)
  | SUB      -> interpret(comms, callSub(stack, bindings)::stacks, bindings)
  | MUL      -> interpret(comms, callMul(stack, bindings)::stacks, bindings)
  | DIV      -> interpret(comms, callDiv(stack, bindings)::stacks, bindings)
  | REM      -> interpret(comms, callRem(stack, bindings)::stacks, bindings)
  | SWAP     -> interpret(comms, callSwap(stack)::stacks, bindings)
  | POP      -> interpret(comms, callPop(stack)::stacks, bindings)
  | NEG      -> interpret(comms, callNeg(stack, bindings)::stacks, bindings)
  | AND      -> interpret(comms, callAnd(stack, bindings)::stacks, bindings)
  | OR       -> interpret(comms, callOr(stack, bindings)::stacks, bindings)
  | NOT      -> interpret(comms, callNot(stack, bindings)::stacks, bindings)
  | IF       -> interpret(comms, callIf(stack, bindings)::stacks, bindings)
  | EQUAL    -> interpret(comms, callEqual(stack, bindings)::stacks, bindings)
  | LESSTHAN -> interpret(comms, callLessThan(stack, bindings)::stacks, bindings)
  | CAT      -> interpret(comms, callCat(stack, bindings)::stacks, bindings)
  | BIND     -> (match callBind(stack, bindings) with 
                        (newStack, newBinds) -> interpret(comms, newStack::stacks, newBinds))
  | LET      -> interpret(comms, []::stack::stacks, ([]::bindings))
  | END      -> interpret(callEnd(comms, stack::stacks, bindings))
  | CALL     -> interpret(comms, call(stack, bindings)::stacks, bindings)
  | FUNCTION(name, arg) -> interpret(comms, callFunction(stack, bindings, comms, name, arg)::stacks, bindings)
  | IOFUNC(name, arg)   -> interpret(comms, callInOut(stack, bindings, comms, name, arg)::stacks, bindings)
  | QUIT     -> stack
  | FUNEND   -> stack
  )
  | _ -> []


(*************************************************************************************************)
(* WRITING AND READING HELPER FUNCTIONS *)
(*************************************************************************************************)
let read_lines inc =
  let rec loop_read acc =
    try 
      let l=input_line inc in 
      loop_read (l::acc)
    with
      | End_of_file -> List.rev acc
  in
    loop_read []

let rec write_all l oc=
   match l with 
     | [] -> ()
     | hd::tl ->  
             let () =Printf.fprintf oc "%s\n" hd  in 
             write_all tl oc

(*************************************************************************************************)
(* INTERPRETER FUNCTION *)
(*************************************************************************************************)

let interpreter (inputFile : string) (outputFile : string) =
  let ic = open_in inputFile in
    let oc = open_out outputFile in
      let inList = read_lines ic in
        let commands = parsecommands(inList) in
          let finalStack = (interpret(commands, [[]], [[]])) in
	           let stringList = List.map toString finalStack in
                let _ = write_all stringList oc in
                  let _= close_in ic in 
                    let _= close_out oc in () 

(*let _ = interpreter "input2/input13.txt" "testout.txt"*)
