type printable = B of bool   | I of int      | C of char | 
                 S of string | L of int list | P of printable * printable

let ex1 = P (P (C 'z', P (P (L [1; -5; 13], C 'c'), P (I 0, B true))), S "Hello")
let ex2 = P (P (B false, P (P (L [-21; 53; 12], S "c"), P (I 0, B false))), S "Hello")
let ex3 = P (P (C 'f', P (P (L [15; -15; 213], S "c"), P (P (C 't', C 't'), S "false"))),S "Hello")

let rec count_chars (p: printable):int =
        (* write here your code *)
        (* count_chars counts the number of type 'char's *)
        match p with
        | C (c) -> 1
        | B (b) -> 0
        | I (i) -> 0
        | S (s) -> 0
        | L (l) -> 0
        | P (a,b) -> (count_chars a) + (count_chars b)

let rec global_or (p: printable): bool option =
        (* write here your code *)
        match p with
        | B (b) -> if b = true then (Some true) else (Some false)
        | C (c) -> None
        | I (i) -> None
        | S (s) -> None
        | L (l) -> None
        | P (a,b)->
            match (global_or a) with
            | Some true -> Some true
            | Some false ->
                ( match (global_or b) with
                | Some true -> Some true
                | Some false -> Some false
                | None -> Some false )
            | None -> match (global_or b) with
                | Some true -> Some true
                | Some false -> Some false
                | None -> None


let rec f_on_int_list (f: int-> int) (p: printable) : printable =
        (* write here your code *)
        match p with (* check if first & second argument is a list *)
        | L (l) -> L (List.map(f) l) (* Run the function on the int if p contains a list *)
        | I (i) -> I (i)
        | S (s) -> S (s)
        | C (c) -> C (c)
        | B (b) -> B (b)
        | P (a,b) -> P((f_on_int_list (f) a), (f_on_int_list (f) b))

let rec sum_all_ints (p: printable) : int option =
        (* write here your code *)
    match p with
    | I (i) -> Some i
    | C (c) -> None
    | S (s) -> None
    | B (b) -> None
    | L (l) -> Some ( List.fold_left(+) 0 l )
| P (a,b) -> ( match sum_all_ints a with
    | Some i -> ( match sum_all_ints b with
                | Some eye -> Some (i + eye)
                | None -> Some i )
    | None -> ( match sum_all_ints b with
                | Some i-> Some i
                | None -> None ) )

let string_of_intlist l =
    let stringlist = List.map(string_of_int) l in
    List.fold_left(fun acc x -> acc^x) "" stringlist;;

let rec tostring (p: printable): string =
        (* write here your code *)
    match p with
    | S (s) -> s
    | B (b) -> string_of_bool b
    | I (i) -> string_of_int i
    | C (c) -> Char.escaped c
    | L (l) -> string_of_intlist l
    | P (a,b) -> (tostring a)^(tostring b)

