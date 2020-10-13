(*Groupe L1
Chaimae OUARDANI
Edgar REMY
Hamid OUKHNINI
Maxence PERICAT
Sebastien PONT
*)

Section CalculPredicats.
Variable A B : Type.

Theorem Thm_8 : forall (P Q : A -> Prop),
(forall x1 : A, (P x1) /\ (Q x1))
-> (forall x2 : A, (P x2)) /\ (forall x3 : A, (Q x3)).

intros.
split.
intro.
cut (P x2 /\ Q x2).
intros.
destruct H0.
exact H0.
generalize x2.
exact H.
intros.
cut (P x3 /\ Q x3).
intros.
destruct H0.
exact H1.
generalize x3.
exact H.
Qed.

Theorem Thm_8_malin : forall (P Q : A -> Prop),
(forall x1 : A, (P x1) /\ (Q x1))
-> (forall x2 : A, (P x2)) /\ (forall x3 : A, (Q x3)).

intros.
split.
intro.
apply (H x2).
intros.
apply (H x3).
Qed.


Theorem Thm_9 : forall (P : A -> B -> Prop),
(exists x1 : A, forall y1 : B, (P x1 y1))->  forall y2 : B, exists x2 : A, (P x2 y2).
intros.
destruct H.
exists x.
generalize y2.
exact H.
Qed.

Theorem Thm_10 : forall (P Q : A -> Prop),
(exists x1 : A, (P x1) -> (Q x1))-> (forall x2 : A, (P x2))  ->  exists x3 : A, (Q x3).
intros .
destruct H.
exists x.
apply H.
generalize x.
exact H0.
Qed.

End CalculPredicats.