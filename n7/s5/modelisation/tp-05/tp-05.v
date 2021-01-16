
(* 1.  *)
split.
elim factorielle_zero. 
reflexivity.
split. 
omega.
apply H.

(* 1.bis *)
generalize H.
generalize factorielle_zero.
intro.
intuition.

(* 1.ter *)
generalize H.
generalize factorielle_zero.
intros.
split.
exact H0.
exact H1.

(* 2. *)
split.
generalize H3
intros.
omega.
rewrite H5.
omega.

